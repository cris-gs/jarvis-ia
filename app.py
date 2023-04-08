import pickle
import pandas as pd
import numpy as np
import re

from unidecode import unidecode
from flask import Flask, request

app = Flask(__name__)

#*Dependencias: 
    #* pip install pandas
    #* pip install scikit-learn
    #* pip install statsmodels
    #* pip install unidecode
    #* pip install flask

#* Run command: python app.py

@app.route('/precioBitcoin', methods=['POST'])
def precioBitcoin():
    # Obtener los valores del formulario
    date = request.form.get('date')

    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Modelos\modeloPrecioBitcoin.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Cargar los datos de entrenamiento
    data = pd.read_csv(r'D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Data\bitcoin_price_Training - bitcoin_price.2013Apr-2017Aug.csv.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    prediction_date = pd.to_datetime(date)
    dias = (prediction_date - data.index[-1]).days

    # Hacer predicciones para el DataFrame de prueba
    predicciones = modelo.forecast(steps=dias)

    # Imprimir las predicciones
    print(f'El precio de Bitcoin para el {prediction_date.date()} será de ${predicciones[0]:.2f}')
    return predicciones[0]

@app.route('/precioAutomovil', methods=['POST'])
def precioAutomovil():

    # Obtener los valores del formulario
    age = request.form.get('age')
    presentPrice = request.form.get('presentPrice')
    kmsDriven = request.form.get('kmsDriven')
    fuelType = request.form.get('fuelType')
    sellerType = request.form.get('sellerType')
    transmission = request.form.get('transmission')
    Owner = request.form.get('owner')

    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Modelos\modeloPrecioAutomovil.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Codificar las variables categóricas (tipo de combustible, tipo de vendedor y transmisión)
    fuelTypeCod = 1 if fuelType.lower() == 'gasolina' else 0
    sellerTypeCod = 1 if sellerType.lower() == 'particular' else 0
    transmissionCod = 1 if transmission.lower() == 'manual' else 0


    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        'Age': [age],
        'Present_Price': [presentPrice],
        'Kms_Driven': [kmsDriven],
        'Fuel_Type': [fuelTypeCod],
        'Seller_Type': [sellerTypeCod],
        'Transmission': [transmissionCod],
        'Owner': [Owner],
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('El precio del automóvil es de:', predicciones[0][0])
    return predicciones[0][0]

@app.route('/recomendarPelicula', methods=['POST'])
def recomendarPelicula():

    # Obtener los valores del formulario
    title = request.form.get('title')
    num_recommendations = request.form.get('num_recommendations')

    movies = pd.read_csv('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Data\movies.csv')
    ratings = pd.read_csv(r'D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Data\ratings.csv')
    data = pd.merge(movies, ratings, on='movieId')

    # Seleccionar las columnas necesarias del dataframe
    ratings_matrix = pd.pivot_table(data, values='rating', index='userId', columns='title').fillna(0)

    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Modelos\modeloRecomendarPelicula.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    #Busca el titulo en la lista de películas
    peliculaExistente = False
    for column in ratings_matrix.columns:
        if title in column:
            peliculaExistente = True

    # Verificar si el título de la película se encuentra en ratings_matrix
    if(peliculaExistente == False):
        print("La película '{}' no se encuentra en la matriz de valoraciones.".format(title))
        return "La película '{}' no se encuentra en la matriz de valoraciones.".format(title)

    # Obtener el índice de la película a partir del título
    title = re.escape(title)
    idx = movies.loc[movies['title'].str.contains(title)].index[0]

    # Obtener las películas similares utilizando el modelo KNN
    distances, indices = modelo.kneighbors(ratings_matrix.iloc[idx, :].values.reshape(1, -1), n_neighbors=num_recommendations+1)

    # Crear una lista para almacenar las recomendaciones
    movie_recommendations = []

    # Recorrer las películas similares y añadir sus títulos a la lista de recomendaciones
    for i in range(1, len(distances.flatten())):
        movie_recommendations.append(movies.iloc[indices.flatten()[i]]['title'])
        print('{0}: {1}, con una distancia de {2}'.format(i, movies.iloc[indices.flatten()[i]]['title'], distances.flatten()[i]))
    return movie_recommendations

@app.route('/clienteCompañiaCelular', methods=['POST'])
def clienteCompañiaCelular():

    # Obtener los valores del formulario
    # gender = request.form.get('gender')
    # seniorCitizen = request.form.get('seniorCitizen')
    # partner = request.form.get('partner')
    # dependents = request.form.get('dependents')
    # tenure = request.form.get('tenure')
    # phoneService = request.form.get('phoneService')
    # multipleLines = request.form.get('multipleLines')
    # internetService = request.form.get('internetService')
    # onlineSecurity = request.form.get('onlineSecurity')
    # onlineBackup = request.form.get('onlineBackup')
    # deviceProtection = request.form.get('deviceProtection')
    # techSupport = request.form.get('techSupport')
    # streamingTV = request.form.get('streamingTV')
    # streamingMovies = request.form.get('streamingMovies')
    # contract = request.form.get('contract')
    # paperlessBilling = request.form.get('paperlessBilling')
    # paymentMethod = request.form.get('paymentMethod')
    # monthlyCharges = request.form.get('monthlyCharges')
    # totalCharges = request.form.get('totalCharges')

    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Modelos\modeloClienteCompañiaCelular.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        'gender': [request.form.get('gender')],
        'SeniorCitizen': [request.form.get('seniorCitizen')],
        'Partner': [request.form.get('partner')],
        'Dependents': [request.form.get('dependents')],
        'tenure': [request.form.get('tenure')],
        'PhoneService': [request.form.get('phoneService')],
        'MultipleLines': [request.form.get('multipleLines')],
        'InternetService': [request.form.get('internetService')],
        'OnlineSecurity': [request.form.get('onlineSecurity')],
        'OnlineBackup': [request.form.get('onlineBackup')],
        'DeviceProtection': [request.form.get('deviceProtection')],
        'TechSupport': [request.form.get('techSupport')],
        'StreamingTV': [request.form.get('streamingTV')],
        'StreamingMovies': [request.form.get('streamingMovies')],
        'Contract': [request.form.get('contract')],
        'PaperlessBilling': [request.form.get('paperlessBilling')],
        'PaymentMethod': [request.form.get('paymentMethod')],
        'MonthlyCharges': [request.form.get('monthlyCharges')],
        'TotalCharges': [request.form.get('totalCharges')],
    })

    # Imprimir las predicciones
    test_data["gender"].replace({'Female':0, 'Male':1},inplace = True)
    test_data["Partner"].replace({"No": 0, "Yes": 1}, inplace=True)
    test_data["Dependents"].replace({"No": 0, "Yes": 1}, inplace=True)
    test_data["PhoneService"].replace({"No": 0, "Yes": 1}, inplace=True)
    test_data["MultipleLines"].replace({"No phone service": 0, "No": 1, "Yes": 2}, inplace=True)
    test_data["InternetService"].replace({"No": 0, "DSL": 1, "Fiber optic": 2}, inplace=True)
    test_data["OnlineSecurity"].replace({"No internet service": 0, "No": 1, "Yes": 2}, inplace=True)
    test_data["OnlineBackup"].replace({"No internet service": 0, "No": 1, "Yes": 2}, inplace=True)
    test_data["DeviceProtection"].replace({"No internet service": 0, "No": 1, "Yes": 2}, inplace=True)
    test_data["TechSupport"].replace({"No internet service": 0, "No": 1, "Yes": 2}, inplace=True)
    test_data["StreamingTV"].replace({"No internet service": 0, "No": 1, "Yes": 2}, inplace=True)
    test_data["StreamingMovies"].replace({"No internet service": 0, "No": 1, "Yes": 2}, inplace=True)
    test_data["Contract"].replace({"Month-to-month": 0, "One year": 1, "Two year": 2}, inplace=True)
    test_data["PaperlessBilling"].replace({"No": 0, "Yes": 1}, inplace=True)
    test_data["PaymentMethod"].replace({"Electronic check": 0, "Mailed check": 1, "Bank transfer (automatic)": 2, "Credit card (automatic)": 3}, inplace=True)

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    if predicciones == 1:
        print('El cliente va a dejar la compañía de celulares')
    else:
        print('El cliente no va a dejar la compañía de celulares')
    return predicciones

