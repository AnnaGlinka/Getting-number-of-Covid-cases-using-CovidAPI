from APIprovider import CountryListProvider, CovidCasesGenerator, APIError
import pprint


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
        print(f"Selected country slug: {country_slug.capitalize()}")
        break
    except ValueError :
       print(f"{i} more chances left.")
    
    i -= 1

else:
    print("No correct value for country was selected.")

if country_slug:

    query_params = {
            "from": "2020-04-01T00:00",
            "to": "2020-05-01T00:00:00Z"
        }
    ccg = CovidCasesGenerator("/country/", country_slug)
    try:
        covid_data_result = ccg.get_data(query_params)
    except APIError as api_err:
        print(api_err)
    else:
        #print(covid_data_result[0])
        if  covid_data_result == []:
            print(f"No data for {country_input} for dates form {query_params['from']} to {query_params['to']}")
        else:
            ccg.print_data_to_the_file(covid_data_result)
    
    

