dic = {'a': 1, 'b': 2}
dic['a'] = 3 # Modifies the existing dictionary object
dic['r'] = 9 #add element in dic
print(dic)
zabeer_cars = {
    "1":"mustang",
    "2":"primio",
    "3":"allion"
    }
robin_cars = {
    "1":"mustang",
    "2":"4v",
    "3":"pulser"
    }
saif_cars = {
    "1":"thriller",
    "2":"kpr",
    "3":"gixxer"
    }
for i , car in enumerate(robin_cars):
    print(car,robin_cars[car],i)

#list
list = [zabeer_cars["1"],robin_cars,saif_cars]
print(list)