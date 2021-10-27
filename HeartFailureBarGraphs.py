# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 16:36:09 2021

@author: Isaac
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

dataset = pd.read_csv('C:/Users/Isaac/Desktop/HeartDisease/heart.csv')
#print(dataset)

    
#This method shows a visual of the gender in this dataset   
def SexCount(ds):

    sex_count = ds['Sex'].value_counts()
    
    print("Number of males in the dataset",ds['Sex'].tolist().count('M'))
    print("Number of females in the dataset",ds['Sex'].tolist().count('F'))
    
    plt.figure(figsize = (100,60))
    plt.rcParams['font.size'] = 150
    plt.xlabel("Gender", fontsize = 150, color = 'red', labelpad =100)
    plt.ylabel("Number of Female/Male", fontsize =150, color = 'red', labelpad =100)
    plt.title("Gender in the Dataset", fontsize = 150, color = 'red')
    theLegend = mpatches.Patch(label='Gender total 918')
    plt.legend(handles=[theLegend])
    
    ax= sex_count.plot(kind ='bar', edgecolor = 'black', linewidth = 30, width = .8, color = 'cyan')

    plt.ylim(0,1000)
    plt.yticks(np.arange(0,1000,50))
    plt.xticks(rotation = 0)
     

    for i, v in sex_count.reset_index().iterrows():
        ax.text(i-.1, v.Sex + 40 , v.Sex, color='red', fontsize = 150)

    plt.show()



def Ages(ds):
    
    age_count = ds['Age'].value_counts().sort_index()
    
    plt.figure(figsize = (300,100))
    
    plt.rcParams['font.size'] = 200
    plt.xlabel("Age", fontsize = 300, color = 'red', labelpad = 150)
    plt.ylabel("Number of ages", fontsize = 300, color = 'red', labelpad = 100)
    plt.title("Total ages in the dataset", fontsize = 300, color = 'red')
    
    ax = age_count.plot(kind = 'bar', edgecolor = 'black', linewidth = 30, width =1, color = 'cyan', align = 'center')
    
    plt.ylim(0,100)
    plt.yticks(np.arange(0,105,5))
    plt.xticks(rotation = 0)
    
    for i, v in age_count.reset_index().iterrows():
        ax.text(i-.4, v.Age + 3 , v.Age, color='red', fontsize = 200)
    
    plt.show()
    
    age_count = ds['Age'].value_counts().sort_values(ascending = False)
    
    plt.figure(figsize = (300,100))
    
    plt.rcParams['font.size'] = 200
    plt.xlabel("Age", fontsize = 300, color = 'red', labelpad = 150)
    plt.ylabel("Number of ages", fontsize = 300, color = 'red', labelpad = 100)
    plt.title("Total ages descending order", fontsize = 300, color = 'red')
    
    ax = age_count.plot(kind = 'bar', edgecolor = 'black', linewidth = 30, width =1, color = 'cyan', align = 'center')
    
    plt.ylim(0,100)
    plt.yticks(np.arange(0,105,5))
    plt.xticks(rotation = 0)
    
    for i, v in age_count.reset_index().iterrows():
        ax.text(i-.4, v.Age + 3 , v.Age, color='red', fontsize = 200)
    
    plt.show()
    
    
    
# =============================================================================
# def ChestPains(ds):
#     
#     chest_pains = ds['ChestPainType'].value_counts().sort_index()
#     
#     plt.figure(figsize = (300,100))
#     
#     chest_pains = ds['ChestPainType'].value_counts().sort_values(ascending = False)
#     
#     plt.figure(figsize = (300,100))
#     
#     plt.rcParams['font.size'] = 200
#     plt.xlabel("Age", fontsize = 300, color = 'red', labelpad = 150)
#     plt.ylabel("Number of ages", fontsize = 300, color = 'red', labelpad = 100)
#     plt.title("Total ages descending order", fontsize = 300, color = 'red')
#     
#     ax = chest_pains.plot(kind = 'bar', edgecolor = 'black', linewidth = 30, width =1, color = 'cyan', align = 'center')
#     
#     plt.ylim(0,100)
#     plt.yticks(np.arange(0,105,5))
#     plt.xticks(rotation = 0)
#     
#     for i, v in chest_pains.reset_index().iterrows():
#         ax.text(i-.4, v.ChestPainType + 3 , v.ChestPainType, color='red', fontsize = 200)
#     
#     plt.show()
#
# =============================================================================
    
    
    
SexCount(dataset)
Ages(dataset)  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


