import pytest

base_url = 'https://ya.ru'
status_code = 200


def pytest_addoption(parser):
    parser.addoption(base_url)
    parser.addoption(status_code)


@pytest.fixture
def base_url(request):
    return request.config.getoption("base_url")