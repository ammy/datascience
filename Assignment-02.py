#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:11:00 2018

@author: Manish Parihar
"""

import csv
from collections import defaultdict
 
zweitstimmenGruppe = defaultdict(float)

# open csv file 
with open("ergebnisse.csv", encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        try:
            # Add value of "zweitstimmen" with the key of "gruppe"
            if row[2] == "DIE LINKE.":
                zweitstimmenGruppe["DIE LINKE"] += float(row[4])
            elif row[2] == "GRÜNE/B 90":
                zweitstimmenGruppe["GRÜNE"] += float(row[4])
            else:
                zweitstimmenGruppe[row[2]] += float(row[4])
        except ValueError:
            pass 
            # do nothing

gultige_object = zweitstimmenGruppe["Gültige"]
 # remove non-party from the list
zweitstimmenGruppe.pop("Gültige")
zweitstimmenGruppe.pop("Ungültige")

# define datatype for storing key/value pairs of party (Gruppe)
partyPercentage = defaultdict(float) 

# Calculate percentage 
for k in zweitstimmenGruppe:
    if zweitstimmenGruppe[k] > 0:
        percentage = zweitstimmenGruppe[k]/gultige_object
        partyPercentage[k] = percentage
        print (k + ";" + str(round(percentage*100,1)) + "%")
        

### merge every party below 5% ###

sonstige = 0.0
sonstigeGruppen = list();

# sum of all the results of groups of all below than 5%
for k in partyPercentage:
    if partyPercentage[k]<0.05:
        sonstige += partyPercentage[k]
        sonstigeGruppen.append(k)

# remove groups below 5% from dictionary
for i in sonstigeGruppen:
    partyPercentage.pop(i)
    
# add sonstige to dictionary
partyPercentage["Sonstige"] = sonstige

# Result of the dictionary
for k in partyPercentage:
    print (k + ";" + str(round(partyPercentage[k]*100,1)) + "%")

#%%

### Plot bar chart with party data ###

import matplotlib.pyplot as plt

# Color Code
colors = defaultdict()
colors["AfD"] = '#FADBD8'   # Light Red
colors["GRÜNE"] = '#48C9B0' # Light Green
colors["CDU"] = '#85C1E9'   # Light Blue
colors["DIE LINKE"] = '#E59866' # Light Orange
colors["CSU"] = '#D2B4DE' # Light Purple
colors["FDP"] = '#F1C40F'   # Light Yellow
colors["SPD"] = '#BDC3C7'   # Light Grey
colors["Sonstige"] = '#FAE5D3' # Ultra Light Orange

x=[]
y=[]
c=[]
for i in partyPercentage.items():    
    x.append(i[0])
    y.append(i[1])
    c.append(colors[i[0]])

barchart = plt.bar(x,y, color=c)

# display the numeric values on top of the bar
for a,b in zip(x, y): 
    plt.text( a, b, str(round(b*100,1)) )
    plt.title("Federal Election 2017: Second Vote Result")
    plt.show()