@app.route('/masaCorporal', methods=['POST'])
def masaCorporal():
    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Modelos\modeloMasaCorporal.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        "Density": [request.form.get('density')],
        "Age": [request.form.get('age')],
        "Weight": [request.form.get('weight')],
        "Height": [request.form.get('height')],
        "Neck": [request.form.get('neck')],
        "Chest": [request.form.get('chest')],
        "Abdomen": [request.form.get('abdomen')],
        "Hip": [request.form.get('hip')],
        "Thigh": [request.form.get('thigh')],
        "Knee": [request.form.get('knee')],
        "Ankle": [request.form.get('ankle')],
        "Biceps": [request.form.get('biceps')],
        "Forearm": [request.form.get('forearm')],
        "Wrist": [request.form.get('wrist')]
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('La masa corporal del paciente es:', predicciones[0])
    return predicciones[0]

@app.route('/calidadVino', methods=['POST'])
def calidadVino():
    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Modelos\modeloCalidadVino.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        "fixed acidity": [request.form.get('fixed')],
        "volatile acidity": [request.form.get('volatile')],
        "citric acid": [request.form.get('citric')],
        "residual sugar": [request.form.get('residualSugar')],
        "chlorides": [request.form.get('chlorides')],
        "free sulfur dioxide": [request.form.get('freeSulfurDioxide')],
        "total sulfur dioxide": [request.form.get('totalSulfurDioxide')],
        "density": [request.form.get('density')],
        "pH": [request.form.get('pH')],
        "sulphates": [request.form.get('sulphates')],
        "alcohol": [request.form.get('alcohol')],
        "type_red": [request.form.get('red')],
        "type_white": [request.form.get('white')]
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('La calidad del vino es de:', predicciones[0])
    return predicciones[0]

