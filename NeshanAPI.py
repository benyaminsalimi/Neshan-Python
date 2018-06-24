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

    def Test_Api_Key(self):
        url = 'https://api.neshan.org/v1/search'
        req = requests.get(url=url, headers=self.header)
        if req.status_code == 480:
            return False
        elif req.status_code == 200:
            return True
        else:
            print('something wrong')
            return False

    def Test_Location(self,latitude,longitude):
        url = self.api_url + 'reverse'
        param = {}
        param['lat'] = latitude
        param['lng'] = longitude
        req = requests.get(url=url, headers=self.header, params=param)
        if req.status_code==483:
            return False
        elif req.status_code == 200:
            return True
        else:
            print('Something wrong')
            return False

    def req(self,url,param=None):
        url = self.api_url + url
        req = requests.get(url=url, headers=self.header, params=param)
        result = req.json()
        status_code = req.status_code
        return result, status_code

    def Location_Based(self, term, latitude, longitude):
        url = 'search'
        param = {}
        param['term'] = term
        param['lat'] = latitude
        param['lng'] = longitude
        return self.req(url=url,param=param)

    def Reverse_Geocoding(self,latitude, longitude,):
        url = 'reverse'
        param = {}
        param['lat'] = latitude
        param['lng'] = longitude
        return self.req(url=url, param=param)

    def Direction(self,origin_latitude,origin_longitude,destination_latitude,destination_longitude,alternative):
        url = 'routing'
        param = {}
        if alternative is True:
            param['alternative'] = 'true'
        # latitude,longtitude
        param['origin'] = origin_latitude+','+origin_longitude
        param['destination'] = destination_latitude+','+destination_longitude
        return self.req(url=url, param=param)
