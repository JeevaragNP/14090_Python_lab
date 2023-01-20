dict = { "brand":"Lamborghini", "Model":"Hurrican", "year":"2020" }
print(dict)
print(dict["brand"])
x= dict.get("Model")
print(x)
y = dict.values()
print(y)
dict["year"] = 2022
print(dict)
dict.update({"Model":"Aventador"})
print(dict)
dict["Transmission"] = "Automatic"
print(dict)
dict.update({"Engine":"V12"})
print(dict)
'''dict.pop("year")
print(dict)
dict.popitem()
print(dict)
del dict["year"]
print(dict)
dict.clear()
print(dict)'''
dict2 = dict.copy()
print(dict2)
for i in dict2.values():
    print(i,end="-")
print()
for i in dict2.keys():
    print(i,end=", ")
