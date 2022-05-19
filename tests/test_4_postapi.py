from commons_qa.api.api_client import ApiClient

class TestApiUser:
    api_client = ApiClient('https://2p5mwal37l.execute-api.us-east-1.amazonaws.com/v1/contacts')

    def test_post_user(self):
        body = {
            "id": "aiagAmrin212",
            "firstname": "santi",
            "lastname": "amorin"
        }
        response = self.api_client.post(payload=body)
        assert response.status_code in (200,201,202)