from APIprovider import CountryListProvider, CovidCasesGenerator
from pydantic import ValidationError

# https://covid19api.com/
# A free API for data on Coronavirus
# documetation on Postman https://documenter.getpostman.com/view/10808728/SzS8rjbc

country_list_provider = CountryListProvider()
country_list_provider.show_countries_list()

country_slug = ""

i = 3
while i >= 0:
    try:
        country_input = input("Select the country from the list above: ")
        country_slug = country_list_provider.get_coutry_slug(country_input)
        break
    except:
        print(f"{i} more chances left.")
    
    i -= 1

if country_slug:
    print(f"Selected country: {country_slug.capitalize()}")
else:
    print("No correct value for country was selected.")

case = CovidCasesGenerator()
case.make_request(country_slug, "2020-04-01", "2020-05-01")
