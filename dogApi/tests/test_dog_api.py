import pytest

from requests import Response
from dogApi.utils.assertions import Checking
from dogApi.utils.api import ApiDog


@pytest.mark.dog_test
class TestDogPage:
    def test_dog_list(self):
        print("\nCheck dog_list status code, fields, fields value")

    result_get: Response = ApiDog.dog_list()
    Checking.dog_status_code_assert(result_get, 200)
    Checking.dog_field_assert(result_get, ["message", "status"])
    Checking.dog_value_field_assert(result_get, "status", "success")
    print("Successful")

    def test_dog_images(self):
        print("\nCheck dog_list status code, fields, fields value")

    result_get: Response = ApiDog.dog_images()
    Checking.dog_status_code_assert(result_get, 200)
    Checking.dog_images_cerberus(result_get)
    Checking.dog_value_field_assert(result_get, "status", "success")


@pytest.mark.param_tests
@pytest.mark.parametrize("test_params", ["1", "2", "3"], ids=["1 dog", "2 dog", "3 dog"])
def test_dog_random(test_params):
    print("\nCheck dog_list status code, fields, fields value")
    result_get: Response = ApiDog.dog_random(test_params)
    Checking.dog_status_code_assert(result_get, 200)
    Checking.test_dog_random_json_schema(result_get)
    Checking.dog_value_field_assert(result_get, "status", "success")
