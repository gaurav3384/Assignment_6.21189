# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 00:48:53 2018

@author: gauravkgupta
"""

import matplotlib.pyplot as plt
import pandas as pd


#url= 'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_origina l.csv'
titanic = pd.read_csv('titanic_original.csv')

#1. Create a pie chart presenting the male/female proportion
labels= 'male', 'female'
sizes = [titanic[titanic.sex =='male'].shape[0], titanic[titanic.sex =='female'].shape[0]]
fig1, ax1 = plt.subplots()
plt.pie(sizes, labels=labels)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# scatter plot for fare paid and age with different colour for male and female
male_age=titanic[titanic.sex == 'male']['age']
males_fare=titanic[titanic.sex == 'male']['fare']
female_age=titanic[titanic.sex == 'female']['age']
females_fare= titanic[titanic.sex == 'female']['fare']
plt.scatter(male_age, males_fare, color='r')
plt.scatter(female_age, females_fare, color='g')
plt.xlabel('Age')
plt.ylabel('fare')
plt.show()