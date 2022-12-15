import json
from requests import Response
import requests
import cerberus
from jsonschema import validate


class Checking:

    @staticmethod
    def json_status_code_assert(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Successful status code: " + str({response.status_code}))
        else:
            print(f"Wrong status code: " + str({response.status_code}))


    @staticmethod
    def json_field_assert(response: Response, expected_field):
        field = json.loads(response.text)
        assert list(field) == expected_field
        print("All field present")


    @staticmethod
    def json_value_field_assert(response: Response, field_name, expected_value):
        check = response.json()
        check_field_value = check.get(field_name)
        assert check_field_value == expected_value
        print(expected_value + ' TRUE !!!')

    @staticmethod
    def json_images_cerberus(response: Response):
        schema = {
            'message': {"type": "list"},
            'status': {"type": "string"}
        }

        v = cerberus.Validator()
        assert v.validate(response.json(), schema)

    @staticmethod
    def test_json_random_json_schema(response: Response):
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