@app.route('/cantidadInventario', methods=['POST'])
def cantidadInventario():
    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Modelos\modeloCantidadInventario.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    item = request.form.get('item')
    strStore = request.form.get('store')
    store_codes = {'walmart': 1, 'pricesmart': 2, 'aliss': 3, 'h&m': 4, 'zara': 5, 'forever': 6, 'ikea': 7, 'adidas': 8, 'nike': 9, 'pandora': 10}
    store = store_codes.get(unidecode(store).lower(), 0)

    if(store==0):
        print('Tienda no registrada')
        return 'Tienda no registrada'

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        "store": [store],
        "item": [item],
        "month": [request.form.get('month')],
        "year": [request.form.get('year')],
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('La cantidad de inventario para el item {}, en la empresa {}, es de:'.format(item, strStore), predicciones[0])
    return predicciones[0]

@app.route('/tarifaTaxi', methods=['POST'])
def tarifaTaxi():
    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Modelos\modeloTarifaTaxi.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    paymentMethod = request.form.get('paymentMethod')
    rateCode = request.form.get('rateCode')    

    payment_method = {'tarjeta de credito': 1, 'efectivo': 2, 'viaje gratis': 3, 'disputado': 4, 'desconocido': 5, 'viaje anulado': 6}
    paymentMethod = payment_method.get(unidecode(paymentMethod).lower(), 0)

    if(paymentMethod==0):
        print('El método de pago no existe')
        return 'El método de pago no existe'
    
    rate_code = {'estandar': 1, 'aeropuerto': 2, 'connaught place': 3, 'noida': 4, 'tarifa negociada': 5, 'viaje compartido': 6}
    rateCode = rate_code.get(unidecode(rateCode).lower(), 0)

    if(rateCode==0):
        print('El código de tarifa para el viaje no existe')
        return 'El código de tarifa para el viaje no existe'

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        "driver+AF8-tip": [request.form.get('driver')],
        "mta+AF8-tax": [request.form.get('mtaTax')],
        "distance": [request.form.get('distante')],
        "num+AF8-passengers": [request.form.get('numPassenger')],
        "toll+AF8-amount": [request.form.get('tollAmount')],
        "payment+AF8-method": [paymentMethod],
        "rate+AF8-code": [rateCode],
        "extra+AF8-charges": [request.form.get('extraCharges')],
        "improvement+AF8-charge": [request.form.get('improvementCharge')]
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('La tarifa del viaje es de:', predicciones[0])
    return predicciones[0]

@app.route('/delayViajeAvion', methods=['POST'])
def delayViajeAvion():
    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Modelos\modeloViajeAvion.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    #* WN: Southwest Airlines, XE: ExpressJet Airlines, YV: Mesa Airlines, OH: PSA Airlines, OO: SkyWest Airlines, 
    #* UA: United Airlines, US: US Airways, DL: Delta Air Lines, EV: ExpressJet Airlines, F9: Frontier Airlines, 
    #* FL: AirTran Airways, HA: Hawaiian Airlines, MQ: Envoy Air, NW: Northwest Airlines, 9E: Endeavor Air, 
    #* AA: American Airlines, AQ: Aloha Airlines, AS: Alaska Airlines, B6: JetBlue Airways, CO: Continental Airlines

    uniqueCarrier = request.form.get('uniqueCarrier')

    unique_carrier = {'wn': 1, 'xe': 2, 'yv': 3, 'oh': 4, 'oo': 5, 'ua': 6, 'us': 7, 'dl': 8, 'ev': 9, 'f9': 10, 'fl': 11, 
                 'ha': 12, 'mq': 13, 'nw': 14, '9e': 15, 'aa': 16, 'aq': 17, 'as': 18, 'b6': 19, 'co': 20}
    uniqueCarrier = unique_carrier.get(uniqueCarrier.lower(), 0)

    if(uniqueCarrier==0):
        print('Ese código de identificación de aerolínea no existe')
        return 'Ese código de identificación de aerolínea no existe'

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        "DepTime": [request.form.get('depTime')],
        "CRSDepTime": [request.form.get('crsDepTime')],
        "ArrTime": [request.form.get('arrTime')],
        "CRSArrTime": [request.form.get('crsArrTime')],
        "UniqueCarrier": [uniqueCarrier],
        "ActualElapsedTime": [request.form.get('actualElapsedTime')],
        "CRSElapsedTime": [request.form.get('crsElapsedTime')],
        "AirTime": [request.form.get('airTime')],
        "ArrDelay": [request.form.get('arrDelay')],
        "DepDelay": [request.form.get('depDelay')],
        "Distance": [request.form.get('distance')],
        "CarrierDelay": [request.form.get('carrierDelay')],
        "WeatherDelay": [request.form.get('weatherDelay')],
        "NASDelay": [request.form.get('nasDelay')],
        "SecurityDelay": [request.form.get('securityDelay')]
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('El retraso del vuelo es de:', round(predicciones[0]*60, 3))
    return round(predicciones[0]*60, 3)

