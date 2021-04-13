# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages

def update_damages(list):
  new_list = []
  for data in list:
    if data == 'Damages not recorded':
      new_list.append('Damages not recorded')
    elif "M" in data:
      new_list.append(float(data.strip("M")) * conversion["M"])
    elif "B" in data:
      new_list.append(float(data.strip("B")) * conversion["B"])
  return new_list

updated_damages = update_damages(damages)
      
# print(update_damages)

# 2 
# Create a Table

# Create and view the hurricanes dictionary

def hurricanes_dict(names, months, years, max_winds, areas, damages, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes.update({
          names[i]: {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_winds[i], "Areas Affected": areas[i], "Damage": updated_damages[i], "Deaths": deaths[i]}})
    return hurricanes


hurricanes = hurricanes_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)


# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key

def hurricanes_by_year(dict):
  new_dict = {}
  for i in dict:
    current_year = dict[i]['Year']
    current_cane = dict[i]
    if current_year not in new_dict:
      new_dict[current_year] = current_cane
  return new_dict

hurricanes_by_year = hurricanes_by_year(hurricanes)

# print(hurricanes_by_year[1989])

# 4
# Counting Damaged Areas

def affected_areas(dictionary):
  new_dict = {}
  for i in dictionary:
    for j in dictionary[i]['Areas Affected']:
        if j not in new_dict:
          new_dict[j] = 1
        else:
          new_dict[j] += 1
  return(new_dict)


# create dictionary of areas to store the number of hurricanes involved in

affected_areas_count = affected_areas(hurricanes)

# print(affected_areas_count)


# 5 
# Calculating Maximum Hurricane Count

def most_affected(dict):
  max_no = 0
  max_name = ''
  for key, value in dict.items():
    if value > max_no:
      max_no = value
      max_name = key + ' ' + str(max_no)
  return max_name

# find most frequently affected area and the number of hurricanes involved in

max_hurricane_count = most_affected(affected_areas_count)

# 6
# Calculating the Deadliest Hurricane

def most_mortalities(dict):
  max_no = 0
  max_name = ''
  for i in dict:
    if dict[i]['Deaths'] > max_no:
      max_no = dict[i]['Deaths']
      max_name = i + ' ' + str(max_no)
  return max_name

# find highest mortality hurricane and the number of deaths

deadliest_hurricane = most_mortalities(hurricanes)

# 7
# Rating Hurricanes by Mortality

hurricanes_by_mortality = {1:[],2:[],3:[],4:[],5:[]}
def hurricane_rating(hurricanes):
  for i in hurricanes.keys():
    mortality_scale = {1:0, 2:100, 3:500, 4:1000, 5:10000}
    if hurricanes[i]["Deaths"] > mortality_scale[1] and hurricanes[i]["Deaths"] < mortality_scale[2]:
      hurricanes_by_mortality[1].append(hurricanes[i]['Name'])
  
    elif hurricanes[i]["Deaths"] > 100 and hurricanes[i]["Deaths"] < 500:
      hurricanes_by_mortality[2].append(hurricanes[i]['Name'])
  
    elif hurricanes[i]["Deaths"] > 500 and hurricanes[i]["Deaths"] < 1000:
      hurricanes_by_mortality[3].append(hurricanes[i]['Name'])
  
    elif hurricanes[i]["Deaths"] > 1000 and hurricanes[i]["Deaths"] < 10000:
      hurricanes_by_mortality[4].append(hurricanes[i]['Name'])
  
    elif hurricanes[i]["Deaths"] > 10000:
      hurricanes_by_mortality[5].append(hurricanes[i]['Name'])
  return hurricanes_by_mortality

# print(hurricane_rating(hurricanes))


# categorize hurricanes in new dictionary with mortality severity as key

mortality_hurricanes = hurricane_rating(hurricanes)

# 8 Calculating Hurricane Maximum Damage

def most_damage(dict):
  max = 0
  max_name = ''
  for i in hurricanes.keys():
    if type(hurricanes[i]['Damage']) == str:
      continue
    elif hurricanes[i]['Damage'] > max:
        max = hurricanes[i]['Damage']
        max_name = hurricanes[i]['Name']
  return max, max_name

# print(most_damage(hurricanes))


# find highest damage inducing hurricane and its total cost

most_damage_cane = most_damage(hurricanes)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def hurricane_damage_rating(hurricanes):

  hurricanes_by_damage = {k: [] for k in damage_scale.keys()}
  
  for i in hurricanes.keys():

    if type(hurricanes[i]["Damage"]) == str:
      continue

    elif hurricanes[i]["Damage"] > damage_scale[0] and hurricanes[i]["Damage"] < damage_scale[1]:
      hurricanes_by_damage[0].append(hurricanes[i])
  
    elif hurricanes[i]["Damage"] > 100000000 and hurricanes[i]["Damage"] < 1000000000:
      hurricanes_by_damage[1].append(hurricanes[i])
  
    elif hurricanes[i]["Damage"] > 1000000000 and hurricanes[i]["Damage"] < 10000000000:
      hurricanes_by_damage[2].append(hurricanes[i])
  
    elif hurricanes[i]["Damage"] > 10000000000 and hurricanes[i]["Damage"] < 100000000000:
      hurricanes_by_damage[3].append(hurricanes[i])
  
    elif hurricanes[i]["Damage"] > 100000000000:
      hurricanes_by_damage[4].append(hurricanes[i])
  return hurricanes_by_damage

hurricane_damage_ratings = hurricane_damage_rating(hurricanes)

# print(hurricane_damage_ratings)
