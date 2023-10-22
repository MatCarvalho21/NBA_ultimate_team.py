import iso3166

dict_of_countries = dict(iso3166.countries_by_name)

dict_rigth_countries = dict()

for each_country_name, each_country_values in dict_of_countries.items():
    dict_rigth_countries[f"{each_country_name}"] = each_country_values.alpha2