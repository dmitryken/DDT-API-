import pytest

from requests import Response
from jsonplaceApi.utils.assertions import Checking
from jsonplaceApi.utils.api import ApiPlace


@pytest.mark.json_test
class TestPlacePage:
    def test_js_list(self):
        result_get: Response = ApiPlace.js_list()
        Checking.js_status_code_assert(result_get, 200)
        Checking.js_field_assert(result_get, ["message", "status"])
        Checking.js_value_field_assert(result_get, "status", "success")
        print("Successful")

    def test_js_add(self):
        result_get: Response = ApiPlace.js_images()
        Checking.js_status_code_assert(result_get, 200)
        Checking.js_images_cerberus(result_get)
        Checking.js_value_field_assert(result_get, "status", "success")


    def test_js_filter(self, test_params):
        print("\nCheck js_list status code, fields, fields value")
        result_get: Response = ApiPlace.js_random(test_params)
        Checking.js_status_code_assert(result_get, 200)
        Checking.test_js_random_json_schema(result_get)
        Checking.js_value_field_assert(result_get, "status", "success")

    def test_sort(self):
        get_result: Response = ApiPlace.sort_result()
        Checking.assert_status_code(get_result, 200)
        Checking.json_schema_sort(get_result)
        Checking.range_array_1_page(get_result)

    def test_by_name(self):
        get_result: Response = ApiPlace.filter_breweries_by_name()
        Checking.assert_status_code(get_result, 200)
        Checking.json_schema_by_name(get_result)