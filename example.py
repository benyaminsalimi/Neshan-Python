from NeshanAPI import *

api = NeshanAPI('your API KEY')
test = api.Location_Based('رضا','59.6157432','36.2880443')
result= test[0]
status_code= test[1]
print(result)
print(status_code)