@app.route('/precioAguacate', methods=['POST'])
def precioAguacate():
    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Proyecto 1\Modelos\modeloPrecioAguacate.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    request.form.get('region')

    all_regions = {'albany': 1, 'atlanta': 2, 'baltimore washington': 3, 'boise': 4, 'boston': 5, 'buffaloro chester': 6,
                        'california': 7, 'charlotte': 8, 'chicago': 9, 'cincinnati dayton': 10, 'columbus': 11, 'dallas fort worth': 12, 
                        'denver': 13, 'detroit': 14, 'grand rapids': 15, 'great lakes': 16, 'harrisburg scranton': 17, 'hartford springfield': 18, 
                        'houston': 19, 'indianapolis': 20, 'jackson ville': 21, 'las vegas': 22, 'los angeles': 23, 'louis ville': 24, 
                        'miami fort lauderdale': 25, 'mid south': 26, 'nash ville': 27, 'new orleans mobile': 28, 'new york': 29, 'north east': 30, 
                        'northernnewengland': 31, 'orlando': 32, 'philadelphia': 33, 'phoenixtucson': 34, 'pittsburgh': 35, 'plains': 36, 
                        'portland': 37, 'raleigh greensboro': 38, 'richmond norfolk': 39, 'roanoke': 40, 'sacramento': 41, 'san diego': 42, 
                        'san francisco': 43, 'seattle': 44, 'south carolina': 45, 'south central': 46, 'south east': 47, 'spokane': 48, 'stlouis': 49, 
                        'syracuse': 50, 'tampa': 51, 'totalus': 52, 'west': 53, 'westtexnewmexico': 54}
    
    region = all_regions.get(region.lower(), 0)

    if(region==0):
        print('Región no existente')
        return 'Región no existente'

    # Crear un nuevo DataFrame
    test_data = pd.DataFrame({
        'Total Volume': [request.form.get('totalVolume')],
        '4046': [request.form.get('d4046')],
        '4225': [request.form.get('d4225')],
        '4770': [request.form.get('d4770')],
        'Total Bags': [request.form.get('totalBags')],
        'Small Bags': [request.form.get('smallBags')],
        'Large Bags': [request.form.get('largeBags')],
        'XLarge Bags': [request.form.get('xLargeBags')],
        'type': [request.form.get('dtype')],
        'year': [request.form.get('year')],
        'region': [region]
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('El precio del aguacate es de:', predicciones[0])
    return predicciones

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# print('----------------------------------')
# precioBitcoin('2017-08-08')
# print('----------------------------------')
# precioAutomovil(2, 9.85, 6900, "Gasolina", "Particular", "Manual", 1)
# print('----------------------------------')
# recomendarPelicula("Tom and Huck", 5)
# print('----------------------------------')
# clienteCompañiaCelular('Male', 0, 'No', 'No', 56, 'Yes', 'Yes', 'Fiber optic', 'Yes', 'Yes', 'Yes', 
#                        'Yes', 'Yes', 'Yes', 'Two year', 'Yes', 'Credit card (automatic)', 110.50, 6045.90)
# print('----------------------------------')
# masaCorporal(1.0, 3, 50.0, 100.0, 20.0, 50.0, 40.0, 30.0, 20.0, 15.0, 10.0, 15.0, 10.0, 8.0)
# print('----------------------------------')
# calidadVino(8.9, 0.3, 0.38, 2.8, 0.10, 31, 69, 0.998, 3.25, 0.86, 12.8, 1, 0)
# print('----------------------------------')
# cantidadInventario('Aliss', 3, 5, 2024)
# print('----------------------------------')
# tarifaTaxi(1.0, 0.5, 3.2, 2, 0.0, 'Tarjeta de crédito', 'estándar', 0.5, 0.3)
# print('----------------------------------')
# delayViajeAvion(1853.0, 520, 1439.0, 1004, 'UA', 172.0, 84.0, 235.0, 48.0, 22.0, 1230, 22.0, 0, 2.0, 11.0)
# print('----------------------------------')
# precioAguacate(10, 17074.83, 1527.63, 71976.41, 75.78, 8940.04, 97.49, 0.0, 2, 2024, 'San Diego')