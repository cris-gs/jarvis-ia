# Menú de opciones
menu = "Opciones disponibles: \n1 si quiere predecir el precio del bitcoin \n2 si quiere predecir el precio de un automóvil \n3 si quiere que le recomiende películas \n4 si quiere clasificar la calidad de un vino \n5 si quiere predecir la cantidad de inventario de una compañía \n6 si quiere predecir la tarifa de los viajes de taxi \n7 si quiere clasificar si un cliente se va a pasar de compañía celular \n8 si quiere predecir el delay de los viajes de avión \n9 si quiere predecir la masa corporal de un paciente \n10 si quiere predecir el precio de un aguacate. \nPor favor, indique la opción que desea seleccionar diciendo la palabra 'opción' seguida del número correspondiente."
# menu = "Opciones disponibles: "

# Selecciona el modelo correspondiente a la opción elegida
def select_model(option):
  if "10" in option:
    return({'id': 10, 'messages': [ "Para predecir el precio de los aguacates, necesitaríamos los siguientes datos:",
                                    {"type":"float", "message":"¿Cuál es el número total de aguacates vendidos?"},
                                    {"type":"float", "message":"¿Cuál es el número total de aguacates con PLU 4046 vendidos?"},
                                    {"type":"float", "message":"¿Cuál es el número total de aguacates con PLU 4225 vendidos?"},
                                    {"type":"float", "message":"¿Cuál es el número total de aguacates con PLU 4770 vendidos?"},
                                    {"type":"float", "message":"¿Cuál es el número total de bolsas de aguacates vendidas, incluyendo todas las tallas y tipos de bolsas?"},
                                    {"type":"float", "message":"¿Cuál es el número de bolsas pequeñas de aguacates vendidas?"},
                                    {"type":"float", "message":"¿Cuál es el número de bolsas grandes de aguacates vendidas?"},
                                    {"type":"float", "message":"¿Cuál es el número de bolsas extra grandes de aguacates vendidas?"},
                                    {"type":"str", "options": {"convencional": 0, "orgánico": 1}, "message":"¿Qué tipo de aguacate se vendió, convencional o orgánico?"},
                                    {"type":"int", "message":"¿En qué año se realizó la venta de aguacates?"},
                                    {"type":"str", "options":{'albany': 1, 'atlanta': 2, 'baltimore washington': 3, 'boise': 4, 'boston': 5, 'buffaloro chester': 6,
                                    'california': 7, 'charlotte': 8, 'chicago': 9, 'cincinnati dayton': 10, 'columbus': 11, 'dallas fort worth': 12,
                                    'denver': 13, 'detroit': 14, 'grand rapids': 15, 'great lakes': 16, 'harrisburg scranton': 17, 'hartford springfield': 18,
                                    'houston': 19, 'indianapolis': 20, 'jackson ville': 21, 'las vegas': 22, 'los angeles': 23, 'louis ville': 24,
                                    'miami fort lauderdale': 25, 'mid south': 26, 'nash ville': 27, 'new orleans mobile': 28, 'new york': 29, 'north east': 30,
                                    'northernnewengland': 31, 'orlando': 32, 'philadelphia': 33, 'phoenixtucson': 34, 'pittsburgh': 35, 'plains': 36,
                                    'portland': 37, 'raleigh greensboro': 38, 'richmond norfolk': 39, 'roanoke': 40, 'sacramento': 41, 'san diego': 42,
                                    'san francisco': 43, 'seattle': 44, 'south carolina': 45, 'south central': 46, 'south east': 47, 'spokane': 48, 'stlouis': 49,
                                    'syracuse': 50, 'tampa': 51, 'totalus': 52, 'west': 53, 'westtexnewmexico': 54}
                                    , "message":"¿De dónde provienen los aguacates?"}]})
  
  elif "1" in option:
    return({'id': 1, 'messages': ["Para predecir el precio del bitcoin, necesitamos los siguientes datos:", 
                                  "Diga el año", "Diga del mes", "Diga del día"]})
  elif "2" in option:
    return({'id': 2, 'messages': ["Para predecir el precio de un automóvil, necesitamos los siguientes datos:", 
                                  {"type":"int", "message":"Diga la edad del automóvil"}, 
                                  {"type":"int", "message":"Diga el precio actual del automóvil"}, 
                                  {"type":"int", "message":"Diga la distancia recorrida por el automóvil"}, 
                                  {"type":"str", "options": {"diesel": 0, "gasolina": 1, "gas": 2}, "message":"Diga el tipo de combustible que utiliza el automóvil, debe de ser alguna de estas opciones, Diesel, Gasolina, o Gas"}, 
                                  {"type":"str", "options": {"concesionario": 0, "propietario": 1}, "message":"Diga el tipo de vendedor, debe de ser alguna de estas opciones, Concesionario o Propietario"}, 
                                  {"type":"str", "options": {"manual": 0, "automática": 1}, "message":"Diga el tipo de transmisión, debe de ser alguna de estas opciones, Manual o Automática"}, 
                                  {"type":"int", "message":"Diga la cantidad de dueños que ha tenido el automóvil"}]})
  elif "3" in option:
    return({'id': 3, 'messages': ["Para recomendar películas, necesitamos los siguientes datos:", 
                                 "Diga el nombre de la película", "Diga la cantidad de recomendaciones que desea"]})
  elif "4" in option:
    return({'id': 4, 'messages': ["Para clasificar la calidad de un vino, necesitamos los siguientes datos:", 
                                  {"type":"float", "message":"¿Cuál es el nivel de acidez fija?"},
                                  {"type":"float", "message":"¿Cuál es el nivel de acidez volátil?"},
                                  {"type":"float", "message":"¿Cuál es el nivel de ácido cítrico?"},
                                  {"type":"float", "message":"¿Cuál es el nivel de azúcar residual?"},
                                  {"type":"float", "message":"¿Cuál es el nivel de cloruros?"},
                                  {"type":"float", "message":"¿Cuál es el nivel de dióxido de azufre libre?"},
                                  {"type":"float", "message":"¿Cuál es el nivel de dióxido de azufre total?"},
                                  {"type":"float", "message":"¿Cuál es el nivel de densidad?"},
                                  {"type":"float", "message":"¿Cuál es el nivel de pH?"},
                                  {"type":"float", "message":"¿Cuál es el nivel de sulfatos?"},
                                  {"type":"float", "message":"¿Cuál es el nivel de alcohol?"},
                                  {"type":"str", "options": {"rojo": 0, "blanco": 1}, "message":"¿El tipo de vino es rojo o blanco?"}]})
  elif "5" in option:
    return({'id': 5, 'messages': [ "Para predecir la cantidad de inventario de una compañía, necesitamos los siguientes datos:", 
                                  {"type":"str", "options":{'walmart': 1, 'pricesmart': 2, 'aliss': 3, 'h&m': 4,
                                  'zara': 5, 'maxi palí': 6, 'ikea': 7, 'adidas': 8, 'nike': 9, 'pandora': 10}, 
                                  "message":"¿En qué tienda se vendieron los artículos? Las opciones son: walmart, pricesmart, aliss, h&m, zara, maxi palí, ikea, adidas, nike, pandora."}, 
                                  {"type":"int", "message":"¿Cuál es el número del artículo vendido en esa tienda?"}, 
                                  {"type":"int", "message":"¿En qué mes se vendieron los artículos?"}, 
                                  {"type":"int", "message":"¿En qué año se vendieron los artículos?"}]})

                                #1.0/0.5/3.2/2/0.0/Tarjeta de crédito/estándar/0.5/0.3
  elif "6" in option:
    return({'id': 6, 'messages': ["Para predecir la tarifa de los viajes de taxi, necesitamos los siguientes datos:", 
                                  {"type":"float", "message":"¿Cuánto fue la propina dada al conductor?"},
                                  {"type":"float", "message":"¿Cuál es la tasa de impuestos aplicada por el servicio?"},
                                  {"type":"float", "message":"¿Cuál fue la distancia recorrida en el viaje?"},
                                  {"type":"float", "message":"¿Cuántos pasajeros había en la cabina?"},
                                  {"type":"float", "message":"¿Cuánto se pagó en peajes?"},
                                  {"type":"str", "options":{'tarjeta de crédito': 1, 'efectivo': 2, 'viaje gratis': 3, 'disputado': 4, 'desconocido': 5, 'viaje anulado': 6}, 
                                  "message":"¿Cuál fue el método de pago utilizado? Las opciones son: tarjeta de crédito, efectivo, viaje gratis, disputado, desconocido, viaje anulado."},
                                  {"type":"str", "options":{'estándar': 1, 'aeropuerto': 2, 'lugar de connaught': 3, 'noida': 4, 'tarifa negociada': 5, 'viaje compartido': 6}, 
                                  "message":"¿Cuál fue el código de tarifa para el viaje? Las opciones son: estándar, aeropuerto, lugar de connaught, noida, tarifa negociada, viaje compartido"},
                                  {"type":"str", "options":{'sí': 1, 'no': 0}, "message":"¿Se le aplicaron cargos extras?"},
                                  {"type":"float", "message":"¿Cuánto fue el cargo recaudado para mejorar el servicio?"}]})
  
  elif "7" in option:
    return({'id': 7, 'messages':[ "Para clasificar si un cliente se va a pasar de compañía celular, necesitamos los siguientes datos:",
                                  {"type":"str", "options": {"femenino": 0, "masculino": 1}, "message":'Diga el genero del cliente, femenino o masculino'}, 
                                  {"type":"str", "options": {"no": 0, "sí": 1}, "message":'¿El cliente es mayor de edad?'}, 
                                  {"type":"str", "options": {"no": 0, "sí": 1}, "message":'¿El cliente tiene pareja?'}, 
                                  {"type":"str", "options": {"no": 0, "sí": 1}, "message":'¿El cliente tiene dependientes?'}, 
                                  {"type":"int", "message":'¿Cuál es el número de meses que el cliente ha estado suscrito al servicio?'}, 
                                  {"type":"str", "options": {"no": 1, "sí": 2}, "message":'¿El cliente tiene servicio telefónico?'}, 
                                  {"type":"str", "options": {"sin servicio telefonico": 0, "no": 1, "sí": 2}, "message":'¿El cliente tiene varias líneas telefónicas?, en caso de que no tenga ningun servicio, indique sin servicio telefonico'}, 
                                  {"type":"str", "options": {"no": 0, "sí": 1}, "message":'¿El cliente tiene servicio de internet?'}, 
                                  {"type":"str", "options": {"dsl": 0, "fibra óptica": 1}, "message":'¿Qué tipo de servicio de Internet tiene el cliente? las opciones son: DSL, Fibra óptica'}, 
                                  {"type":"str", "options": {"sin servicio de internet": 0, "no": 1, "sí": 2}, "message":'¿El cliente tiene seguridad en línea?'}, 
                                  {"type":"str", "options": {"sin servicio de internet": 0, "no": 1, "sí": 2}, "message":'¿El cliente tiene copia de seguridad en línea?'}, 
                                  {"type":"str", "options": {"sin servicio de internet": 0, "no": 1, "sí": 2}, "message":'¿El cliente tiene protección de dispositivos?'}, 
                                  {"type":"str", "options": {"sin servicio de internet": 0, "no": 1, "sí": 2}, "message":'¿El cliente tiene soporte técnico?'}, 
                                  {"type":"str", "options": {"sin servicio de internet": 0, "no": 1, "sí": 2}, "message":'¿El cliente tiene servicio de televisión en streaming?'}, 
                                  {"type":"str", "options": {"sin servicio de internet": 0, "no": 1, "sí": 2}, "message":'¿El cliente tiene servicio de películas en streaming?'}, 
                                  {"type":"str", "options": {"mes a mes": 0, "2 años": 1, "un año": 2}, "message":'¿Qué tipo de contrato que tiene el cliente? las opciones son Mes a mes, Dos años o Un año'}, 
                                  {"type":"str", "options": {"no": 0, "sí": 1}, "message":'¿El cliente tiene facturación sin papel?'}, 
                                  {"type":"str", "options": {"cheque electrónico": 0, "cheque enviado por correo": 1, "transferencia bancaria": 2, "tarjeta de crédito": 3}, "message":'Indique el método de pago que utiliza el cliente, la opciones son, cheque electrónico, cheque enviado por correo, transferencia bancaria, tarjeta de crédito'}, 
                                  {"type":"float", "message":'¿Cual es el monto mensual que paga el cliente por sus servicios de telecomunicaciones?'}, 
                                  {"type":"float", "message":'¿Cual es el monto total que el cliente ha pagado hasta la fecha?'}]})
                                  
                                  #float/int/float/int/str/float/float/float/float/float/int/float/float/float/float
  elif "8" in option:
    return({ 'id': 8, 'messages': [ "Para predecir el retraso de los viajes de avión, necesitamos los siguientes datos:",
                                    {"type":"float", "message":"¿Cuál es la hora de salida real del vuelo?"},
                                    {"type":"int", "message":"¿Cuál es la hora de salida programada del vuelo?"},
                                    {"type":"float", "message":"¿Cuál es la hora de llegada real del vuelo?"},
                                    {"type":"int", "message":"¿Cuál es la hora de llegada programada del vuelo?"},
                                    {"type":"str", "options":{'wn': 1, 'xe': 2, 'yv': 3, 'oh': 4, 'oo': 5, 'ua': 6, 'us': 7, 'dl': 8, 'ev': 9, 'f9': 10, 'fl': 11,
                                    'ha': 12, 'mq': 13, 'nw': 14, '9e': 15, 'aa': 16, 'aq': 17, 'as': 18, 'b6': 19, 'co': 20},
                                    "message":"¿Cuál es el código de dos letras que identifica a la aerolínea?"},
                                    {"type":"float", "message":"¿Cuánto es el tiempo real de vuelo en minutos?"},
                                    {"type":"float", "message":"¿Cuánto es el tiempo de vuelo programado en minutos?"},
                                    {"type":"float", "message":"¿Cuánto es el tiempo en el aire en minutos?"},
                                    {"type":"float", "message":"¿Cuántos minutos de retraso hay en la llegada?"},
                                    {"type":"float", "message":"¿Cuántos minutos de retraso hay en la salida?"},
                                    {"type":"int", "message":"¿Cuál es la distancia de vuelo en millas?"},
                                    {"type":"float", "message":"¿Cuántos minutos de retraso son atribuidos a la aerolínea?"},
                                    {"type":"float", "message":"¿Cuántos minutos de retraso son atribuidos al clima?"},
                                    {"type":"float", "message":"¿Cuántos minutos de retraso son atribuidos al sistema nacional de aviación?"},
                                    {"type":"float", "message":"¿Cuántos minutos de retraso son atribuidos a la seguridad?"}]})
  
  elif "9" in option:
    return({'id': 9,'messages': [ "Para predecir la masa corporal de un paciente, necesitamos los siguientes datos:",
                                  {"type":"float", "message":"¿Cuál es la densidad corporal del paciente?"},
                                  {"type":"int", "message":"¿Cuál es la edad del paciente en años?"},
                                  {"type":"float", "message":"¿Cuál es el peso del paciente en libras?"},
                                  {"type":"float", "message":"¿Cuál es la altura del paciente en pulgadas?"},
                                  {"type":"float", "message":"¿Cuál es la circunferencia del cuello del paciente en pulgadas?"},
                                  {"type":"float", "message":"¿Cuál es la circunferencia del pecho del paciente en pulgadas?"},
                                  {"type":"float", "message":"¿Cuál es la circunferencia del abdomen del paciente en pulgadas?"},
                                  {"type":"float", "message":"¿Cuál es la circunferencia de la cadera del paciente en pulgadas?"},
                                  {"type":"float", "message":"¿Cuál es la circunferencia del muslo del paciente en pulgadas?"},
                                  {"type":"float", "message":"¿Cuál es la circunferencia de la rodilla del paciente en pulgadas?"},
                                  {"type":"float", "message":"¿Cuál es la circunferencia del tobillo del paciente en pulgadas?"},
                                  {"type":"float", "message":"¿Cuál es la circunferencia del bíceps del paciente en pulgadas?"},
                                  {"type":"float", "message":"¿Cuál es la circunferencia del antebrazo del paciente en pulgadas?"},
                                  {"type":"float", "message":"¿Cuál es la circunferencia de la muñeca del paciente en pulgadas?"}]})
  
  else:
    return("Lo siento, no he entendido su respuesta. Por favor, seleccione una opción válida.")