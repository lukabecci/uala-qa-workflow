from commons_qa.api.api_client import ApiClient

class TestApiUser:
    api_client = ApiClient('https://asesvuhm88.execute-api.us-east-1.amazonaws.com/')

    def test_verify_username(self):
        response = self.api_client.get("contacts/MATI_ID")
        print(response.json())
        print(response.status_code)
        print(response)
        assert response.status_code == 200