#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data

# ## Prison Helicopter Escapes

# I begin by importing some helper functions.

# In[2]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(url)


# Let's print the first three rows

# In[4]:


print(data[0:3])


# Now I delete the last column of each row (the detail column)

# In[5]:


index = 0
for row in data:
    data[index] = row[0:-1]
    index = index + 1


# In[6]:


print(data[0])


# Next, I change the date format to display only the year.

# In[7]:


for row in data:
    row[0] = fetch_year(row[0])


# In[8]:


print(data[0])


# Extracting the minimum and maximum years in the data

# In[9]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# In[10]:


print(min_year)
print(max_year)


# Creating a list of years that includes all the years within the year range

# In[11]:


years = []
for year in range(min_year, max_year +1):
    years.append(year)


# In[12]:


print(years)


# In[13]:


attempts_per_year = []
for year in years:
    tracker = [year, 0]
    attempts_per_year.append(tracker)
print(attempts_per_year)


# In[14]:


for case in attempts_per_year:
    year = case[0]
    for row in data:
        if row[0] == year:
            case[1] += 1
print(attempts_per_year)


# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In which year did the most attempts at breaking out of prison with a helicopter occur? Answer: The most attempts happened in the years 1986, 2001, 2007, and 2009.

# Next, let's determine in which country the most prision break attempts happen

# In[18]:


countries_frequency = df["Country"].value_counts()


# In[19]:


print_pretty_table(countries_frequency)


# In[ ]:




