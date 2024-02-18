# frozen_bot_challenge


En este repositorio, se presenta la implementacion de un hipotetico bot de atención al cliente y se resuelven algunos de sus procedimientos a realizar, planteados en un diagrama de flujo, mediante el codigo de Python.

## Ejercicio 1

### Objetivo:
Completar el método `is_hot_in_pehuajo` con el siguiente objetivo:

- Consultar la información de clima y devolver True si la temperatura actual supera los 28 grados celsius o False caso contrario. Esto implica incluso devolver False ante cualquier excepción http.

### Notas:
- Al revisar la documentación de la API, se observa que la temperatura se encuentra en Kelvin, por lo que se hace el cálculo para convertir a Celsius.

## Ejercicio 2.1

### Objetivo:
Dadas las variables `product_name` y `quantity`, completar la función `is_product_available` con el siguiente objetivo:

- Buscar en un pandas DataFrame y devolver True si existe stock, False en caso contrario.

### Notas:
- El DataFrame `_PRODUCT_DF` contiene información sobre los productos y su cantidad en stock.

## Ejercicio 2.2

### Objetivo:
Reformular la función `is_product_available_current_stock` para solucionar un potencial bucle infinito al momento de verificar el stock de un producto.

### Notas:
- Al devolver None es cuando el producto no existe, al devolver 0 es que no hay stock.

---