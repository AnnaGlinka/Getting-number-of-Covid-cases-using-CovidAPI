from APIprovider import CountryListProvider, CovidCasesGenerator

# https://covid19api.com/
# A free API for data on Coronavirus
# documetation on Postman https://documenter.getpostman.com/view/10808728/SzS8rjbc


country = CountryListProvider()
country.show_countries_list()


selected_country = country.get_country_code()
if selected_country:
    print(f"Selected country: {selected_country.capitalize()}")
else:
    print("No correct value for country was selected.")


case = CovidCasesGenerator()
case.make_request(selected_country, "2020-04-01", "2020-05-01")
