import json
from requests import Response
import requests
import cerberus
from jsonschema import validate

'''Methods for checking the responses of our requests'''


class Checking:
    '''Checking status code'''

    @staticmethod
    def dog_status_code_assert(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Successful status code: " + str({response.status_code}))
        else:
            print(f"Wrong status code: " + str({response.status_code}))

    '''Method for checking presence of required fields in response to request'''

    @staticmethod
    def dog_field_assert(response: Response, expected_field):
        field = json.loads(response.text)
        assert list(field) == expected_field
        print("All field present")

    '''Method for checking value of required fields in response to request '''

    @staticmethod
    def dog_value_field_assert(response: Response, field_name, expected_value):
        check = response.json()
        check_field_value = check.get(field_name)
        assert check_field_value == expected_value
        print(expected_value + ' TRUE !!!')

    @staticmethod
    def dog_images_cerberus(response: Response):
        schema = {
            'message': {"type": "list"},
            'status': {"type": "string"}
        }

        v = cerberus.Validator()
        assert v.validate(response.json(), schema)

    @staticmethod
    def test_dog_random_json_schema(response: Response):
        """проверка структуры ответа на запрос"""
        respons = response.json()
        schema = {
            "type": "object",
            "properties": {
                'message': {"type": "array"},
                'status': {"type": "string"}
            },
            "required": ["message", "status"]
        }

        validate(instance=response.json(), schema=schema)

        assert respons["status"] == "success"
