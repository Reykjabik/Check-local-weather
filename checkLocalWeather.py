'''
As long as you have a URL, the webbrowser module lets users cut out the step of
opening the browser and directing themselves to a website. Other programs could
use this functionality to do the following:

AIM: Open the browser to the URL for your local weather.

'''
####### LIBRARIES WE'RE GOING TO NEED #######
# WEBBROWSER: to open links in a browser    #
# GEOCODER: to fetch the user's geolocation #
#############################################

import webbrowser, geocoder

# 1. We need to get the user's location first. We'll use the user's IP:
g = geocoder.ip('me')
lat = str(g.latlng[0])
long = str(g.latlng[1])

# 2. We are going to use Yandex Pogoda, since the building of the URL
#    is pretty easy once we have the latitude and longitude.
link = 'https://www.yandex.ru/pogoda/moscow?'
query_link = link + 'lat=' + lat + '&lon=' + long + '&via=srp'
webbrowser.open_new_tab(query_link)

# Tadaa!
