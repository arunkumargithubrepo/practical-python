# pcost.py
#
# Exercise 1.27
# Total_purchase_value = 0.0
# with open('Data/portfolio.csv', 'rt') as f:
#     for line in f:
#         # print(line)
#         rows  = line.split(',')
#         if rows[1].isnumeric():
#             Total_purchase_value += (int(rows[1]) * float(rows[2]))
#     print('Total amount to purchase portfolio is {0}'.format(Total_purchase_value))

# Exercise 1.28
import gzip
with gzip.open('Data/portfolio.csv.gz', 'rt') as zfile:
    for line in zfile:
        print(line)

