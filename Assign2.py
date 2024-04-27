#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.What are the two values of the Boolean data type? How do you write them?
# True & False


# In[2]:


#2. What are the three different types of Boolean operators?
#and,or,not


# In[7]:


#3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
#True and True = True
#True and False = False
#True or True = True
#True or False = True
#not True = False
#not False = True


# In[8]:


#4. What are the values of the following expressions?
#(5 > 4) and (3 == 5) = false
#not (5 > 4) = False
#(5 > 4) or (3 == 5) = True
#not ((5 > 4) or (3 == 5)) = False
#(True and True) and (True == False)  = False
#(not False) or (not True)= True


# In[10]:


#5. What are the six comparison operators?
# ==
# >=
# !=
# >
# <
# <=


# In[1]:


#How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
#The '=' is the so-called assignment operator and is used to assign the result of the expression on the right side of the 
# operator to the variable on the left side. The '==' is the so-called equality comparison operator and is used 
# to check whether the two expressions on both sides are equal or not.
# assignment 
a=1
# equal to
1==1


# In[4]:


#7. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')
#Result
#ham
#spam
#spam


# In[5]:


#8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
#Greetings! if anything else is stored in spam.
if spam ==1:
    print('Hello')
if spam ==2:
    print('Howdy')
else:
    print('Greeting!')


# In[6]:


#9.If your programme is stuck in an endless loop, what keys you’ll press?
#Ans- ctrl+c


# In[7]:


#10. How can you tell the difference between break and continue?
#The Break statement stops the entire loop process. Whereas the Continue statement only stops the current iteration of the loop.


# In[8]:


#11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# In range(10) range will start from 0 and will go till 9
# In range(0,10) range will start from 0 and will go till 9
# In range (0,10,1) range will start from 0 and will go till 9 with gap of 1


# In[14]:


#12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
#program that prints the numbers 1 to 10 using a while loop.
for a in range(0,11):
    print(a)
a=1
while a<11:
    print(a)
    a+=1
    


# In[13]:


#13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
spam.bacon()


# In[ ]:




