from NeshanAPI import *

api = NeshanAPI('Your API-KEY from Neshan.org')

#Reverse_Geocoding(latitude, longitude)
address = api.Reverse_Geocoding('35.717596', '51.419728')
print('\n\n\ngeo location to address test:')
print(address)
print(address['address'])
print(address['neighbourhood'])
print(address['in_traffic_zone'])

#Location_Based(word_to_search, latitude, longitude)
location_search = api.Location_Based('رضا','59.6157432','36.2880443')
print('\n\n\nsearch place around one ponit')
print(location_search)

#Direction(origin_latitude,origin_longitude,destination_latitude,destination_longitude,alternative=None)
dir = api.Direction('35.695574','51.344047','35.722441','51.409321')
print('\n\n\nDirection test:')
print(dir)

#Distance_Duration(origin_latitude,origin_longitude,destination_latitude,destination_longitude):
dd = api.Distance_Duration('35.695574','51.344047','35.722441','51.409321')
print('\n\n\nDistance Duration between 2 point:')
print(dd[0]) # Distance  output: {'value': 11655.0, 'text': '۱۲ کیلومتر'}
print(dd[1]) # Duration output: {'value': 1720.0, 'text': '۲۹ دقیقه'}




