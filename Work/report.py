# report.py
#
# Exercise 2.4 append tuple to list
import csv
#
#
# def portfolio_details(filename):
#     portfolio = []
#     with open(filename, "rt") as f:
#         rows = csv.reader(f)
#         header = next(rows)
#         for row in rows:
#             holding = (row[0], int(row[1]), float(row[2]))
#             portfolio.append(holding)
#     return portfolio
#
#
# portfolio = portfolio_details("Data/portfolio.csv")
# total = 0
# for name, shares, price in portfolio:
#     total += shares * price
#
# print("total = {0}".format(total))
######################################################################################
# append dictionary to list
# import csv
#
#
# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         header = next(rows)
#         for row in rows:
#             holding = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
#             portfolio.append(holding)
#     return portfolio
#
#
# print(read_portfolio("Data/portfolio.csv"))
#
# portfolio = read_portfolio("Data/portfolio.csv")
# total_cost = 0
# for share in portfolio:
#     total_cost += share['shares'] * share['price']
#     print("Share Name: {0}\t\t No. of Shares: {1}\t\tPrice: {2}".format(share['name'],share['shares'],share['price']))
#
# print("total cost of shares = {0}".format(total_cost))

######################################################################################
# add csv data to dictionary
import csv


def read_prices(filename):
    share = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                share[row[0]] = row[1]
    return share

f = read_prices("Data/prices.csv")
# To get the corresponding key of a value
print(list(f.keys())[list(f.values()).index('51.94')])