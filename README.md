# Dutch-Travel-Advices

This is a hobby project to visualize the travel advices given by the Dutch Ministry of Foreign Affairs, as well as learning more about creating maps (using geopandas) and creating gifs (using imageio).

This is not in any way linked to the Dutch Ministry of Foreign Affairs (sorry for scraping your website!).

Sources for the maps:
* [The travel advice maps that can be found through this page](https://www.nederlandwereldwijd.nl/help/in-welke-taal-communiceert-welk-land).
* [The twitter page of the Dutch Ministry of Foreign Affairs](https://twitter.com/247BZ). This was relevant, because I wanted some older data which in most cases they had.

## Maps and plots
Below a gif version:
![](compressed.gif)

Or below this the most recent jpg version:
![](most_recent_map.png)

Or want more quantified way? Here how much area is what color in the map (excluding cities):
![](area_over_time.png)

And another fun thing where I average them (which ofcourse should not be done with ordinal data, but fun nevertheless):
![](average.png)


## Notes (as well as a to-do list):
Because I rely on the natural earth data, specificically the [admin 1](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/), the disputed territories and the populated places, this makes it harder to perfectly mirror the maps made by the Dutch Ministry of Foreign Affairs. Therefore I have made a list of all countries where this is not (yet) perfect.

General note, I only started after the 10th of March of 2020. So everything before this, is a bit uncertain.

### American Samao

* (13/03/2020-14/04/2020) The map of American Samao was missing (instead the map of american virgin islands was shown). Therefor it is shown as grey.

### Armenia
* Border zones could not be incooporated.

### Bolivia
* A small part of Cochabamba is red after 21 February 2020.

### China
* The region Aksai Chin shows up in the maps of both Pakistan, China and India. Because it is de facto governed by China, the travel advice on the China page is chosen. This no endorsement.
* Taiwan has its own travel advice map, but is also included in the China map. Because Taiwan is de facto independent, I only use the Taiwan map.

### Ethiopia
* Part of Somali region is orange.
* A lot of stuff is actually transregions.

### Egypt
* Not all regions have only one colour.
* The Hala'ib triangle should be red, but I don't have a polygon for that yet.

### Georgia
* Borders are incorrect.

### Germany
* (28/10/2020-now) The city of Aachen has orange travel advice, but is not in the list of cities.

### India
* The region Aksai Chin shows up in the maps of both Pakistan, China and India. Because it is de facto governed by China, the travel advice on the China page is chosen. This no endorsement.
* Jammu and Kashmir overlap with Pakistan

### Indonesia
* Vulcanoes could not be added
* I could not find the city Donggala
* An area in Antan Jaya is orange which is not in the world map

### Iran
* Individual cities should be added
* Over time has not been incoorperated yet.
* Abu Musa, Greater Tunb and Lesser Tunb are claimed by UAE, but de facto governed by Iran. Therefor, I will follow the travel advice provided on the Iran page.

### Iraq
* The borders around Kurdistan are red (10-03-2020), but this has not been included in the world map.

### Israel
* Golan heights

### Italy
* (01/01/2020-now) The vulcanoes Vesuvius, Stromboli and Etna have red travel advices, could not be included in the world map.

### Ivory Coast
* Borders

### Japan
* A small area near Fukushima should be red.
* I'm not entirely sure when it switched from green to yellow in February/March.

### Lebanon
* The map is very colorful, which could not completely be mirrored.

### Libia
* Lot of provinces have different colors within one.
* I don't have the city information from before 20 February.

### Malaysia
* Sabah is partly yellow and orange.

### Marocco
* Some cities (including El Hoceima) do not appear in the natural earth dataset, but have a yellow travel advice.

### Mexico
* The border between US and Mexico is not in the world map (except for some cities)
* The city of Ixtapa

### Myanmar
* (01/01/2020-now) Not all cities that have a travel advice different than their surrounding were in the list of cities.

### North Macedonia
* The northern border should be yellow.

### Pakistan
* The region Aksai Chin shows up in the maps of both Pakistan, China and India. Because it is de facto governed by China, the travel advice on the China page is chosen. This no endorsement.
* Jammu and Kashmir overlap with India

### Peru
* Two rivers are orange (26-02-2020), but could not be reflected in the world map.
* The border with colombia is orange (26-02-2020), but could not be reflected in the world map.

### Saudi Arabia
* The border with Yemen is red (02-03-2020), but could not be reflected in the world map.
* The border with Iraq is orange (02-03-2020), but could not be reflected in the world map.

### Somalia

### Spain
* From 6-7, two small regions were orange. However, it was only possible to color the larger regions that those were part of as a whole.

### Syria
* Golan heights

### Taiwan
* Taiwan has its own travel advice map, but is also included in the China map. Because Taiwan is de facto independent, I only use the Taiwan map.

### UAE
* Abu Musa, Greater Tunb and Lesser Tunb are claimed by UAE, but de facto governed by Iran. Therefor, I will follow the travel advice provided on the Iran page.

### Hong Kong
### Macau
* duplicate with China
