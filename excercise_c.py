united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]["capital"] = "Cardiff"
print(united_kingdom)
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append({
    "name": "Northern Ireland",
    "population": 1811000,
    "capital": "Belfast"})
# print(united_kingdom)    
# next time create new dictionary in a variable!
# 3. Use a loop to print the names of all the countries in the UK.
index = 0
for countries in united_kingdom:
    print(united_kingdom[index]["name"])
    index += 1

#for country in united_kingdom:
# print(country['name'])    

# 4. Use a loop to find the total population of the UK.
# index_1= 0
# population_uk = 0
# for population in united_kingdom:
#     pop = united_kingdom[index_1]["population"]
#     population_uk += int(pop)
#     index_1 += 1
# print(population_uk)    

total_pop = 0
for country in united_kingdom:
  total_pop += country["population"]
  #total_pop = total_pop + country["population"] is the same as line above
print(f'The total population of the UK is {total_pop}')