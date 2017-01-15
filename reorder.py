# algo taken from http://stackoverflow.com/questions/33001490/python-re-ordering-columns-in-a-csv
# accessed at 4pm on 11/19/2016
import csv

with open('data_combiner.csv', 'r') as infile, open('data_ordered.csv', 'a') as outfile:
    order = ['', 'year', 'name','team_id', 'franchise_id', 'win_percent', 'w', 'g', 'ab', 'bb', 'e', 
            'er','era', 'fp','h', 'ha', 'hr', 'hra','r', 'ra', 'run_diff', 'so', 'soa', 'double', 
            'triple', 'ws_win']
    writer = csv.DictWriter(outfile, fieldnames = order)
    writer.writeheader()
    for row in csv.DictReader(infile):
        writer.writerow(row)
