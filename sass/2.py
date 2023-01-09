lst = range(5,15)
evel_list = [ x for x in lst if x % 2 == 0]
print(evel_list) 

list_squere = [x ** 3 for x in lst]
print(list_squere)

print([(x - 5) ** 2 for x in lst])