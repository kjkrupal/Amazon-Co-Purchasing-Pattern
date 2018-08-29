import sys

filename = sys.argv[1]
count = 0
reviews_file_name = '../Dataset/reviews.csv'
reviews_meta_file_name = '../Dataset/reviews-meta.csv'

file = open(filename, 'r', errors='ignore')
reviews_file = open(reviews_file_name, 'w+', errors='ignore')
reviews_meta_file = open(reviews_meta_file_name, 'w+', errors='ignore')

reviews_file.write('asin,date,customer_id,rating,votes,helpful\n')
reviews_meta_file.write('asin,total,downloaded,avg_rating\n')

new_line = ''
asin_val = 0
review_flag = False

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
        asin_val = asin
        new_line = new_line + asin + ','
    
    if('discontinued product' in line):
        new_line = ''
        continue

    if(label == '  reviews'):
        line = line.replace('  reviews: total: ', '')
        line = line.replace(' downloaded: ', '')
        line = line.replace(' avg rating: ', '')
        line = line.split(' ')
        total = line[0]
        downloaded = int(line[1])
        avg_rating = line[2]

        for i in range(0, downloaded):
            review_line = next(file)
            review_line = review_line.replace('cutomer:', ',')
            review_line = review_line.replace('rating:', ',')
            review_line = review_line.replace('votes:', ',')
            review_line = review_line.replace('helpful:', ',')
            review_line = review_line.split(',')
            item_line = asin_val + ','
            for items in review_line:
                items = items.replace(' ', '')
                item_line = item_line + items + ','
            
            reviews_file.write(item_line[:-1])
        
        reviews_meta_file.write(asin_val + ',' + total + ',' + str(downloaded) + ',' + avg_rating)
