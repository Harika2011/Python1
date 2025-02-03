class USA:
    def capital(self):
        print("The capital of USA is Washington, D.C.")

    def language(self):
        print("The official language of USA is English.")

    def type_of_country(self):
        print("USA is a developed country.")

class India:
    def capital(self):
        print("The capital of India is New Delhi.")

    def language(self):
        print("The official languages of India is Hindi and English.")

    def type_of_country(self):
        print("India is a developing country.")


def country_info(country):
    country.capital()
    country.language()
    country.type_of_country()

usa = USA()
india = India()

print("Information on USA")
country_info(usa)

print("\n Information on INDIA")
country_info(india)
