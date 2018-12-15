# dictionary {"key":value} - pairs "json kind"

# NoSQL database| json for
# information of profile
information = {"name":"csk",
               "age":27,
               "city":["bangalore"],
               "area":{"btm":"street"}}

# print(information)
# # accessing the value of dictionary
# print(information["name"])
# print(information["age"])
# print(information["city"])
# print(information["area"]["btm"])
# input()
# function in dicionary
# print(dir(information))

# Assignment :
# ['clear', 'copy', 'fromkeys', 'get',
# 'items', 'keys', 'pop', 'popitem',
# 'setdefault', 'update', 'values']

# print(information.items())
# print(information.keys())
# print(information.values())
print(information)
information["name"] = "sathish"
information.pop("city")

print(information)
#print(information())
print(dir(information))

for value,key in information.items():
    print(value,key)