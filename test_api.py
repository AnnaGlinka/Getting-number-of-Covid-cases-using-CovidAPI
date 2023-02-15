import requests

# test the endpoint for list of the countries "https://api.covid19api.com/countries"
#pytest -v -s
#pytest -v -s test_api.py::test_can_call_counties_endpoint
#pytest -v -s test_api.py::test_can_call_covid_per_country_endpoint


def test_can_call_counties_endpoint():
    endpoint_countries = "https://api.covid19api.com/countries"
    response = requests.get(endpoint_countries)
    assert response.status_code == 200


def test_can_call_covid_per_country_endpoint():
    endpoint_countries = "https://api.covid19api.com/country/chile"
    response = requests.get(endpoint_countries)
    assert response.status_code == 200