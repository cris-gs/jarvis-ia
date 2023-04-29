# Menú de opciones
# menu = "Opciones disponibles: \n1 si quiere predecir el precio del bitcoin \n2 si quiere predecir el precio de un automóvil \n3 si quiere que le recomiende películas \n4 si quiere clasificar la calidad de un vino \n5 si quiere predecir la cantidad de inventario de una compañía \n6 si quiere predecir la tarifa de los viajes de taxi \n7 si quiere clasificar si un cliente se va a pasar de compañía celular \n8 si quiere predecir el delay de los viajes de avión \n9 si quiere predecir la masa corporal de un paciente \n10 si quiere predecir el precio de un aguacate. \nPor favor, indique la opción que desea seleccionar diciendo la palabra 'opción' seguida del número correspondiente."
menu = "Opciones disponibles: "

# Selecciona el modelo correspondiente a la opción elegida
def select_model(option):
  if "10" in option:
    return({'id': 10, 'messages': [ "Para predecir el precio de los aguacates, necesitaríamos los siguientes datos:",
                                    "¿Cuál es el número total de aguacates vendidos?", "¿Cuál es el número total de aguacates con PLU 4046 vendidos?", "¿Cuál es el número total de aguacates con PLU 4225 vendidos?",
                                    "¿Cuál es el número total de aguacates con PLU 4770 vendidos?", "¿Cuál es el número total de bolsas de aguacates vendidas, incluyendo todas las tallas y tipos de bolsas?",
                                    "¿Cuál es el número de bolsas pequeñas de aguacates vendidas?", "¿Cuál es el número de bolsas grandes de aguacates vendidas?", "¿Cuál es el número de bolsas extra grandes de aguacates vendidas?",
                                    "¿Qué tipo de aguacate se vendió, convencional o orgánico?", "¿En qué año se realizó la venta de aguacates?", "¿De dónde provienen los aguacates?" ]})
  
  elif "1" in option:
    return({'id': 1, 'messages': ["Para predecir el precio del bitcoin, necesitamos los siguientes datos:", 
                                  "Diga el año", "Diga del mes", "Diga del día"]})
  elif "2" in option:
    return({'id': 2, 'messages': ["Para predecir el precio de un automóvil, necesitamos los siguientes datos:", 
                                  "Diga la edad del automóvil", "Diga el precio actual del automóvil", "Diga la distancia recorrida por el automóvil", "Diga el tipo de combustible que utiliza el automóvil, debe de ser alguna de estas opciones, Diesel, Gasolina, o Gas", 
                                  "Diga el tipo de vendedor, debe de ser alguna de estas opciones, Particular, Concesionario o Propietario", "Diga el tipo de transmisión, debe de ser alguna de estas opciones, Manual o Automática", 
                                  "Diga la cantidad de dueños que ha tenido el automóvil"]})
  elif "3" in option:
    return({'id': 3, 'messages': ["Para recomendar películas, necesitamos los siguientes datos:", 
                                 "Diga el nombre de la película", "Diga la cantidad de recomendaciones que desea"]})
  elif "4" in option:
    return({'id': 4, 'messages': ["Para clasificar la calidad de un vino, necesitamos los siguientes datos:", "¿Cuál es el nivel de acidez fija?",
                                  "¿Cuál es el nivel de acidez volátil?", "¿Cuál es el nivel de ácido cítrico?", "¿Cuál es el nivel de azúcar residual?", "¿Cuál es el nivel de cloruros?",
                                  "¿Cuál es el nivel de dióxido de azufre libre?", "¿Cuál es el nivel de dióxido de azufre total?", "¿Cuál es el nivel de densidad?", "¿Cuál es el nivel de pH?",
                                  "¿Cuál es el nivel de sulfatos?", "¿Cuál es el nivel de alcohol?", '¿El tipo de vino es rojo o blanco?']})
  elif "5" in option:
    return({'id': 5, 'messages': [ "Para predecir la cantidad de inventario de una compañía, necesitamos los siguientes datos:", "¿En qué tienda se vendieron los artículos? Las opciones son: walmart, pricesmart, aliss, h&m, zara, maxi palí, ikea, adidas, nike, pandora.", 
                                  "¿Cuál es el número del artículo vendido en esa tienda?", "¿En qué mes se vendieron los artículos?", "¿En qué año se vendieron los artículos?"]})
  elif "6" in option:
    return({'id': 6, 'messages': ["Para predecir la tarifa de los viajes de taxi, necesitamos los siguientes datos:", "¿Cuánto fue la propina dada al conductor?",  "¿Cuál es la tasa de impuestos aplicada por el servicio?",
                                  "¿Cuál fue la distancia recorrida en el viaje?", "¿Cuántos pasajeros había en la cabina?", "¿Cuánto se pagó en peajes?", "¿Cuál fue el método de pago utilizado? Las opciones son: tarjeta de crédito, efectivo, viaje gratis, disputado, desconocido, viaje anulado.",
                                  "¿Cuál fue el código de tarifa para el viaje? Las opciones son: estándar, aeropuerto, lugar de connaught, noida, tarifa negociada, viaje compartido", "¿Cuántos cargos extras se aplicaron?", "¿Cuánto fue el cargo recaudado para mejorar el servicio?"]})
  
  elif "7" in option:
    return({'id': 7, 'messages':["Para clasificar si un cliente se va a pasar de compañía celular, necesitamos los siguientes datos:",
                                 'Diga el genero del cliente, femenino o masculino', '¿El cliente es mayor de edad?', '¿El cliente tiene pareja?', '¿El cliente tiene dependientes?', '¿Cuál es el número de meses que el cliente ha estado suscrito al servicio?', 
                                  '¿El cliente tiene servicio telefónico?', '¿El cliente tiene varias líneas telefónicas?, en caso de que no tenga ningun servicio, indique sin servicio telefonico', '¿El cliente tiene servicio de internet?', 
                                  '¿Que tipo de servicio de Internet tiene el cliente? las opciones son DSL, Fibra óptica', '¿El cliente tiene seguridad en línea?', '¿El cliente tiene copia de seguridad en línea?', '¿El cliente tiene protección de dispositivos?', 
                                  '¿El cliente tiene soporte técnico?', '¿El cliente tiene servicio de televisión en streaming?', '¿El cliente tiene servicio de películas en streaming?', '¿Qué tipo de contrato que tiene el cliente? las opciones son Mes a mes, Dos años o Un año', 
                                  '¿El cliente tiene facturación sin papel?', 'Indique el método de pago que utiliza el cliente, la opciones son, cheque electrónico, cheque enviado por correo, transferencia bancaria, tarjeta de crédito', 'Cual es el monto mensual que paga el cliente sus servicios de telecomunicaciones', 
                                  '¿Cual es el monto total que el cliente ha pagado hasta la fecha?']})

  elif "8" in option:
    return({ 'id': 8, 'messages': [ "Para predecir el retraso de los viajes de avión, necesitamos los siguientes datos:",
                                    "¿Cuál es la hora de salida real del vuelo?", "¿Cuál es la hora de salida programada del vuelo?", "¿Cuál es la hora de llegada real del vuelo?",
                                    "¿Cuál es la hora de llegada programada del vuelo?", "¿Cuál es el código de dos letras que identifica a la aerolínea?", "¿Cuánto es el tiempo real de vuelo en minutos?",
                                    "¿Cuánto es el tiempo de vuelo programado en minutos?", "¿Cuánto es el tiempo en el aire en minutos?", "¿Cuántos minutos de retraso hay en la llegada?",
                                    "¿Cuántos minutos de retraso hay en la salida?", "¿Cuál es la distancia de vuelo en millas?", "¿Cuántos minutos de retraso son atribuidos a la aerolínea?",
                                    "¿Cuántos minutos de retraso son atribuidos al clima?", "¿Cuántos minutos de retraso son atribuidos al sistema nacional de aviación?",
                                    "¿Cuántos minutos de retraso son atribuidos a la seguridad?"
  ]
} )
  
  elif "9" in option:
    return({'id': 9,'messages': [ "Para predecir la masa corporal de un paciente, necesitamos los siguientes datos:",
                                  "¿Cuál es la densidad corporal del paciente?", "¿Cuál es la edad del paciente en años?", "¿Cuál es el peso del paciente en libras?", "¿Cuál es la altura del paciente en pulgadas?", "¿Cuál es la circunferencia del cuello del paciente en pulgadas?", "¿Cuál es la circunferencia del pecho del paciente en pulgadas?",
                                  "¿Cuál es la circunferencia del abdomen del paciente en pulgadas?", "¿Cuál es la circunferencia de la cadera del paciente en pulgadas?", "¿Cuál es la circunferencia del muslo del paciente en pulgadas?", "¿Cuál es la circunferencia de la rodilla del paciente en pulgadas?",
                                  "¿Cuál es la circunferencia del tobillo del paciente en pulgadas?", "¿Cuál es la circunferencia del bíceps del paciente en pulgadas?", "¿Cuál es la circunferencia del antebrazo del paciente en pulgadas?", "¿Cuál es la circunferencia de la muñeca del paciente en pulgadas?" ]})
  
  else:
    return("Lo siento, no he entendido su respuesta. Por favor, seleccione una opción válida.")