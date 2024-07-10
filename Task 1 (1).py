#!/usr/bin/env python
# coding: utf-8

# In[1]:


# creating a list
list_1=[10,20,30,40,50]

#Adding an element to the list
list_1.append(6)
print(list_1)

#removing an element from the list
list_1.remove(50)
print(list_1)

#modifying an element in the list
list_1[2]=15
print(list_1)

#inserting an element in the list
list_1.insert(3,45.0)

print("updated list is-",list_1)


# In[2]:


# creating a dictionary
dict_1={"employee":"mahesh","salary":10000,"job":"gardening"}

#adding a key value pair to the dictionary
dict_1["gender"]="male"
print(dict_1)

#removing a key value pair from the dictionary
del dict_1["job"]
print(dict_1)

# modifying the value in the dictionary
dict_1["employee"]="Ramesh"

print("updated dictioary is-",dict_1)


# In[3]:


# tuple
tuple_1 = (15,25,35)

# add new element to the tuple
element_1 = 45
my_tuple=tuple_1+(element_1,)
print(my_tuple)

# remove an element form the tuple
my_tuple=tuple_1[:1]+tuple_1[2:]
print(my_tuple)

#modifing a element in the tuple
mod_element=55
my_tuple=tuple_1[:1]+(mod_element,)
print(my_tuple)


# In[ ]:




