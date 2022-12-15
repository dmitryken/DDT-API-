import requests
import allure


class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            return result

    @staticmethod
    def post(url, body):
        with allure.step('POST'):
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            return result
