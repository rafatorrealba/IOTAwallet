'''
Retreive the balance in iota for all addresses with balances for a given seed
'''

from iota import Iota
import pprint

# This is a demonstration seed, always generate your own seed!
seed1 = 'BLICFZQCUKH9YDPYKXLQFQNTUAEINQSB9NASLCMBQ99ICLQOPZCFFIQRJGXXVSFHKZSO9WLLZAGDUGADX'
seed2 = '9JQCUTFBAMVBSNYIGBAUCCEFABCNNFMMLYIJ9RAXZNSTCKDVSESTGXIXCCUFEGRVHA9YNLITFDZQZUFRW'

api1 = Iota('http://localhost:14265', seed1)
api2 = Iota('http://localhost:14265', seed2)


balance1 = api1.get_account_data()
print('The balance of th wallet1 is: ', balance1['balance'])


balance2= api2.get_account_data()

print('The balance of th wallet2 is: ', balance2['balance'])
