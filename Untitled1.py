#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[["dnesh","20","chennai"],["kiran","madurai","30"]]#to handle the values in different order we use dictionary.
#this is another data type.


# In[4]:


a={"name":"dinesh","age":"20","location":"chennai"}
print(a.get("name"))
print(a["name"])


# In[5]:


a={"name":"dinesh","age":"20","location":"chennai"}
print(type(a))
print(isinstance(a,dict))


# In[6]:


a={"name":"dinesh","age":"20","location":"chennai"}


# In[7]:


a["add"]="test"
print(a)


# In[8]:


del a["add"]
print(a)


# In[9]:


print(len(a))
print(sorted(a))


# In[10]:


a={"name":"dinesh","age":"20","location":"chennai","name":"demo"}
print(a["name"])


# In[11]:


print(a.keys())#will give keys#result will be in "list"
print(a.values())#will give values#result will bi in "list"
print(a.items())#will give both keys and values # result will be in "list" and "tuple"


# In[12]:


##opertor
##arithmetic
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)##floor quotient
print(a%b)##modulus##reminder


# In[16]:


a=1753
b=275
print(a%b)


# In[14]:


##opertor
##assignment
a=5
b=2


# In[15]:


##operator
##relation
a=5
b=2
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)


# In[17]:


#logical operator
print(True and True) #True
print(True and False) #false
print(True or True) #true
print(True or False)# True
print(not True)#false
print(not False)#true


# In[ ]:




