import sys

filename = sys.argv[1]
count = 0
csv_file_name = '../Dataset/sample-itemset.csv'

file = open(filename, 'r')
csv_file = open(csv_file_name, 'w+')
new_line = ''

for line in file:
    if(count < 7):
        count = count + 1
        continue
    if(line == '\n'):
        continue
    
    label = line.partition(':')[0]

    if(label == 'Id'):
        line = line.replace(' ', '')
        line = line.split(':')
        tid = line[1].split('\n')
        tid = tid[0]
        #print("TID: " + str(tid) + " ")
        new_line = new_line + tid + ','
    
    if('discontinued product' in line):
        new_line = ''
        continue

    if(label == 'ASIN'):
        line = line.replace(' ', '')
        line = line.split(':')
        asin = line[1].split('\n')
        asin = asin[0]
        #print("ASIN: " + str(asin))
        new_line = new_line + asin + ','

    if(label == '  similar'):
        line = line.split(':')
        line = line[1].replace('  ', ',')
        line = line.split('\n')
        line = line[0].replace(' ', '')
        line = line.split(',')
        for i in range(0, len(line)):
            if(i == 0):
                continue
            new_line = new_line + line[i] + ','
        csv_file.write(new_line[:-1] + '\n')
        new_line = ''
            

