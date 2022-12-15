from .methods import Http_methods


base_url = "https://jsonplaceholder.typicode.com"


class ApiPlace:

    @staticmethod
    def res_get_list():
        get_resource = "/posts/1"  # Resource method get
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        return result_get

    @staticmethod
    def res_list():
        get_resource = "/posts"
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.json())
        return result_get

