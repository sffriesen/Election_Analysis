#counties = ["Arapahoe", "Denver", "Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not in the list of counties")

#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties")
#else:
#    print("Arapahoe or El Paso is not in the list of counties")

#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")
#else:
#    print("Arapahoe and El Paso are not in the lsit of counties")

#for county in counties:
#    print(county)


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "Registered_voters":432438}]

#for county_dict in voting_data:
#    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)