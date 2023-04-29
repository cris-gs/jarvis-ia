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
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloPrecioBitcoin.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Cargar los datos de entrenamiento
    data = pd.read_csv(
        r'D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Data\bitcoin_price_Training - bitcoin_price.2013Apr-2017Aug.csv.csv')
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
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloPrecioAutomovil.pkl', 'rb') as archivo:
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
        'Owner': [owner],
    })

    # Realizar la predicción con el modelo y los parámetros
    predicciones = modelo.predict(test_data)

    # Imprimir las predicciones
    print('El precio de venta del automóvil es de:', str(round(predicciones[0][0], 3)), 'dolares')
    return ('El precio de venta del automóvil es de:', str(round(predicciones[0][0], 3)), 'dolares')

# /recomendarPelicula/Tom and Huck/5
def recomendarPelicula(title, num_recommendations):

    movies = pd.read_csv(
        'D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Data\movies.csv')
    ratings = pd.read_csv(
        r'D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Data\ratings.csv')
    data = pd.merge(movies, ratings, on='movieId')

    # Seleccionar las columnas necesarias del dataframe
    ratings_matrix = pd.pivot_table(
        data, values='rating', index='userId', columns='title').fillna(0)
    
    list_movies = movies["title"].tolist()
    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloRecomendarPelicula.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Busca el titulo en la lista de películas
    peliculaExistente = False
    for movie in list_movies:
        if title.lower() in movie.lower():
            title = movie
            peliculaExistente = True
            break

    # Verificar si el título de la película se encuentra en ratings_matrix
    if (peliculaExistente == False):
        print(
            "La película '{}' no se encuentra en la matriz de valoraciones.".format(title))
        return "La película '{}' no se encuentra en la matriz de valoraciones.".format(title)

    # Obtener el índice de la película a partir del título
    title = re.escape(title)
    idx = movies.loc[movies['title'].str.contains(title)].index[0]

    try:
        num_recommendations = int(num_recommendations)
    except:
        return 'Lo siento, no se pudo realizar la recomendación debido a que se ingresó un dato incorrecto'
    
    # Obtener las películas similares utilizando el modelo KNN
    distances, indices = modelo.kneighbors(ratings_matrix.iloc[idx, :].values.reshape(
        1, -1), n_neighbors= num_recommendations+1)

    # Crear una lista para almacenar las recomendaciones
    # movie_recommendations = []

    # Recorrer las películas similares y añadir sus títulos a la lista de recomendaciones
    movie_response = ''
    for i in range(1, len(distances.flatten())):
        # movie_recommendations.append(
        #     movies.iloc[indices.flatten()[i]]['title'])
        print('{0}: {1}, con una distancia de {2}'.format(
            i, movies.iloc[indices.flatten()[i]]['title'], distances.flatten()[i]))
        movie_response = movie_response+ ', '+'{0}: {1}, con una distancia de {2}'.format(
            i, movies.iloc[indices.flatten()[i]]['title'], distances.flatten()[i])

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
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloClienteCompañiaCelular.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)
    list_paymentMethod = ["cheque electrónico", "cheque enviado por correo", "transferencia bancaria", "tarjeta de crédito"]
    for method in list_paymentMethod:
        if paymentMethod.lower() in method.lower():
            paymentMethod = method
            break
        else:
            paymentMethod = 'transferencia bancaria'

    list_Contract = ["Month-to-month", "One year", "Two year"]
    if 'mes' in contract.lower():
        contract = list_Contract[0]
    if '1' in contract.lower() or 'uno' in contract.lower():
        contract = list_Contract[1]
    else:
        contract = list_Contract[2]
     
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

    replace_data(test_data, "gender", ["femenino", "masculino"])
    replace_data(test_data, "SeniorCitizen", ["no", "si"])
    replace_data(test_data, "Partner", ["no", "si"])
    replace_data(test_data, "Dependents", ["no", "si"])
    replace_data(test_data, "PhoneService", ["no", "si"])
    replace_data(test_data, "MultipleLines", ["sin servicio telefonico", "no", "si"])
    replace_data(test_data, "InternetService", ["no", "dsl", "fibra optica"])
    replace_data(test_data, "OnlineSecurity", ["sin servicio de internet", "no", "si"])
    replace_data(test_data, "OnlineBackup", ["sin servicio de internet", "no", "si"])
    replace_data(test_data, "DeviceProtection", ["sin servicio de internet", "no", "si"])
    replace_data(test_data, "TechSupport", ["sin servicio de internet", "no", "si"])
    replace_data(test_data, "StreamingTV", ["sin servicio de internet", "no", "si"])
    replace_data(test_data, "StreamingMovies", ["sin servicio de internet", "no", "si"])
    test_data["Contract"].replace(
        {"Month-to-month": 0, "One year": 1, "Two year": 2}, inplace=True)
    replace_data(test_data, "PaperlessBilling", ["no", "si"])
    test_data["PaymentMethod"].replace({"cheque electrónico": 0, "cheque enviado por correo": 1,
                                    "transferencia bancaria": 2, "tarjeta de crédito": 3}, inplace=True)
    
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
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloMasaCorporal.pkl', 'rb') as archivo:
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
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloCalidadVino.pkl', 'rb') as archivo:
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
    print('La calidad del vino es de:', predicciones[0])
    return ('La calidad del vino es de:', str(predicciones[0]))

#/cantidadInventario/Aliss/3/5/2024
def cantidadInventario(store, item, month, year):
    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloCantidadInventario.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)
    strStore = store
    store_codes = {'walmart': 1, 'pricesmart': 2, 'aliss': 3, 'h&m': 4,
                   'zara': 5, 'maxi palí': 6, 'ikea': 7, 'adidas': 8, 'nike': 9, 'pandora': 10}
    store = store_codes.get(unidecode(store).lower(), 0)

    if (store == 0):
        print('Lo siento, no se pudo realizar la predicción debido a que se ingresó una tienda no registrada')
        return 'Lo siento, no se pudo realizar la predicción debido a que se ingresó una tienda no registrada'

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
    print('La cantidad de inventario para el item {}, en la empresa {}, es de: {}'.format(item, strStore, round(predicciones[0], 3)))
    return str('La cantidad de inventario para el item {}, en la empresa {}, es de: {}'.format(item, strStore, round(predicciones[0], 3)))

#/tarifaTaxi/1.0/0.5/3.2/2/0.0/Tarjeta de crédito/estándar/0.5/0.3
def tarifaTaxi(driver, mtaTax, distante, numPassenger, tollAmount, paymentMethod, rateCode, extraCharges, improvementCharge):
    # Cargar el modelo guardado con pickle
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloTarifaTaxi.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)
    
    payment_method1 = {'tarjeta de crédito': 1, 'efectivo': 2, 'viaje gratis': 3, 'disputado': 4, 'desconocido': 5, 'viaje anulado': 6}
    print(payment_method1.get(paymentMethod.lower()))
    paymentMethod = payment_method1.get(paymentMethod.lower(), 0)

    if (paymentMethod == 0):
        print('Lo siento, no se pudo realizar la predicción debido a que se ingresó un método de pago no existente')
        return 'Lo siento, no se pudo realizar la predicción debido a que se ingresó un método de pago no existente'

    rate_code = {'estándar': 1, 'aeropuerto': 2, 'lugar de connaught': 3,
                 'noida': 4, 'tarifa negociada': 5, 'viaje compartido': 6}
    rateCode = rate_code.get(rateCode.lower(), 0)

    if (rateCode == 0):
        print('Lo siento, no se pudo realizar la predicción debido a que se ingresó un código de tarifa para el viaje no existente')
        return 'Lo siento, no se pudo realizar la predicción debido a que se ingresó un código de tarifa para el viaje no existente'

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
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloViajeAvion.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

    # * WN: Southwest Airlines, XE: ExpressJet Airlines, YV: Mesa Airlines, OH: PSA Airlines, OO: SkyWest Airlines,
    # * UA: United Airlines, US: US Airways, DL: Delta Air Lines, EV: ExpressJet Airlines, F9: Frontier Airlines,
    # * FL: AirTran Airways, HA: Hawaiian Airlines, MQ: Envoy Air, NW: Northwest Airlines, 9E: Endeavor Air,
    # * AA: American Airlines, AQ: Aloha Airlines, AS: Alaska Airlines, B6: JetBlue Airways, CO: Continental Airlines

    unique_carrier = {'wn': 1, 'xe': 2, 'yv': 3, 'oh': 4, 'oo': 5, 'ua': 6, 'us': 7, 'dl': 8, 'ev': 9, 'f9': 10, 'fl': 11,
                      'ha': 12, 'mq': 13, 'nw': 14, '9e': 15, 'aa': 16, 'aq': 17, 'as': 18, 'b6': 19, 'co': 20}
    uniqueCarrier = unique_carrier.get(uniqueCarrier.lower(), 0)

    if (uniqueCarrier == 0):
        print('Lo siento, no se pudo realizar la predicción debido a que se ingresó un código de identificación de aerolínea no existente')
        return 'Lo siento, no se pudo realizar la predicción debido a que se ingresó un código de identificación de aerolínea no existente'

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
    with open('D:\crist\TEC\Semestre 7\INTELIGENCIA ARTIFICIAL\Modelos\modeloPrecioAguacate.pkl', 'rb') as archivo:
        modelo = pickle.load(archivo)

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

    if (region == 0):
        print('Región no existente')
        return 'Región no existente'

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
    print('El precio del aguacate es de:', predicciones[0])
    return str(predicciones[0])


# print('----------------------------------')
# precioBitcoin('2023-04-21')
# print('----------------------------------')
# precioAutomovil(2, 9.85, 6900, "Gasolina", "Particular", "Manual", 1)
# print('----------------------------------')
#recomendarPelicula("casino", 5)
# print('----------------------------------')
# clienteCompañiaCelular('masculino', 'no', 'no', 'no', 56, 'si', 'si', 'fibra optica', 'si', 'si', 'si', 'si', 'si', 'si', '2 años', 'si', 'tarjeta de credito', 110.50, 6045.90)
# print('----------------------------------')
# masaCorporal(1.0, 3, 50.0, 100.0, 20.0, 50.0, 40.0, 30.0, 20.0, 15.0, 10.0, 15.0, 10.0, 8.0)
# print('----------------------------------')
# calidadVino(8.9, 0.3, 0.38, 2.8, 0.10, 31, 69, 0.998, 3.25, 0.86, 12.8, 1, 0)
# print('----------------------------------')
# cantidadInventario('walmart', 3, 5, 2024)
# print('----------------------------------')
# tarifaTaxi(1.0, 0.5, 3.2, 2, 0.0, 'tarjeta de crédito', 'estándar', 0.5, 0.3)
# print('----------------------------------')
# delayViajeAvion(1853.0, 520, 1439.0, 1004, 'UA', 172.0, 84.0, 235.0, 48.0, 22.0, 1230, 22.0, 0, 2.0, 11.0)
# print('----------------------------------')
precioAguacate(10, 17074.83, 1527.63, 71976.41, 75.78, 8940.04, 97.49, 0.0, 2, 2024, 'San Diego')