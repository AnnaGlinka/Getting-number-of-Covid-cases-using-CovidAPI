from APIprovider import CountryListProvider, CovidCasesGenerator, APIError


# https://covid19api.com/
# A free API for data on Coronavirus
# documetation on Postman https://documenter.getpostman.com/view/10808728/SzS8rjbc

country_list_provider = CountryListProvider("/countries")
country_api_data = country_list_provider.get_data()
#print(cuntry_api_data)
country_list_provider.show_countries_list(country_api_data)

country_slug_list = country_list_provider.create_countries_slugs_list(country_api_data)
#print(country_slug_list)

country_slug = ""

i = 3
while i >= 0:
    try:
        country_input = input("Select the country from the list above: ")
        country_slug = country_list_provider.validate_input(country_input, country_slug_list)
        print(f"Selected country: {country_slug.capitalize()}")
        break
    except ValueError :
       print(f"{i} more chances left.")
    
    i -= 1

else:
    print("No correct value for country was selected.")

if country_slug:
    case = CovidCasesGenerator()
    try:
        covid_data_result = case.request_covid_data(country_slug, "2020-04-01", "2020-05-01")
    except APIError as api_err:
        print(api_err)
    else:
        covid_data_result = case.request_covid_data(country_slug, "2020-04-01", "2020-05-01")
        case.print_data_to_the_file(covid_data_result)
    

