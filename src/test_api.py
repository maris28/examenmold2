import unittest
from flask import Flask
from app import app
from clases import Empleado

class TestEmpleado(unittest.TestCase):
    def test_calcular_salario_mensual(self):
        empleado = Empleado('John Doe', 30, 60000)
        self.assertEqual(empleado.calcular_salario_mensual(), 5000)

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_formulario(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Calculadora de Salario', response.data)

    def test_calcular(self):
        response = self.app.post('/calcular', data=dict(
            nombre='John Doe',
            edad=30,
            salario_base=60000
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'El salario de John Doe es: $5000.0', response.data)

if __name__ == '__main__':
    unittest.main()
