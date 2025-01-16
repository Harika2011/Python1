def get_country_code():
    country_codes = {
        'India': '0091',
        'Australia': '0025',
        'Nepal': '00977'
    }
    country = input("Enter the country name: ")
    code = country_codes.get(country)
    if code:
        print(f"The country code for {country} is {code}.")
    else:
        print(f"Country code for {country} is not available.")
get_country_code()
