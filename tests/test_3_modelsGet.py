from commons_qa.api.api_client import ApiClient
from models.models import UserModel
class TestApiUser:
    api_client = ApiClient('https://asesvuhm88.execute-api.us-east-1.amazonaws.com/')

    def test_get_sin_model(self):
        response = self.api_client.get("contacts/MATI_ID")
        print(response)
        response_en_json = response.json()
        assert response_en_json["Firstname"] == "viernes"
        assert response_en_json["Id"] == "MATI_ID"

    def test_con_models(self):
        response = self.api_client.get("contacts/MATI_ID")
        user_model = UserModel.generate_model(response.json())
        id = user_model.id
        firstname = user_model.firstname
        assert "viernes" == firstname
        assert "MATI_ID" == id