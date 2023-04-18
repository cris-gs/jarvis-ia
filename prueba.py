import pickle
import pandas as pd
import numpy as np

def precioBitcoin(date):

    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloPrecioBitcoin.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Cargar los datos de entrenamiento
    data = pd.read_csv(r'D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Data\bitcoin_price_Training - bitcoin_price.2013Apr-2017Aug.csv.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    prediction_date = modelo.forecast(steps=dias)
    dias = (prediction_date - data.index[-1]).days

    # Hacer predicciones para el DataFrame de prueba
    predicciones = modelo.predict(np.array([[dias]]))

    # Imprimir las predicciones
    print(f'El precio de Bitcoin para el {prediction_date.date()} será de ${predicciones[0]:.2f}')
    return predicciones[0]


precioBitcoin('2017-08-08')