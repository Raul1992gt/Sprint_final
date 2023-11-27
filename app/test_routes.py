# test_routes.py
import json
import unittest
from app.models import Data
from app import create_app, db

class TestDataRoutes(unittest.TestCase):
    def setUp(self):
        # Creamos app de pruebas y su configuración
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        # Limpiamos la base de datos después de las pruebas
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_insert_data(self):
        # Probamos la ruta insert_data
        data = {"name": "Test User"}
        response = self.client.post("/data", json=data)
        self.assertEqual(response.status_code, 200)

        # Verificamos que los datos se insertaron en la base de datos
        inserted_data = json.loads(response.data)
        self.assertEqual(inserted_data["message"], "Data inserted successfully")

    def test_get_all_data(self):
        # Probamos la ruta get_all_data
        response = self.client.get("/data")
        self.assertEqual(response.status_code, 200)

        # Verificamos que la respuesta contiene los datos esperados
        data_list = json.loads(response.data)
        self.assertIsInstance(data_list, list)

    def test_delete_data(self):
        # Insertamos datos de prueba en la base de datos
        test_data = {"name": "Test User"}
        insert_response = self.client.post("/data", json=test_data)
        self.assertEqual(insert_response.status_code, 200)

        # Verificamos que la respuesta después de la inserción es correcta
        inserted_data = json.loads(insert_response.data)
        self.assertEqual(inserted_data["message"], "Data inserted successfully")

        # Obtenemos el objeto Data de la base de datos
        data = Data.query.filter_by(name=test_data["name"]).first()

        # Aseguramos que 'data' no sea None antes de proceder
        self.assertIsNotNone(data)

        # Obtenemos el id del objeto Data
        data_id = data.id

        # Probamos la ruta delete_data
        delete_response = self.client.delete(f"/data/{data_id}")
        
        # Verificamos que el código de estado sea 200 (OK)
        self.assertEqual(delete_response.status_code, 200)

        # Verificamos que los datos se eliminaron de la base de datos
        delete_data_response = json.loads(delete_response.data)
        self.assertEqual(delete_data_response["message"], "Data deleted successfully")

    def test_update_data(self):
        # Insertamos datos de prueba en la base de datos
        test_data = {"name": "Test User"}
        insert_response = self.client.post("/data", json=test_data)
        self.assertEqual(insert_response.status_code, 200)

        # Verificamos que la respuesta después de la inserción es correcta
        inserted_data = json.loads(insert_response.data)
        self.assertEqual(inserted_data["message"], "Data inserted successfully")

        # Obtenemos el objeto Data de la base de datos
        data = Data.query.filter_by(name=test_data["name"]).first()

        # Aseguramos que 'data' no sea None antes de proceder
        self.assertIsNotNone(data)

        # Obtenemos el id del objeto Data
        data_id = data.id

        # Datos actualizados
        updated_data = {"name": "Updated Test User"}

        # Probamos la ruta update_data
        update_response = self.client.put(f"/data/{data_id}", json=updated_data)
        
        # Verificamos que el código de estado sea 200 (OK)
        self.assertEqual(update_response.status_code, 200)

        # Verificamos que los datos se actualizaron en la base de datos
        update_data_response = json.loads(update_response.data)
        self.assertEqual(update_data_response["message"], "Data updated successfully")

        # Verificamos que los datos actualizados coinciden con lo que esperamos
        updated_data_in_db = db.session.query(Data).get(data_id)
        self.assertEqual(updated_data_in_db.name, updated_data["name"])


if __name__ == "__main__":
    unittest.main()
