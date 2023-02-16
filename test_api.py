import requests
import pytest
from unittest import mock
import builtins

from APIprovider import CountryListProvider


# test the endpoint for list of the countries "https://api.covid19api.com/countries"
#pytest -v -s
#pytest -v -s test_api.py::test_can_call_counties_endpoint
#pytest -v -s test_api.py::test_can_call_covid_per_country_endpoint
#pytest -v -s test_api.py::test_get_country_code


def test_can_call_counties_endpoint():
    endpoint_countries = "https://api.covid19api.com/countries"
    response = requests.get(endpoint_countries)
    assert response.status_code == 200


def test_can_call_covid_per_country_endpoint():
    endpoint_countries = "https://api.covid19api.com/country/chile"
    response = requests.get(endpoint_countries)
    assert response.status_code == 200


def test_get_country_code():
    """
    tests symulates user input and checks output of the function
    """
    with mock.patch.object(builtins, "input", lambda _: "Brazil"):
        assert CountryListProvider.get_country_code(CountryListProvider) == "brazil"