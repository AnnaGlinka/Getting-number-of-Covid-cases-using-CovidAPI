from APIprovider import CountryListProvider, CovidCasesGenerator

# https://covid19api.com/
# A free API for data on Coronavirus
# documetation on Postman https://documenter.getpostman.com/view/10808728/SzS8rjbc


country = CountryListProvider()

selected_country = country.getCountryCode()
print(f"Selected country: {selected_country.capitalize()}")

case = CovidCasesGenerator()
case.make_request(selected_country, "2020-04-01", "2020-05-01")
