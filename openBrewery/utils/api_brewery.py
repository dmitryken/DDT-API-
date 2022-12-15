from openBrewery.utils.brew_http_methods import Http_methods

base_url = "https://api.openbrewerydb.org/"


class Brewery:

    @staticmethod
    def single_brewery():
        '''Get solo brewery'''
        get_resource = "breweries/madtree-brewing-cincinnati"
        get_url = base_url + get_resource
        print(get_url)
        result_single_brewery_get = Http_methods.get(get_url)
        print(result_single_brewery_get.json())
        return result_single_brewery_get

    @staticmethod
    def list_breweries():
        '''Get list brewery'''
        get_resource = "breweries?per_page=3"
        get_url = base_url + get_resource
        print(get_url)
        result_list_breweries_get = Http_methods.get(get_url)
        print(result_list_breweries_get.json())
        return result_list_breweries_get

    @staticmethod
    def filter_breweries_by_city():
        '''Filter breweries by city.'''
        get_resource = "breweries?by_city=san_diego&per_page=3"
        get_url = base_url + get_resource
        print(get_url)
        result_filter_breweries_by_city_get = Http_methods.get(get_url)
        print(result_filter_breweries_by_city_get.json())
        return result_filter_breweries_by_city_get

    @staticmethod
    def sort_breweries_by_dist():
        '''Sort the results by distance from an origin point, denoted by latitude,longitude.'''
        get_resource = "breweries?by_dist=38.8977,77.0365&per_page=3"
        get_url = base_url + get_resource
        print(get_url)
        result_sort_breweries_by_dist_get = Http_methods.get(get_url)
        print(result_sort_breweries_by_dist_get.json())
        return result_sort_breweries_by_dist_get

    @staticmethod
    def filter_breweries_by_name():
        '''Filter breweries by name.'''
        get_resource = "breweries?by_name=cooper&per_page=3"
        get_url = base_url + get_resource
        print(get_url)
        result_filter_breweries_by_name_get = Http_methods.get(get_url)
        print(result_filter_breweries_by_name_get.json())
        return result_filter_breweries_by_name_get

    @staticmethod
    def filter_breweries_by_state():
        '''Filter breweries by state.'''
        get_resource = "breweries?by_state=new_york&per_page=3"
        get_url = base_url + get_resource
        print(get_url)
        result_filter_breweries_by_state_get = Http_methods.get(get_url)
        print(result_filter_breweries_by_state_get.json())
        return result_filter_breweries_by_state_get

    @staticmethod
    def filter_breweries_by_postal():
        '''Filter breweries by postal code.'''
        get_resource = "breweries?by_postal=44107&per_page=3"
        get_url = base_url + get_resource
        print(get_url)
        result_filter_breweries_by_postal_get = Http_methods.get(get_url)
        print(result_filter_breweries_by_postal_get.json())
        return result_filter_breweries_by_postal_get

    @staticmethod
    def filter_breweries_by_type():
        '''Filter by type of brewery.'''
        get_resource = "breweries?by_type=micro&per_page=3"
        get_url = base_url + get_resource
        print(get_url)
        result_filter_breweries_by_type_get = Http_methods.get(get_url)
        print(result_filter_breweries_by_type_get.json())
        return result_filter_breweries_by_type_get

    @staticmethod
    def breweries_page():
        '''The offset or page of breweries to return.'''
        get_resource = "breweries?page=15&per_page=3"
        get_url = base_url + get_resource
        print(get_url)
        result_breweries_page_get = Http_methods.get(get_url)
        print(result_breweries_page_get.json())
        return result_breweries_page_get

    @staticmethod
    def breweries_per_page():
        '''Number of breweries to return each call.'''
        get_resource = "breweries?per_page=2"
        get_url = base_url + get_resource
        print(get_url)
        get_result = Http_methods.get(get_url)
        print(get_result.json())
        return get_result

    @staticmethod
    def sort_result():
        '''Sort the results by one or more fields.
            asc for ascending order
            desc for descending order'''
        get_resource = "breweries?by_state=ohio&sort=type,name:asc&per_page=3"
        get_url = base_url + get_resource
        print(get_url)
        result_sort_result_get = Http_methods.get(get_url)
        print(result_sort_result_get.json())
        return result_sort_result_get

    @staticmethod
    def random_brewery():
        '''Get a random brewery.'''
        get_resource = "breweries/random"
        get_url = base_url + get_resource
        print(get_url)
        result_random_brewery_get = Http_methods.get(get_url)
        print(result_random_brewery_get.json())
        return result_random_brewery_get

    @staticmethod
    def size_brewery(get_url):
        '''Number of breweries to return each call. Note: Default is 1. Max per page is 50.'''
        print(get_url)
        result_size_brewery_get = Http_methods.get(get_url)
        print(result_size_brewery_get.json())
        return result_size_brewery_get

    @staticmethod
    def search_breweries():
        '''Search for breweries based on a search term.'''
        get_resource = "breweries/search?query=dog&per_page=3"
        get_url = base_url + get_resource
        print(get_url)
        result_search_breweries_get = Http_methods.get(get_url)
        print(result_search_breweries_get.json())
        return result_search_breweries_get

    @staticmethod
    def autocomplete_brewery():
        '''Return a list of names and ids of breweries based on a search term. This endpoint is typically used for a
        drop-down selection.The maximum number of breweries returned is 15.'''
        get_resource = "breweries/autocomplete?query=dog"
        get_url = base_url + get_resource
        print(get_url)
        result_autocomplete_brewery_get = Http_methods.get(get_url)
        print(result_autocomplete_brewery_get.json())
        return result_autocomplete_brewery_get