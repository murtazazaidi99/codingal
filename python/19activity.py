# empty dictionary
my_dict={}
# dictionary with mixed keys
my_dict={'name':'zaidi',1:[2,5,12]}
my_dict={'name':'syed','age':18}
#output: syed
print(my_dict['name'])
print(my_dict.get('age'))
#update value
my_dict['age']=18
print(my_dict)
#add item
my_dict['address']='downtown'
print(my_dict)
#remove particular element
my_dict.pop('age')
print(my_dict)
# access a particular element
print('address:',my_dict.get('address'))
#remove all the elements
my_dict.clear()
print(my_dict)