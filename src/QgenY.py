#!/home/dadu/anaconda3/bin python3.6

#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
###############################
QgenY_ascii = """
############################################################

############################################################
                          .-=-.
                         /  ! )\\
                      __ \__/__/
                     / _<( ^.^ )
                    / /   \ c /O
                    \ \_.-./=\.-._     _
                     `-._  `~`    `-,./_<
                         `\' \'\`'----'
                       *   \  . \          *
                            `-~~~\   .
                       .      `-._`-._   *
                             *    `~~~-,      *
                   ()                   * )
                  <^^>             *     (   .
                 .-""-.                    )
      .---.    ."-....-"-._     _...---''`/. '
     ( (`\ \ .'            ``-''    _.-"'`
      \ \ \ : :.   QgenY         .-'
       `\`.\: `:.   Alpha     _.'
       (  .'`.`            _.'
        ``    `-..______.-'
                  ):.  (
                ."-....-".
              .':.        `.
              "-..______..-"
############################################################

############################################################
"""
print (QgenY_ascii)

#Importing Data

interface = pd.read_csv('interface.csv', header=0, names=range(3))
table_names = ["File_type", "Block", "Interface"]
groups = interface[0].isin(table_names).cumsum()
tables = {g.iloc[0,0]: g.iloc[1:] for k,g in interface.groupby(groups)}

#list(tables)

for k,v in tables.items():
    if(k == "File_type"):
        print ("File type: ",v)
    elif(k == "Block"):
        print ("Block Name: ",v)

    

