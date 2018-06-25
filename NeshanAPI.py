import requests

__author__='Benyamin.Salimi@gmail.com'
__repository__='https://github.com/benyaminsalimi/Neshan-Python'

class NeshanAPI(object):
    def __init__(self,key):
        self.header = {}
        self.header['Api-Key'] = key
        self.header['user-agent'] = 'Neshan API Python lib'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        self.api_url = 'https://api.neshan.org/v1/'

    def req(self,url,param=None):
        url = self.api_url + url
        req = requests.get(url=url, headers=self.header, params=param)
        try:
            result = req.json()
        except:
            result = {'status':'Api return empty value with 200 status code!'}
        return result

    def Location_Based(self, term, latitude, longitude):
        url = 'search'
        param = {}
        param['term'] = term
        param['lat'] = latitude
        param['lng'] = longitude
        return self.req(url=url,param=param)

    def Reverse_Geocoding(self,latitude, longitude):
        url = 'reverse'
        param = {}
        param['lat'] = latitude
        param['lng'] = longitude
        return self.req(url=url, param=param)

    def Direction(self,origin_latitude,origin_longitude,destination_latitude,destination_longitude,alternative=None):
        url = 'routing'
        param = {}
        if alternative is True:
            param['alternative'] = 'true'
        # latitude,longtitude
        param['origin'] = origin_latitude+','+origin_longitude
        param['destination'] = destination_latitude+','+destination_longitude
        return self.req(url=url, param=param)

    def Distance_Duration(self,origin_latitude,origin_longitude,destination_latitude,destination_longitude):
        url = 'routing'
        param = {}
        # latitude,longtitude
        param['origin'] = origin_latitude + ',' + origin_longitude
        param['destination'] = destination_latitude + ',' + destination_longitude
        r = self.req(url=url,param=param)
        distance = r['routes'][0]['legs'][0]['distance']
        duration = r['routes'][0]['legs'][0]['duration']
        return distance, duration