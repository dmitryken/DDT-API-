from .dog_http_methods import Http_methods
#from .conftest import param_fixture


base_url = "https://dog.ceo"


class ApiDog:
    '''Methods dog list'''

    @staticmethod
    def dog_list():
        get_resource = "/api/breed/hound/list"  # Resource method get
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        return result_get

    @staticmethod
    def dog_images():
        get_resource = "/api/breed/hound/afghan/images"
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        return result_get

    @staticmethod
    def dog_random(test_params):
        get_resource = "/api/breed/hound/afghan/images/random/"
        get_url = base_url + get_resource + test_params
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        return result_get
