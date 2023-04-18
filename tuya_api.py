import logging
from tuya_resources.tuya_iot import (TuyaOpenAPI,AuthType,TUYA_LOGGER)
TUYA_LOGGER.setLevel(logging.DEBUG)

#conecta a una cuenta de Tuya Cloud
#----------------------------------#
#Recibe una api key, un api secret, un username, y un password,
#opcionalmente puede recibir un endpoint para cambiar de región,
#por defecto es "https://openapi-ueaz.tuyaus.com" para United States West
# y retorna el objeto openapi,con el que posteriormente
#se utilizan los métodos de POST y GET
#dentro de las funciones read_relay() y write_relay()
def connect_to_cloud(
        ACCESS_ID,ACCESS_KEY,USERNAME,PASSWORD,
        ENDPOINT = "https://openapi-ueaz.tuyaus.com"):
    openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY, AuthType.CUSTOM)
    openapi.connect(USERNAME, PASSWORD)
    return openapi


#Lee el estado de un relay WI-FI
#------------------------------#
#Recibe un objeto openapi, correspondiente a la sesión de TuyaCloud y
#recibe también el ID correspondiente al relay wi-fi.
#Retorna el status del parámetro switch_1 del relay wi-fi
#correspondiente al restado del contacto del relay
def read_relay(openapi_obj,relay_id):
    status = openapi_obj.get('/v1.0/iot-03/devices/{}/status'.format(relay_id))
    relay_status = status["result"][0]["value"]
    return relay_status


#enciende o apaga el relay
#------------------------#
#Recibe un objeto openapi, correspondiente a la sesión de TuyaCloud,
#un id correspondiente a un relay wi-fi, y el valor a escribir en el relay
#True para encender, False para apagar.
#No retorna nada
def write_relay(openapi_obj,relay_id,value):
    commands = {'commands': [{'code': 'switch_1', 'value': value}]}
    openapi_obj.post('/v1.0/iot-03/devices/{}/commands'.format(relay_id), commands)

