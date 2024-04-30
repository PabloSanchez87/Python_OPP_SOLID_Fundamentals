"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""
## TESTING - PRUEBAS UNITARIAS
import unittest # importamos unittest
from datetime import datetime, date # para importar la fecha

def sum (a,b):
    if not isinstance(a, (int, float)) or not isinstance(b,(int,float)):
         raise ValueError("Los argumentos deben ser enteros o decimales")   
    return a + b

class TestSum(unittest.TestCase):       # debemos crear una clase y extender la clase unittest
    # Casos positivos.                  
    def test_sum(self):                 # debe empezar siempre por test para que la liberia lo busque
        self.assertEqual(sum(5,7),12)
        self.assertEqual(sum(5,-7),-2)
        self.assertEqual(sum(0,0),0)
        self.assertEqual(sum(2.5,2.1),4.6)
        self.assertEqual(sum(2.5,2.5),5)
        
    # Control de errores.
    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5",7)
        with self.assertRaises(ValueError):
            sum("5","7")
        with self.assertRaises(ValueError):
            sum(5,"7")
        with self.assertRaises(ValueError):
            sum("a",7)
        with self.assertRaises(ValueError):
            sum(None,7)

# unittest.main() 

### EXTRA ###
data ={
    "name": "Pablo Sanchez",
    "age": 36,
    "birth_date": datetime.strptime("01-12-87", "%d-%m-%y").date(),  # Trabajamos con formato fechas
    "programming_languages": ["Python", "C++", "Java"]
}

# Clase para los test.
class TestData(unittest.TestCase):
    # Muchas librerias de testing podemos preparar el contexto para meter los datos con los que va a trabajar el propio test.
    def setUp(self) -> None:  ## Aunque generalmente trabajaremos con los propios datos de la aplicación y no con unos dummie como estamos haciendo.
        self.data ={
            "name": "Pablo Sanchez",
            "age": 36,
            "birth_date": datetime.strptime("01-12-87", "%d-%m-%y").date(),  
            "programming_languages": ["Python", "C++", "Java"]
        }
    
    # Test 
    def test_fields_exist(self):  #testeamos si existen todos los campos
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    # Test
    def test_data_is_correct(self): # poner nombres de los test muy explicitos.
        self.assertEqual(self.data["name"], "Pablo Sanchez") # sólo valdría así sabiendo a ciencia cierta que los datos a comprobar son estos.
        
        # Comprobamos los types de datos.
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)

unittest.main()



    