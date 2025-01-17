import configuration
import data
import requests


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_products_kits(productIds, token):
    header = data.headers.copy()
    header["Authorization"]= "Bearer "+token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                         json=productIds,  # inserta el cuerpo de solicitud
                         headers=header)  # inserta los encabezados