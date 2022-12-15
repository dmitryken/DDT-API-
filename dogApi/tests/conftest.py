import pytest


@pytest.fixture(params=["1", "2", "3"], ids=["1 images", "2 images", '3 images'])
def param_fixture(request):
    return request.param
