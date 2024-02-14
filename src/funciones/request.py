import requests

def data(url):
    try:
        response = requests.get(url)
        datos = response.json()['IdHospital'][0]['Nombre'][1]['Direccion'][2]# Convierte la respuesta en formato JSON a un diccionario de Python
        return datos
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return None