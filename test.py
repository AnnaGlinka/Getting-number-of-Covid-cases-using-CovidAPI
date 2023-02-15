import requests

# test the endpoint for "https://api.covid19api.com/countries"

endpoint_countries = "https://api.covid19api.com/countries"

def test_can_call_endpoint_countries():
    response = requests.get(endpoint_countries)
    assert response.status_code == 200