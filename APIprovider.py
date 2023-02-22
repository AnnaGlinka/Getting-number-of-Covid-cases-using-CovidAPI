import requests
import csv 


class APIError(Exception):

    def __init__(self, status):
        self.status = status
        
    def __str__(self):
        return f"APIError: status={self.status}"


class ReadDataFromAPI:

    def __init__(self, endpoint):
        self._APIurl = "https://api.covid19api.com" + endpoint

    def get_data(self, query_params={}):
        self._query_params = query_params
        _response = requests.get(self._APIurl, params=self._query_params)
        if _response.status_code != 200:
            raise APIError(_response.status_code)
        return _response.json()


class CountryListProvider(ReadDataFromAPI):
    """
    The class creates a list of countries with it's codes for which data regarding Covid19 
    cases are available in the API
    https://documenter.getpostman.com/view/10808728/SzS8rjbc#7934d316-f751-4914-9909-39f1901caeIb8
    """

    def __init__(self, endpoint):
        super().__init__(endpoint)

    def create_countries_slugs_list(self, api_countries):
        _country_list_with_slugs = {}
        for _country_record in api_countries:
            _country_list_with_slugs.update(
                {_country_record['Country']: _country_record['Slug']})
        return _country_list_with_slugs

    def show_countries_list(self, api_countries):
        for country_record in api_countries:
            print(country_record['Country'])

    def validate_input(self, input: str, countries_slugs: dict) -> str:
        if input in countries_slugs:
            return countries_slugs[input]
        raise ValueError("This country is not in the list.")


class CovidCasesGenerator(ReadDataFromAPI):
    """
    The class returns Covid19 data available in the API
    https://documenter.getpostman.com/view/10808728/SzS8rjbc#7934d316-f751-4914-9909-39f1901caeb8
    It returns all cases by case type (Confirmed, Recovered, Deaths) for a country from the first recorded 
    case or the selected start date and end date.
    It saves the data in the scv file.
    """

    def __init__(self, endpoint, country_slug):
        self._country_slug = country_slug
        _endpoint = f"{endpoint}{self._country_slug}"
        super().__init__(_endpoint)

    def print_data_to_the_file(self, data: dict):
        self._data = data
        _selected_country = self._data[0]['Country']

        with open(f'Covid19 cases in {_selected_country}.csv', 'w', encoding='UTF8') as f:
            self._writer = csv.writer(f)
            _header = ["Date", "Confirmed", "Recovered", "Deaths"]
            print(_header)
            self._writer.writerow(_header)
            for record in self._data:
                data_record_line = record['Date'][:10], record['Confirmed'], record['Recovered'], record['Deaths'] 
                print(data_record_line)
                self._writer.writerow(data_record_line)
                
     
        
      