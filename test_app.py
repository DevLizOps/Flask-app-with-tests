import unittest
from app import app

class TestApp(unittest.TestCase):

 def setUp(self):
     # Configuración de la aplicación antes de cada prueba
     self.app = app.test_client()
     self.app.testing = True

 def test_formulario(self):
     # Verificación de la página del formulario
     response = self.app.get('/')
     self.assertEqual(response.status_code, 200)
     print('La página del formulario se carga correctamente.')

 def test_ruta_invalida(self):
     # Probar una ruta no válida
     response = self.app.get('/ruta_invalida')
     self.assertEqual(response.status_code, 404)
     print('Ante una ruta inválida, la aplicación responde correctamente.')

if __name__ == '__main__':
 unittest.main()

