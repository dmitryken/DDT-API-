import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://api.openbrewerydb.org/breweries/random?size=3",
        help="This is request url"
    )
    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "putch", "delete"],
        help="method to execute"
    )


@pytest.fixture
def base_url_2(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_method(request):
    return getattr(request, request.config.getoption("--method"))