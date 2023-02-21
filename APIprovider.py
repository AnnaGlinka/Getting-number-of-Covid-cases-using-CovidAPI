import requests
import pandas as pd
import pprint

class APIError(Exception):
    
    def __init__(self, status):
        self.status = status

    def __str__(self):
        return f"APIError: status={self.status}"


class ReadDataFromAPI:

    def __init__(self, endpoint):
        self._APIurl = "https://api.covid19api.com" + endpoint
        
    def get_data(self):
        _response = requests.get(self._APIurl)
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
            _country_list_with_slugs.update({_country_record['Country']: _country_record['Slug']})
        return _country_list_with_slugs
            

    def show_countries_list(self, api_countries):
        for country_record in api_countries:
            print(country_record['Country'])
        

    def validate_input(self, input: str, countries_slugs: dict) -> str:
        if input in countries_slugs:
            return countries_slugs[input]
        raise ValueError("This country is not in the list.")



class CovidCasesGenerator:
    """
    The class returns Covid19 data available in the API
    https://documenter.getpostman.com/view/10808728/SzS8rjbc#7934d316-f751-4914-9909-39f1901caeb8
    It returns all cases by case type (Confirmed, Recovered, Deaths) for a country from the first recorded 
    case or the selected start date and end date.
    It saves the data in the scv file.
    """

    def request_covid_data(self, country, start_date=None, end_date=None):
        self.__country = country
        self.__start_date = start_date
        self.__end_date = end_date

        __query_params = {
            "from": f"{self.__start_date}T00:00",
            "to": f"{self.__end_date}T00:00:00Z"
        }

        __endpoint = f"https://api.covid19api.com/country/{self.__country}"
        response = requests.get(__endpoint, params=__query_params)
        if response.status_code != 200:
            raise APIError(response.status_code)
      

        __date = []
        __confirmed_cases = []
        __deaths = []
        __recovered = []
        for record in response.json():
            __date.append(record['Date'][:10])
            __confirmed_cases.append(record['Confirmed'])
            __recovered.append(record['Recovered'])
            __deaths.append(record['Deaths'])

        confirmed_death_recovered_data = {
            'Date': __date,
            'Confirmed': __confirmed_cases,
            'Recovered': __recovered,
            'Deaths': __deaths
        }
        return confirmed_death_recovered_data

            

    def print_data_to_the_file(self, data: dict):
        df = pd.DataFrame(data)
        if df.empty:
            print(
                f"There was no confirmed Covid19 cases in {self.__country.capitalize()} between {self.__start_date} and {self.__end_date}"
            )
        else:
            print(df)
            df.to_csv(f"Covid19 cases in {(self.__country).capitalize()}.csv", index=False)
