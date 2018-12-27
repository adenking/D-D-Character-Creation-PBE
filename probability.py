'''
credit to https://www.patreon.com/pakstrax for the PDF
https://www.reddit.com/r/dndnext/comments/9e52vk/300_ways_to_roll_for_stats_from_up_to_op/
this is a calculator for dice rolls not on this list
use anydice to get a csv chart with your desired roll and put it in a csv and then run this
https://anydice.com/
'''
import csv
total = 0
with open('PBE.csv') as pbefile:
    pbereader = csv.reader(pbefile)
    pbedict = {rows[0]: rows[1] for rows in pbereader}

with open('probability.csv') as csvfile:
    probreader = csv.reader(csvfile, delimiter=",", quotechar='|')
    for row in probreader:
        total += float(pbedict[row[0]])*(float(row[1])/100)


print(f'Total: {total*6/27}')
