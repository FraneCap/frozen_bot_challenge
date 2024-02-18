### Ejercicio 1:

# Completar el método is_hot_in_pehuajo con el siguiente objetivo:

# - Consultar la información de clima y devolver True si la temperatura actual
# supera los 28 grados celsius o False caso contrario. Esto implica incluso
# devolver False ante cualquier excepción http.

## Notas:
# Al revisar la documentación de la API, se observa que la temperatura se encuentra en Kelvin, por lo que se hace el cálculo para convertir a Celsius

import requests
import pandas as pd

CELSIUS_TO_KELVIN = 273.15


class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"

    @classmethod
    def is_hot_in_pehuajo(cls):
        try:
            response = requests.get(
                cls.ENDPOINT.format(lat=cls.LAT, lon=cls.LON, API_key=cls.API_KEY)
            )
            response.raise_for_status()
            if not response or response.status_code != 200:
                return False
            data = response.json()
            temp_kelvin = data["main"]["temp"]
            temp_celcius = round(temp_kelvin - CELSIUS_TO_KELVIN, 2)
            print(f'La temperatura es de {temp_celcius}\u00b0')
            return temp_kelvin > 28
        except requests.exceptions.RequestException as e:
            print(e)
            return False


result = GeoAPI.is_hot_in_pehuajo()
print(result)


### Ejercicio 2.1:

# Dadas las variables: product_name y quantity, complete la función
# is_product_available con el siguiente objetivo:

# - Buscar en un pandas DataFrame y devolver True si existe stock, False caso
# contrario.


_PRODUCT_DF = pd.DataFrame(
    {
        "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
        "quantity": [3, 10, 0, 5],
    }
)


def is_product_available(product_name, quantity):
    if product_name in _PRODUCT_DF["product_name"].values and \
        _PRODUCT_DF[_PRODUCT_DF["product_name"] == product_name]["quantity"].values[0] >= quantity:
        return True
    return False

has_stock = is_product_available("Chocolate", 3)
print(f'Hay stock: {has_stock}')


### Ejercicio 2.2:

# Si miramos el diagrama de flujo al momento de la decisión de stock, encontramos un
# potencial loop infinito, ya que el usuario podría continuar ingresando productos
# inválidos o sin stock. Reformule la función para solucionar este problema.

##Notas:
# Al devolver None es cuando el producto no existe, al devolver 0 es que no hay stock.


def is_product_available_current_stock(product_name, quantity):
    if product_name in _PRODUCT_DF["product_name"].values and quantity > 0:
        current_stock = _PRODUCT_DF[_PRODUCT_DF["product_name"] == product_name][
            "quantity"
        ].values[0]
        return current_stock >= quantity, current_stock
    else:
        return False, None
    
has_stock, current_stock = is_product_available_current_stock("Chocolate", 3)
print(f'Hay stock: {has_stock}, Cantidad de stock: {current_stock}')