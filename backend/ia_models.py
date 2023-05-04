import pickle
import pandas as pd
import numpy as np
import re
import os
from unidecode import unidecode

# *Dependencias:
# * pip install pandas
# * pip install scikit-learn
# * pip install statsmodels
# * pip install unidecode
# * pip install flask

# * Run command: python app.py

# /precioBitcoin/2017-08-08
def precioBitcoin(date):

    # Cargar el modelo guardado con pickle
    with open('./Modelos/modeloPrecioBitcoin.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Cargar los datos de entrenamiento
    data = pd.read_csv('./Data/bitcoin_price_Training - bitcoin_price.2013Apr-2017Aug.csv.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)
    try:
        prediction_date = pd.to_datetime(date)
    except:
        return 'Lo siento, no se pudo predecir el precio del Bitcoin debido a que se ingresó un dato incorrecto'
    dias = (prediction_date - data.index[-1]).days

    # Hacer predicciones para el DataFrame de prueba
    predicciones = modelo.forecast(steps=dias)

    # Imprimir las predicciones
    print(f'El precio de Bitcoin para el {prediction_date.date()} será de {predicciones[0]:.2f} dolares')
    return str(f'El precio de Bitcoin para el {prediction_date.date()} será de {predicciones[0]:.2f} dolares')

# /precioAutomovil/3/15000/50000/Gasolina/Particular/Manual/1
def precioAutomovil(age, presentPrice, kmsDriven, fuelType, sellerType, transmission, owner):

    # Cargar el modelo guardado con pickle
    with open('./Modelos/modeloPrecioAutomovil.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Codificar las variables categóricas (tipo de combustible, tipo de vendedor y transmisión)
    # fuelTypeCod = 1 if fuelType.lower() == 'gasolina' else 0
    # sellerTypeCod = 1 if sellerType.lower() == 'particular' else 0
    # transmissionCod = 1 if transmission.lower() == 'manual' else 0

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        'Age': [age],
        'Present_Price': [presentPrice],
        'Kms_Driven': [kmsDriven],
        'Fuel_Type': [fuelType],
        'Seller_Type': [sellerType],
        'Transmission': [transmission],
        'Owner': [owner],
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('El precio de venta del automóvil es de:', str(round(predicciones[0][0], 3)), 'dolares')
    return ('El precio de venta del automóvil es de:', str(round(predicciones[0][0], 3)), 'dolares')

# /recomendarPelicula/Tom and Huck/5
def recomendarPelicula(title, num_recommendations):

    movies = pd.read_csv('./Data/movies.csv')
    ratings = pd.read_csv('./Data/ratings.csv')
    data = pd.merge(movies, ratings, on='movieId')

    # Seleccionar las columnas necesarias del dataframe
    ratings_matrix = pd.pivot_table(
        data, values='rating', index='userId', columns='title').fillna(0)
    
    # Cargar el modelo guardado con pickle
    with open('./Modelos/modeloRecomendarPelicula.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Obtener el índice de la película a partir del título
    try:
        title = re.escape(title)
        idx = movies.loc[movies['title'].str.contains(title)].index[0]
        
        # Obtener las películas similares utilizando el modelo KNN
        distances, indices = modelo.kneighbors(ratings_matrix.iloc[idx, :].values.reshape(
            1, -1), n_neighbors= num_recommendations+1)
    except IndexError: 
        return "Lo siento, no pude realizar la recomendación debido a que la película no ha sido encontrada"

    # Crear una lista para almacenar las recomendaciones
    # movie_recommendations = []

    # Recorrer las películas similares y añadir sus títulos a la lista de recomendaciones
    movie_response = ''
    for i in range(1, len(distances.flatten())):
        # movie_recommendations.append(
        #     movies.iloc[indices.flatten()[i]]['title'])
        print('{0}: {1}, con una distancia de {2}'.format(
            i, movies.iloc[indices.flatten()[i]]['title'], round(distances.flatten()[i], 3)))
        movie_response = movie_response+ ', '+'{0}: {1}, con una distancia de {2}'.format(
            i, movies.iloc[indices.flatten()[i]]['title'], round(distances.flatten()[i], 3))

    return movie_response

def replace_data(data, column, values):
    if(len(values) == 2):
        if data[column].isin(values).any():
            data[column].replace({values[0]: 0, values[1]: 1}, inplace=True)
        else:
            data[column].replace({data[column]: 0}, inplace=True)
    else:
        if data[column].isin(values).any():
            data[column].replace({values[0]: 0, values[1]: 1, values[2]: 2}, inplace=True)
        else:
            data[column].replace({data[column]: 0}, inplace=True)

#/clienteCompañiaCelular/Male/0/No/No/56/Yes/Yes/Fiber optic/Yes/Yes/Yes/Yes/Yes/Yes/Two year/Yes/Credit card (automatic)/110.50/6045.90
def clienteCompañiaCelular(gender, seniorCitizen, partner, dependents, tenure, phoneService, multipleLines,
                           internetService, onlineSecurity, onlineBackup, deviceProtection, techSupport, 
                           streamingTV, streamingMovies, contract, paperlessBilling, paymentMethod, monthlyCharges, totalCharges):

    # Cargar el modelo guardado con pickle
    with open('./Modelos/modeloClienteCompañiaCelular.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)
    
    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        'gender': [gender],
        'SeniorCitizen': [seniorCitizen],
        'Partner': [partner],
        'Dependents': [dependents],
        'tenure': [tenure],
        'PhoneService': [phoneService],
        'MultipleLines': [multipleLines],
        'InternetService': [internetService],
        'OnlineSecurity': [onlineSecurity],
        'OnlineBackup': [onlineBackup],
        'DeviceProtection': [deviceProtection],
        'TechSupport': [techSupport],
        'StreamingTV': [streamingTV],
        'StreamingMovies': [streamingMovies],
        'Contract': [contract],
        'PaperlessBilling': [paperlessBilling],
        'PaymentMethod': [paymentMethod],
        'MonthlyCharges': [monthlyCharges],
        'TotalCharges': [totalCharges],
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    if predicciones == 1:
        print('El cliente va a dejar la compañía de celulares')
        return('El cliente va a dejar la compañía de celulares')
    else:
         print('El cliente no va a dejar la compañía de celulares')
         return('El cliente no va a dejar la compañía de celulares')

#/masaCorporal/1.0/3/50.0/100.0/20.0/50.0/40.0/30.0/20.0/15.0/10.0/15.0/10.0/8.0
def masaCorporal(density, age, weight, height, neck, chest, abdomen, hip, thigh, knee, ankle, biceps, forearm, wrist):
    # Cargar el modelo guardado con pickle
    with open('./Modelos/modeloMasaCorporal.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        "Density": [density],
        "Age": [age],
        "Weight": [weight],
        "Height": [height],
        "Neck": [neck],
        "Chest": [chest],
        "Abdomen": [abdomen],
        "Hip": [hip],
        "Thigh": [thigh],
        "Knee": [knee],
        "Ankle": [ankle],
        "Biceps": [biceps],
        "Forearm": [forearm],
        "Wrist": [wrist]
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('La masa corporal del paciente es:', str(round(predicciones[0], 3)))
    return 'La masa corporal del paciente es:', str(round(predicciones[0], 3))

#/calidadVino/8.9/0.3/0.38/2.8/0.10/31/69/0.998/3.25/0.86/12.8/1/0
def calidadVino(fixed, volatile, citric, residualSugar, chlorides, freeSulfurDioxide, 
                totalSulfurDioxide, density, pH, sulphates, alcohol, red, white):
    # Cargar el modelo guardado con pickle
    with open('./Modelos/modeloCalidadVino.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        "fixed acidity": [fixed],
        "volatile acidity": [volatile],
        "citric acid": [citric],
        "residual sugar": [residualSugar],
        "chlorides": [chlorides],
        "free sulfur dioxide": [freeSulfurDioxide],
        "total sulfur dioxide": [totalSulfurDioxide],
        "density": [density],
        "pH": [pH],
        "sulphates": [sulphates],
        "alcohol": [alcohol],
        "type_red": [red],
        "type_white": [white]
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('La calidad del vino es de:', str(predicciones[0]))
    return ('La calidad del vino es de:', str(predicciones[0]))

#/cantidadInventario/Aliss/3/5/2024
def cantidadInventario(store, item, month, year):
    # Cargar el modelo guardado con pickle
    with open('./Modelos/modeloCantidadInventario.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        "store": [store],
        "item": [item],
        "month": [month],
        "year": [year],
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('La cantidad de inventario para el item {}, es de: {}'.format(item, round(predicciones[0], 3)))
    return 'La cantidad de inventario para el item {}, es de: {}'.format(item, round(predicciones[0], 3))

#/tarifaTaxi/1.0/0.5/3.2/2/0.0/Tarjeta de crédito/estándar/0.5/0.3
def tarifaTaxi(driver, mtaTax, distante, numPassenger, tollAmount, paymentMethod, rateCode, extraCharges, improvementCharge):
    # Cargar el modelo guardado con pickle
    with open('./Modelos/modeloTarifaTaxi.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        "driver+AF8-tip": [driver],
        "mta+AF8-tax": [mtaTax],
        "distance": [distante],
        "num+AF8-passengers": [numPassenger],
        "toll+AF8-amount": [tollAmount],
        "payment+AF8-method": [paymentMethod],
        "rate+AF8-code": [rateCode],
        "extra+AF8-charges": [extraCharges],
        "improvement+AF8-charge": [improvementCharge]
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)
    predicciones =  (predicciones * 10) * 0.012
    # Imprimir las predicciones
    print('La tarifa del viaje es de:', str(round(predicciones[0], 3)), 'dolares')
    return ('La tarifa del viaje es de:', str(round(predicciones[0], 3)), 'dolares')

#/delayViajeAvion/1853.0/520/1439.0/1004/UA/172.0/84.0/235.0/48.0/22.0/1230/22.0/0/2.0/11.0
def delayViajeAvion(depTime, crsDepTime, arrTime, crsArrTime, uniqueCarrier, actualElapsedTime, crsElapsedTime, airTime, arrDelay, 
                    depDelay, distance, carrierDelay, weatherDelay, nasDelay, securityDelay):
    # Cargar el modelo guardado con pickle
    with open('./Modelos/modeloViajeAvion.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # * WN: Southwest Airlines, XE: ExpressJet Airlines, YV: Mesa Airlines, OH: PSA Airlines, OO: SkyWest Airlines,
    # * UA: United Airlines, US: US Airways, DL: Delta Air Lines, EV: ExpressJet Airlines, F9: Frontier Airlines,
    # * FL: AirTran Airways, HA: Hawaiian Airlines, MQ: Envoy Air, NW: Northwest Airlines, 9E: Endeavor Air,
    # * AA: American Airlines, AQ: Aloha Airlines, AS: Alaska Airlines, B6: JetBlue Airways, CO: Continental Airlines

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        "DepTime": [depTime],
        "CRSDepTime": [crsDepTime],
        "ArrTime": [arrTime],
        "CRSArrTime": [crsArrTime],
        "UniqueCarrier": [uniqueCarrier],
        "ActualElapsedTime": [actualElapsedTime],
        "CRSElapsedTime": [crsElapsedTime],
        "AirTime": [airTime],
        "ArrDelay": [arrDelay],
        "DepDelay": [depDelay],
        "Distance": [distance],
        "CarrierDelay": [carrierDelay],
        "WeatherDelay": [weatherDelay],
        "NASDelay": [nasDelay],
        "SecurityDelay": [securityDelay]
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('El retraso del vuelo es de:', str(round(predicciones[0]*60, 3)), 'Segundos')
    return ('El retraso del vuelo es de:', str(round(predicciones[0]*60, 3)), 'Segundos')

#/precioAguacate/100.9/60.2/30.6/10.1/150.6/100.4/50.2/0.0/2/2023/San Diego
def precioAguacate(totalVolume, d4046, d4225, d4770, totalBags, smallBags, largeBags, xLargeBags, dtype, year, region):
    # Cargar el modelo guardado con pickle
    with open('./Modelos/modeloPrecioAguacate.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        'Total Volume': [totalVolume],
        '4046': [d4046],
        '4225': [d4225],
        '4770': [d4770],
        'Total Bags': [totalBags],
        'Small Bags': [smallBags],
        'Large Bags': [largeBags],
        'XLarge Bags': [xLargeBags],
        'type': [dtype],
        'year': [year],
        'region': [region]
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('El precio del aguacate es de:', str(round(predicciones[0],3)), 'dolares')
    return ('El precio del aguacate es de:', str(round(predicciones[0],3)), 'dolares')


# print('----------------------------------')
# precioBitcoin('2023-04-21')
# print('----------------------------------')
# precioAutomovil(2, 9.85, 6900, "Gasolina", "Particular", "Manual", 1)
# print('----------------------------------')
# recomendarPelicula("Toy Story (1995)", 5)
# print('----------------------------------')
# clienteCompañiaCelular('masculino', 'no', 'no', 'no', 56, 'si', 'si', 'fibra optica', 'si', 'si', 'si', 'si', 'si', 'si', '2 años', 'si', 'tarjeta de credito', 110.50, 6045.90)
# print('----------------------------------')
# masaCorporal(1.0, 3, 50.0, 100.0, 20.0, 50.0, 40.0, 30.0, 20.0, 15.0, 10.0, 15.0, 10.0, 8.0)
# print('----------------------------------')
# calidadVino(8.9, 0.3, 0.38, 2.8, 0.10, 31, 69, 0.998, 3.25, 0.86, 12.8, 1, 0)
# print('----------------------------------')
# cantidadInventario(1, 3, 5, 2024)
# print('----------------------------------')
# tarifaTaxi(1.0, 0.5, 3.2, 2, 0.0, 'tarjeta de crédito', 'estándar', 0.5, 0.3)
# print('----------------------------------')
# delayViajeAvion(1853.0, 520, 1439.0, 1004, 'UA', 172.0, 84.0, 235.0, 48.0, 22.0, 1230, 22.0, 0, 2.0, 11.0)
# print('----------------------------------')
# precioAguacate(10, 17074.83, 1527.63, 71976.41, 75.78, 8940.04, 97.49, 0.0, 1, 2024, 23)
