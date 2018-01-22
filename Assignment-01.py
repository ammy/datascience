#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 17:40:43 2018

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
        
