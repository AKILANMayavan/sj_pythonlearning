# array list

# list of elements

fruit_list_sametype = ["apple","orange","grapes"]
print(fruit_list_sametype)

# index[0:"apple",1:"orange",2:"grapes",3 :20,4:20.5,5:30,6:'111']
fruit_list_multitype = ["apple","orange","grapes",20,20.5,30,'111']
print(fruit_list_multitype)

# index starts from 0
print(fruit_list_multitype[0])

# output ["apple",20]
# syntax : array[start:end:skip]
print(fruit_list_multitype[0:4:3])
print(fruit_list_multitype[0:4])


# adding an element to list
fruit_list_multitype.append("pine apple")
print(fruit_list_multitype)

#fruit_list_multitype[3] = "pine apple"
fruit_list_multitype.insert(4,"pine")

print(fruit_list_multitype)
print(type(fruit_list_multitype))
print(dir(fruit_list_multitype))