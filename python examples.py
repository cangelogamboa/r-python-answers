#!/usr/bin/env python
# coding: utf-8

# In[3]:


#define variables
intvar = 5
charvar = 'c'
stringvar = "hello world"
floatvar = 6.78


# In[4]:


#print variables
print intvar
print charvar
print stringvar
print floatvar


# In[5]:


#concatanate strings and variables
print "stringvar = " + stringvar
print "intvar = " + str(intvar)


# In[8]:


import sys
if (intvar != 5):
    print "exiting program"
    sys.exit


# In[10]:


a = 10; b = 5; c = 1
if(a<b):
    d = 1
elif (a == b):
    d = 2
else:
    d = 3
print d


# In[11]:


count = 0
while (count < 9):
    print 'The count is: ' + str(count)
    count = count + 1


# In[12]:


for letter in 'Python':     # First Example
   print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print 'Current fruit :', fruit


# In[20]:


def mySum(a,b):
    return a + b;
a1 = mySum(3,3)
b1 = mySum(4.6,4.6)
mySum('a','b')


# In[19]:


def multiply(a,b):
    return a*b;

multiply(3,20)
multiply(4.5,6.5)
multiply('b','d')


# In[25]:


#A 2 row, 3 column Python list
x = [1,2,3],[4,5,6]


# In[27]:


#The value at the second row, second column
x[1][1]


# In[28]:


x[0][0]


# In[29]:


x


# In[31]:


y = ["cat",3,"arm"],["dog",4,"leg"],["fish", 7.5,"head"]


# In[32]:


y[0][0]


# In[ ]:




