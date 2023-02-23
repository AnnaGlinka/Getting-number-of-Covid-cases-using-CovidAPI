import requests
import pytest
from unittest import mock
import builtins
import json

from APIprovider import CountryListProvider, ReadDataFromAPI


# test the endpoint for list of the countries "https://api.covid19api.com/countries"
#pytest -v -s
#pytest -v -s test_api.py::test_can_call_counties_endpoint
#pytest -v -s test_api.py::test_can_call_covid_per_country_endpoint
#pytest -v -s test_api.py::test_get_country_code

query_params = {
        "from": "2020-04-01T00:00",
        "to": "2020-05-01T00:00:00Z"
    }


def test_can_call_counties_endpoint():
    endpoint_countries = "https://api.covid19api.com/countries"
    response = requests.get(endpoint_countries)
    assert response.status_code == 200


def test_can_call_covid_per_country_endpoint():
    endpoint_countries = "https://api.covid19api.com/country/chile"
    response = requests.get(endpoint_countries, params=query_params)
    assert response.status_code == 200


def test_create_countries_slugs_list():
    clp = CountryListProvider("/countries")
    api_url = "https://api.covid19api.com/countries"
    response_countries = requests.get(api_url)
    assert str(type(clp.create_countries_slugs_list(response_countries.json()))) == "<class 'dict'>"
   


    """
    tests symulates user input and checks output of the function
      with mock.patch.object(builtins, "input", lambda _: "Brazil "):
        clp = CountryListProvider()
        assert CountryListProvider.get_country_code(CountryListProvider) == "brazil"

    """
