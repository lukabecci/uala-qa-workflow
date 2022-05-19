import json
from commons_qa.invokers.dynamo_invoker import DynamoInvoker
from commons_qa.invokers.lambda_invoker import LambdaInvoker

payload = {"id": "LeoLambda",
            "firstname": "calle falsa 123",
            "lastname": "testuser123987@uala.com.ar"}

class Test_Invokers:
    def test_lambda_invoker(self):
        lambda_invoker = LambdaInvoker('playground')
        response = lambda_invoker.invoke(payload=payload, function_name='ContactsCreationA1LucaBecci', qualifier='$LATEST')
        print(response)
        print(response['Payload'].read().decode())
        assert True