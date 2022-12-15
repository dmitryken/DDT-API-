from openBrewery.utils.api_brewery import Brewery
from openBrewery.utils.assertions_bre import Assert
from requests import Response

import pytest


@pytest.mark.brew_test
class TestDogPage:
    def test_single_brewery(self):
        get_result: Response = Brewery.single_brewery()
        get_result_js = get_result.json()
        Assert.assert_status_code(get_result, 200)
        Assert.assert_expected_field(get_result, ["id", "name", "brewery_type", "street", "address_2", "address_3",
                                              "city", "state", "county_province", "postal_code", "country",
                                              "longitude", "latitude", "phone", "website_url", "updated_at",
                                              "created_at"])
        Assert.assert_value_field(get_result_js, "id", "madtree-brewing-cincinnati")
        Assert.assert_value_field(get_result_js, "name", "MadTree Brewing")
        Assert.assert_value_field(get_result_js, "brewery_type", "regional")
        Assert.assert_value_field(get_result_js, "street", "3301 Madison Rd")
        Assert.assert_value_field(get_result_js, "city", "Cincinnati")
        Assert.assert_value_field(get_result_js, "state", "Ohio")
        Assert.assert_value_field(get_result_js, "postal_code", "45209-1132")
        Assert.assert_value_field(get_result_js, "country", "United States")
        Assert.assert_value_field(get_result_js, "longitude", "-84.4239715")
        Assert.assert_value_field(get_result_js, "latitude", "39.1563725")
        Assert.assert_value_field(get_result_js, "phone", "5138368733")
        Assert.assert_value_field(get_result_js, "website_url", "http://www.madtreebrewing.com")
        Assert.assert_value_field(get_result_js, "updated_at", "2022-10-30T06:11:39.514Z")
        Assert.assert_value_field(get_result_js, "created_at", "2022-10-30T06:11:39.514Z")

    def test_lest_breweries(self):
        get_result: Response = Brewery.list_breweries()
        one_object_resp = get_result.json()[0]
        Assert.assert_status_code(get_result, 200)
        Assert.assert_list_breweries_cerberus(get_result)
        Assert.range_array_3_page(get_result)
        Assert.assert_value_field(one_object_resp, "id", "10-56-brewing-company-knox")
        Assert.assert_value_field(one_object_resp, "name", "10-56 Brewing Company")
        Assert.assert_value_field(one_object_resp, "brewery_type", "micro")
        Assert.assert_value_field(one_object_resp, "street", "400 Brown Cir")
        Assert.assert_value_field(one_object_resp, "city", "Knox")
        Assert.assert_value_field(one_object_resp, "state", "Indiana")
        Assert.assert_value_field(one_object_resp, "postal_code", "46534")
        Assert.assert_value_field(one_object_resp, "country", "United States")
        Assert.assert_value_field(one_object_resp, "longitude", "-86.627954")
        Assert.assert_value_field(one_object_resp, "latitude", "41.289715")
        Assert.assert_value_field(one_object_resp, "phone", "6308165790")
        Assert.assert_value_field(one_object_resp, "updated_at", "2022-10-30T06:11:39.514Z")
        Assert.assert_value_field(one_object_resp, "created_at", "2022-10-30T06:11:39.514Z")

    def test_by_city(self):
        get_result: Response = Brewery.filter_breweries_by_city()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_by_city(get_result)

    def test_by_dict(self):
        get_result: Response = Brewery.sort_breweries_by_dist()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_by_dict(get_result)

    def test_by_name(self):
        get_result: Response = Brewery.filter_breweries_by_name()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_by_name(get_result)

    def test_by_state(self):
        get_result: Response = Brewery.filter_breweries_by_state()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_by_state(get_result)

    def test_by_postal(self):
        get_result: Response = Brewery.filter_breweries_by_postal()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_by_postal(get_result)

    def test_by_type(self):
        get_result: Response = Brewery.filter_breweries_by_type()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_by_type(get_result)

    def test_page(self):
        get_result: Response = Brewery.breweries_page()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_page(get_result)
        Assert.range_array_3_page(get_result)

    def test_per_page(self):
        get_result: Response = Brewery.breweries_per_page()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_per_page(get_result)

    def test_sort(self):
        get_result: Response = Brewery.sort_result()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_sort(get_result)
        Assert.range_array_3_page(get_result)

    def test_random_brewery(self):
        get_result: Response = Brewery.random_brewery()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_random_brewery(get_result)

    def test_size(self, base_url_2):
        get_result: Response = Brewery.size_brewery(base_url_2)
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_size(get_result)

    def test_search(self):
        get_result: Response = Brewery.search_breweries()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_search(get_result)
        Assert.range_array_3_page(get_result)

    def test_autocomplete(self):
        get_result: Response = Brewery.autocomplete_brewery()
        Assert.assert_status_code(get_result, 200)
        Assert.json_schema_autocomplete(get_result)
