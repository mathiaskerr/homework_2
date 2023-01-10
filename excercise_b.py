users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
jonathan_twitter = users["Jonathan"]["twitter"]
print(jonathan_twitter)
# 2. Get Erik's hometown
erik_home_town = users["Erik"]["home_town"]
print(erik_home_town)
# 3. Get the list of Erik's lottery numbers
erik_lottery_num = users['Erik']['lottery_numbers']
print( erik_lottery_num)
# 4. Get the species of Avril's pet Monty
avril_pet_species = users["Avril"]["pets"][0]["species"]
print(avril_pet_species)
# 5. Get the smallest of Erik's lottery numbers
erik_lowest_number = min(users['Erik']["lottery_numbers"])
print(erik_lowest_number)
# 6. Return an list of Avril's lottery numbers that are even
even_num = []
avril_lotto_num = users["Avril"]["lottery_numbers"]

for num in avril_lotto_num:
    if num % 2 == 0 :
        even_num.append(num)

print(even_num)        

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])
# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"]= "Edinburgh"
# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].insert(0,
    {
      "name": "fluffy",
      "species": "dog"
    },)

print(users["Erik"]["pets"])
# 10. Add another person to the users dictionary

users["Mathias"] = {"twitter" : "mathias123", "lottery_numbers" :[2,5,8,4,7,8], "home_town" : "Glasgow"} 
print(users["Mathias"])