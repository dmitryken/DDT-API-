import json
from requests import Response
import requests
import cerberus
from jsonschema import validate


class Assert:
    '''Checking status code'''

    @staticmethod
    def assert_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Successful status code: " + str({response.status_code}))
        else:
            print(f"Wrong status code: " + str({response.status_code}))

    '''Method for checking presence of required fields in response to request'''

    @staticmethod
    def assert_expected_field(response: Response, expected_field):
        field = json.loads(response.text)
        assert list(field) == expected_field
        print("All field present")

        '''Method for checking value of required fields in response to request '''

    @staticmethod
    def assert_value_field(response: Response, field_name, expected_value):
        checked_js = response
        checked_field_value = checked_js.get(field_name)
        print("Value field getting")
        assert checked_field_value == expected_value
        print(expected_value + ' The value is correct!!!')

        '''Checked field by using cerberus'''

    @staticmethod
    def assert_list_breweries_cerberus(response: Response):
        resp = response.json()[0]
        print(resp['id'])
        schema = {
            'id': {"type": "string"},
            'name': {"type": "string"},
            'brewery_type': {"type": "string"},
            'street': {"type": "string"},
            'address_2': {"type": "string", 'nullable': True},
            'address_3': {"type": "string", 'nullable': True},
            'city': {"type": "string"},
            'state': {"type": "string"},
            'county_province': {"type": "string", 'nullable': True},
            'postal_code': {"type": "string"},
            'country': {"type": "string"},
            'longitude': {"type": "string"},
            'latitude': {"type": "string"},
            'phone': {"type": "string"},
            'website_url': {"type": "string", 'nullable': True},
            'updated_at': {"type": "string"},
            'created_at': {"type": "string"}
        }
        v = cerberus.Validator()
        assert v.validate(response.json()[0], schema)

    @staticmethod
    def range_array_3_page(response: Response):
        checked = response.json()
        print(len(checked))
        assert len(checked) == 3

    @staticmethod
    def json_schema_by_city(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "string"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "string"},
                'latitude': {"type": "string"},
                'phone': {"type": "string"},
                'website_url': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "10-barrel-brewing-co-san-diego"
        assert resp["name"] == "10 Barrel Brewing Co"
        assert resp["street"] == "1501 E St"
        assert resp["city"] == "San Diego"
        assert resp["state"] == "California"
        assert resp["postal_code"] == "92101-6618"
        assert resp["country"] == "United States"
        assert resp["longitude"] == "-117.129593"
        assert resp["latitude"] == "32.714813"
        assert resp["phone"] == "6195782311"
        assert resp["website_url"] == "http://10barrel.com"
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_by_dict(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "string"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "string"},
                'latitude': {"type": "string"},
                'phone': {"type": "string"},
                'website_url': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "incheonbrewery-jung-gu"
        assert resp["name"] == "인천맥주(incheon_brewery)"
        assert resp["brewery_type"] == "brewpub"
        assert resp["street"] == "41, Sinpo-ro 15beon-gil"
        assert resp["city"] == "Jung-gu"
        assert resp["state"] == "Incheon"
        assert resp["postal_code"] == "22314"
        assert resp["country"] == "South Korea"
        assert resp["longitude"] == "126.6222289"
        assert resp["latitude"] == "37.47157834"
        assert resp["phone"] == "070-7722-0705"
        assert resp["website_url"] == "https://www.instagram.com/incheon_brewery"
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_by_name(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "string"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "string"},
                'latitude': {"type": "string"},
                'phone': {"type": "string"},
                'website_url': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "3cross-fermentation-cooperative-worcester"
        assert resp["name"] == "3cross Fermentation Cooperative"
        assert resp["brewery_type"] == "micro"
        assert resp["street"] == "4 Knowlton Ave"
        assert resp["city"] == "Worcester"
        assert resp["state"] == "Massachusetts"
        assert resp["postal_code"] == "1603"
        assert resp["country"] == "United States"
        assert resp["longitude"] == "-71.83057593"
        assert resp["latitude"] == "42.24364875"
        assert resp["phone"] == "5086158195"
        assert resp["website_url"] == "http://www.3cross.coop"
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_by_state(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "string"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "null"},
                'latitude': {"type": "null"},
                'phone': {"type": "string"},
                'website_url': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "12-gates-brewing-company-williamsville"
        assert resp["name"] == "12 Gates Brewing Company"
        assert resp["brewery_type"] == "brewpub"
        assert resp["street"] == "80 Earhart Dr Ste 20"
        assert resp["city"] == "Williamsville"
        assert resp["state"] == "New York"
        assert resp["postal_code"] == "14221-7804"
        assert resp["country"] == "United States"
        assert resp["longitude"] is None
        assert resp["latitude"] is None
        assert resp["phone"] == "7169066600"
        assert resp["website_url"] == "http://www.12gatesbrewing.com"
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_by_postal(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "string"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "string"},
                'latitude': {"type": "string"},
                'phone': {"type": "string"},
                'website_url': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "bottlehouse-brewery-lakewood"
        assert resp["name"] == "BottleHouse Brewery"
        assert resp["brewery_type"] == "micro"
        assert resp["street"] == "13368 Madison Ave"
        assert resp["city"] == "Lakewood"
        assert resp["state"] == "Ohio"
        assert resp["postal_code"] == "44107-4840"
        assert resp["country"] == "United States"
        assert resp["longitude"] == "-81.78445705"
        assert resp["latitude"] == "41.47721765"
        assert resp["phone"] == "2162142120"
        assert resp["website_url"] == "http://www.thebottlehousebrewingcompany.com"
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_by_type(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "string"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "string"},
                'latitude': {"type": "string"},
                'phone': {"type": "string"},
                'website_url': {"type": "null"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "10-56-brewing-company-knox"
        assert resp["name"] == "10-56 Brewing Company"
        assert resp["brewery_type"] == "micro"
        assert resp["street"] == "400 Brown Cir"
        assert resp["city"] == "Knox"
        assert resp["state"] == "Indiana"
        assert resp["postal_code"] == "46534"
        assert resp["country"] == "United States"
        assert resp["longitude"] == "-86.627954"
        assert resp["latitude"] == "41.289715"
        assert resp["phone"] == "6308165790"
        assert resp["website_url"] is None
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_page(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "null"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "string"},
                'latitude': {"type": "string"},
                'phone': {"type": "null"},
                'website_url': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "1850-brewing-company-mariposa"
        assert resp["name"] == "1850 Brewing Company"
        assert resp["brewery_type"] == "micro"
        assert resp["street"] is None
        assert resp["city"] == "Mariposa"
        assert resp["state"] == "California"
        assert resp["postal_code"] == "95338"
        assert resp["country"] == "United States"
        assert resp["longitude"] == "-119.9036592"
        assert resp["latitude"] == "37.570148"
        assert resp["phone"] is None
        assert resp["website_url"] == "http://www.1850restaurant.com"
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_per_page(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "string"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "string"},
                'latitude': {"type": "string"},
                'phone': {"type": "string"},
                'website_url': {"type": "null"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "10-56-brewing-company-knox"
        assert resp["name"] == "10-56 Brewing Company"
        assert resp["brewery_type"] == "micro"
        assert resp["street"] == "400 Brown Cir"
        assert resp["city"] == "Knox"
        assert resp["state"] == "Indiana"
        assert resp["postal_code"] == "46534"
        assert resp["country"] == "United States"
        assert resp["longitude"] == "-86.627954"
        assert resp["latitude"] == "41.289715"
        assert resp["phone"] == "6308165790"
        assert resp["website_url"] is None
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_sort(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "string"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "string"},
                'latitude': {"type": "string"},
                'phone': {"type": "string"},
                'website_url': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "16-lots-brewing-mason"
        assert resp["name"] == "16 Lots Brewing"
        assert resp["brewery_type"] == "brewpub"
        assert resp["street"] == "753 Reading Rd"
        assert resp["city"] == "Mason"
        assert resp["state"] == "Ohio"
        assert resp["postal_code"] == "45040-1303"
        assert resp["country"] == "United States"
        assert resp["longitude"] == "-84.3183801"
        assert resp["latitude"] == "39.3545967"
        assert resp["phone"] == "5134863672"
        assert resp["website_url"] == "http://www.16lots.com"
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_random_brewery(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "city", "state", "postal_code",
                         "country", "updated_at", "created_at",
                         "address_2", "address_3"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] is not None
        assert resp["name"] is not None
        assert resp["brewery_type"] is not None
        assert resp["city"] is not None
        assert resp["state"] is not None
        assert resp["postal_code"] is not None
        assert resp["country"] is not None
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_size(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'phone': {"type": "string"},
                'website_url': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "city", "state", "postal_code",
                         "country", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

    @staticmethod
    def json_schema_search(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"},
                'brewery_type': {"type": "string"},
                'street': {"type": "null"},
                'address_2': {"type": "null"},
                'address_3': {"type": "null"},
                'city': {"type": "string"},
                'state': {"type": "string"},
                'county_province': {"type": "null"},
                'postal_code': {"type": "string"},
                'country': {"type": "string"},
                'longitude': {"type": "null"},
                'latitude': {"type": "null"},
                'phone': {"type": "string"},
                'website_url': {"type": "string"},
                'updated_at': {"type": "string"},
                'created_at': {"type": "string"}
            },
            "required": ["id", "name", "brewery_type", "street", "city", "state", "postal_code",
                         "country", "longitude", "latitude", "phone", "website_url", "updated_at", "created_at",
                         "address_2", "address_3", "county_province"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "barrel-assembly-austin"
        assert resp["name"] == "Barrel Assembly"
        assert resp["brewery_type"] == "planning"
        assert resp["street"] is None
        assert resp["city"] == "Austin"
        assert resp["state"] == "Texas"
        assert resp["postal_code"] == "78751-3019"
        assert resp["country"] == "United States"
        assert resp["longitude"] is None
        assert resp["latitude"] is None
        assert resp["phone"] == "15124236579"
        assert resp["website_url"] == "http://www.barrelassembly.com"
        assert resp["updated_at"] == "2022-10-30T06:11:39.514Z"
        assert resp["created_at"] == "2022-10-30T06:11:39.514Z"

    @staticmethod
    def json_schema_autocomplete(response: Response):
        """проверка структуры ответа на запрос"""
        resp = response.json()[0]
        schema = {
            "type": "object",
            "properties": {
                'id': {"type": "string"},
                'name': {"type": "string"}
            },
            "required": ["id", "name"]
        }

        validate(instance=response.json()[0], schema=schema)

        assert resp["id"] == "barrel-assembly-austin"
        assert resp["name"] == "Barrel Assembly"