from commons_qa.api.api_client import ApiClient

class TestApiUser:
    api_client = ApiClient('https://asesvuhm88.execute-api.us-east-1.amazonaws.com/')

    def test_get_sin_model(self):
        response = self.api_client.get("contacts/MATI_ID")
        response_en_json = response.json()
        assert response_en_json["firstname"]["S"] == "viernes"
        assert(response_en_json.get("id").get("S")) == "MATI_ID"