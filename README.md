# Dutch-Travel-Advices

This is a hobby project to visualize the travel advices given by the Dutch Ministry of Foreign Affairs, as well as learning more about creating maps (using geopandas) and creating gifs (using imageio).

This is not in any way linked to the Dutch Ministry of Foreign Affairs (sorry for scraping your website!).

![](compressed.gif)

Sources for the maps:
* [The travel advice maps that can be found through this page](https://www.nederlandwereldwijd.nl/help/in-welke-taal-communiceert-welk-land).
* [The twitter page of the Dutch Ministry of Foreign Affairs](https://twitter.com/247BZ). This was relevant, because I wanted some older data which in most cases they had.

## Notes (as well as a to-do list):
Because I rely on the natural earth data, specificically the [admin 1](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-1-states-provinces/), the disputed territories and the populated places, this makes it harder to perfectly mirror the maps made by the Dutch Ministry of Foreign Affairs. Therefore I have made a list of all countries where this is not (yet) perfect.

General note, I only started after the 10th of March of 2020. So everything before this, is a bit uncertain.

### Bolivia
* A small part of Cochabamba is red after 21 February 2020.

### China
* The region Aksai Chin shows up in the maps of both Pakistan, China and India. Because it is de facto governed by China, the travel advice on the China page is chosen. This no endorsement.
* Taiwan has its own travel advice map, but is also included in the China map. Because Taiwan is de facto independent, I only use the Taiwan map.

### India
* The region Aksai Chin shows up in the maps of both Pakistan, China and India. Because it is de facto governed by China, the travel advice on the China page is chosen. This no endorsement.


### Iran
* Individual cities should be added
* Over time has not been incoorperated yet.

### Japan
* A small area near Fukushima should be red.
* I'm not entirely sure when it switched from green to yellow in February/March.

### Libia
* A lot should be changed still

### Marocco
* Some cities (including El Hoceima) do not appear in the natural earth dataset, but have a yellow travel advice.

### North Macedonia
* The northern border should be yellow.

### Pakistan
* The region Aksai Chin shows up in the maps of both Pakistan, China and India. Because it is de facto governed by China, the travel advice on the China page is chosen. This no endorsement.

### Peru
* Two rivers are orange (26-02-2020), but could not be reflected in the world map.
* The border with colombia is orange (26-02-2020), but could not be reflected in the world map.

### Saudi Arabia
* The border with Yemen is red (02-03-2020), but could not be reflected in the world map.
* The border with Iraq is orange (02-03-2020), but could not be reflected in the world map.

### Taiwan
* Taiwan has its own travel advice map, but is also included in the China map. Because Taiwan is de facto independent, I only use the Taiwan map.
