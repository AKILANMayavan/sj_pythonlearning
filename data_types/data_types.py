# Commenting
# Notes on data types
# Data Types - string, float, int
# create string variable

# Datatype - Integer

income = 10000

print("Income is "+str(income))

# type of variable - class
print(type(income))

# TODO : change variable in future (Reminder|notes|reference)
# Data type - String

name_1 = 'csk'
name_2 = "csk"
name_3 = """
            csk
            csk
        """

print("name 1 ",name_1)
print("name 2 " +name_2)
print("name 3 "+name_3)
print(type(name_1),type(name_3),type(name_3))

# Datatype - Float

year_exp = 3.5
print("YOE "+str(year_exp))
print(type(year_exp))

# dir function - Getting the functions which acts on variable
print(dir(year_exp))
print(year_exp.hex())

# getting help
print(help(float))


# Time
import time
print(help(time))
print(time.localtime())

# Time extraction - regex (regular expression) ddmmyyyy or dd/mm/yyyy