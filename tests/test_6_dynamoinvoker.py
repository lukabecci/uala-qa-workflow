from commons_qa.api.api_client import ApiClient
from commons_qa.invokers.dynamo_invoker import DynamoInvoker
import random

class TestApiUser:
    api_client = ApiClient('https://2p5mwal37l.execute-api.us-east-1.amazonaws.com/v1/contacts')
    random = str(random.randrange(99999999))

    def test_dynamo(self):
        body = {
            "id": "aiagAmrin212",
            "firstname": "santi",
            "lastname": "amorin"
        }
        self.api_client.post(payload=body)
        dynamo_invoker = DynamoInvoker("playground")
        resultado = dynamo_invoker.get_list_by_query(table_name="ContactsLucaBecci",
                                                     key_condition_expression="id = :id",
                                                     expression_attributes_values={':id': {"S": "aiagAmrin212"}})
        assert resultado["Items"]