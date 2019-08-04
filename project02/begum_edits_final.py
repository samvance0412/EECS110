import folium
import json
import urllib
import helpers
import pprint
import urllib.request
from urllib.request import urlopen


# cur = conn.cursor()
# cur.execute('''
#       SELECT id, substr(city, 12, 16) zip_code
#      FROM data_allegation
#      where length(city) > 13
#      LIMIT 50;
#  ''')
# cur.execute("select substr(city, LENGTH(city) - 5, 5) zip_code, count(*) from data_allegation where substr(city, LENGTH(city)-5, 0) = 6 group by 1")
# results = cur.fetchall()
# cur.close()
# conn.close()

# print(results)

# other_query = "select substr(city, 12, 16) zip_code, count(*) from data_allegation where length(city) > 13 group by 1"

# conn = sqlite3.connect("/Users/samvance/iCloud Drive⁩/Desktop⁩/Desktop⁩/Winter Quarter⁩/Classes⁩/EECS110⁩/projects⁩/⁨project02⁩/cpd.db
# ")
# cur = conn.cursor()
# # there isn't lat and lng so we tried to pull the zip codes as a last item [-1] from 
# # the address cell in the "data_allegation" table 
# cur.execute('''
#     SELECT id, substr(city, 12, 16)
#     FROM data_allegation
#     where length(city) > 13
#     LIMIT 50;
# ''')
# data = cur.fetchall()
# cur.close()
# conn.close()

# print(data)

# for i in data:
#     crime_id = i[0]
#     zip_code = i[1]

#  ( Visualize with zipcode and 06_make_a_map_with_data.py lines 40 on )
folium_map = folium.Map(
    location=[42.004583, -87.661406],
    zoom_start=13,
    tiles="Stamen toner"   # Switch to "Stamen watercolor"
)

color_dict = {"NARCOTICS":'green', "ASSAULT":'red', "BATTERY":'black',
 "THEFT":'teal', "BURGLARY":'magenta', "ROBBERY":'cyan', "CRIMINAL DAMAGE":'yellow', "ELSE":'gray'}

# add some markers to the map...
print('retrieving police department data...')
request = urllib.request.urlopen('https://data.cityofchicago.org/api/views/x2n5-8w5q/rows.json')
data = json.loads(request.read().decode())['data']
'''
Comments by Begum:
In the line 58 I added ['data'] because the dictionary you retrieve from cityofchicago has
2 keys, 'meta' and 'data'. 'data''s value is a list of lists. So one huge list where each element
is a small list that includes details of a certain crime instance. 
In the for loop below I go over this big list and look inside each crime instance to extract its 
location data, offense type etc. Since this data is in list, I can only access it with hard-coded
indices. 
To be able to debug the code faster I added an instance_counter and I look at only the first 100 instances
because there are too many crime instances in Chicago :S and it is taking time to go over them all. 
In your final submission, you can either remove it (that way it'll be true to the original data but it
might cover the entire map and not look good), or increase 100, because 100 is a small sample. 
I also did some changes in variable names to make the code more readable, and added some different color
options for circles which you can extend or edit if you like.
'''

print('creating map markers...')

instance_counter = 0

for crime_instance in data: 
    if instance_counter == 100: #You can remove or edit this to include more instances
        break
    
    lat = crime_instance[-3]
    lng = crime_instance[-2]
    if lat == None or lng == None: #There are some crime instances without lat/long info, I skip those
        continue
    lat = float(lat)
    lng = float(lng)
    offense = crime_instance[12]

    instance_counter = instance_counter + 1
    #offense_count = 
    
    #location = Block['Cached Contents']['Top']['item']
    #offense = PRIMARY DESCRIPTION['Cached Contents']['Top']['item']
    #offense_count = PRIMARY DESCRIPTION['Cached Contents']['Top']['count']
    #lat = ['latitude']
    #lng = ['longitude']
    #print(name, lat, lng, number of complaints

    if offense in color_dict.keys():
        offense_color = color_dict[offense]
    else:
        offense_color = color_dict["ELSE"]
    
    marker = folium.CircleMarker(
        location=[lat, lng],
        color= offense_color, 
        radius= 8, # originaly you have written offense_count * 8, but that is a bit hard to work with. I explained why below.
        fill_color= offense_color,
        fill_opacity=0.6)
    marker.add_to(folium_map)


print('generating the map file...')
file_name = 'chicago_crime.html' 
file_path = helpers.get_file_path(file_name, subdirectory='results')
folium_map.save(file_path)


'''
Offense count. One of the things I don't get about this is, do you want the radius to be multiplied by 
    (1) number of offenses that occured in that exact same spot (lat and lng), or 
    (2) number of occurences of that offense type in general?
I don't think (2) makes much sense, because then for example theft cases will have bigger circles but 
it won't mean that there are more thefts at that specific location when you look at the map. 
If you want to implement (1), it makes more sense, but I am not sure if any location repeats more than 
once in the dataset. Also, if you go with this approach, do you want to keep separate counters for different
types of offenses that happened at that location? This will complicate things even further.

In either of these cases you'll need a separate dictionary that will have one of the following formats:
    dictionary of (2):
        {
            "<offense_type>" : counter (an integer)
            "NARCOTICS" : 5, 
            "THEFT" : 40, etc.
        }
    dictionary of (1):
        {
            "<location tuple>" : counter (or another dictionary with counter for each offense type as in dictionary of (1))
            (41.224, -87.2) : 2
            or
            (41.224, -87.2) : {"NARCOTICS": 1
                                "THEFT": 1
                                "ROBBERY": 3 etc.}
        }
If you do implement this, code in lines from 106 to 112 will be removed from the current for loop it is in, 
because you'll use the current for loop to fill in these abovementioned dictionaries. Then, you'll write 
another for loop right below the current one and that one will go over dictionary you created and make the 
circles on map.
'''