import sys

filename = sys.argv[1]
count = 0
csv_file_name = '../Dataset/titles.csv'

file = open(filename, 'r', errors='ignore')
csv_file = open(csv_file_name, 'w+', errors='ignore')
new_line = ''

for line in file:
    if(count < 7):
        count = count + 1
        continue
    if(line == '\n'):
        continue
    
    label = line.partition(':')[0]

    if(label == 'ASIN'):
        line = line.replace(' ', '')
        line = line.split(':')
        asin = line[1].split('\n')
        asin = asin[0]
        #print("ASIN: " + str(asin))
        new_line = new_line + asin + ','

    if(label == '  title'):
        line = line.replace('  title: ', '')
        title = line.split('\n')
        title = title[0]
        #print("TID: " + str(tid) + " ")
        new_line = new_line + title + ','
    
    if('discontinued product' in line):
        new_line = ''
        continue
    
    if(label == '  group'):
        line = line.replace('  group: ', '')
        group = line.split('\n')
        group = group[0]
        #print("TID: " + str(tid) + " ")
        new_line = new_line + group + ','

    if(label == '  salesrank'):
        line = line.replace('  salesrank: ', '')
        salesrank = line.split('\n')
        salesrank = salesrank[0]
        #print("TID: " + str(tid) + " ")
        new_line = new_line + salesrank
        csv_file.write(new_line + '\n')
        new_line = ''

