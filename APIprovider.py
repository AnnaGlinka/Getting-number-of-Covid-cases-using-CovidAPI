import requests
import pandas as pd
import pprint

class CountryListProvider:
    """
    The class creates a list of countries with it's codes for which data regarding Covid19 
    cases are available in the API
    https://documenter.getpostman.com/view/10808728/SzS8rjbc#7934d316-f751-4914-9909-39f1901caeIb8
    """

    __country_dict = {}

    def __init__(self):
        __endpoint = "https://api.covid19api.com/countries"
        __response = requests.get(__endpoint)
    
    
        for country in __response.json():
            self.__country_dict.update({country['Country']: country['Slug']})


    def show_countries_list(self):
        for country in CountryListProvider.__country_dict:
            print(country)
       
              
    def get_country_code(self):
        while True:
            selected_country = input(
                "Select the country from the list above: ")
            if selected_country in CountryListProvider.__country_dict:
                break
            print(
                "This country is not in the list. Please select a different one"
            )

        return CountryListProvider.__country_dict[selected_country]


class CovidCasesGenerator:
    """
    The class returns Covid19 data available in the API
    https://documenter.getpostman.com/view/10808728/SzS8rjbc#7934d316-f751-4914-9909-39f1901caeb8
    It returns all cases by case type (Confirmed, Recovered, Deaths) for a country from the first recorded 
    case or the selected start date and end date.
    It saves the data in the scv file.
    """

    def make_request(self, country, start_date=None, end_date=None):
        self.__country = country
        self.__start_date = start_date
        self.__end_date = end_date

        __query_params = {
            "from": f"{self.__start_date}T00:00",
            "to": f"{self.__end_date}T00:00:00Z"
        }

        __endpoint = f"https://api.covid19api.com/country/{self.__country}"
        response = requests.get(__endpoint, params=__query_params)

        if response.status_code in range(200, 299):
            __date = []
            __confirmed_cases = []
            __deaths = []
            __recovered = []
            for record in response.json():
                __date.append(record['Date'][:10])
                __confirmed_cases.append(record['Confirmed'])
                __recovered.append(record['Recovered'])
                __deaths.append(record['Deaths'])

            dict = {
                'Date': __date,
                'Confirmed': __confirmed_cases,
                'Recovered': __recovered,
                'Deaths': __deaths
            }
            df = pd.DataFrame(dict)

            if df.empty:
                print(
                    f"There was no confirmed Covid19 cases in {self.__country.capitalize()} between {self.__start_date} and {self.__end_date}"
                )

            else:
                print(df)
                df.to_csv(
                    f"Covid19 cases in {(self.__country).capitalize()}.csv",
                    index=False)
