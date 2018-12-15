# Tuple datastructure
# item basket with price
# tuple is fixed
item_price_list = ["apple",250,"red"]
item_price = ("apple",250,"red")
print(item_price)
print(item_price_list)
print("After changing value")
item_price_list[2]="green"
print(item_price_list)
print(dir(item_price_list))

# item_price[2]="green"
# print(item_price)
print(dir(item_price))
input()
# functions in tuple
print(dir(item_price))

# Assingnment : ['count', 'index']

print(item_price[0])
# TODO : Check why count is used in tuple
print(item_price.count(1))
print(len(item_price))
#
# item_price["apple"] = "aa"
# print(item_price)

item_price_list = list(item_price)
item_price_list[0]="aa"
print(item_price_list)
print(dir(item_price_list))

# tuple is fixed length
tuple_month = ("Jan","Feb","Mar","so on")
print(tuple_month)

# days in month
list_days = [1,2,3,30]
