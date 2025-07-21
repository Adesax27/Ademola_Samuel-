city_name = "Accra"
elevation = 61
population = 4200000
#opning text file
with open("cities_txt", "at") as cities_file:
    print(city_name, file=cities_file)
    print(f"{elevation}, {population}", file=cities_file)
    #file.write(f"{city_name}, {elevation},{population},{cities_file}")