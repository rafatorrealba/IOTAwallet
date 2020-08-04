'''
Retreive the balance in iota for all addresses with balances for a given seed
'''

from iota import Iota
import pprint

# This is a demonstration seed, always generate your own seed!
seed1 = 'LSWXWSUSTKLOUHBMHDM9XBPVAHPPTHA9DAKK9XJLQQSNDJCBJCJAVJCRCJZGVRXIQGFCZPMUFQSTHQQNA'
seed2 = 'MCBCJGLSFCGD9A99UEIOJUDBHDCCXKHXTHOVNJLWFKXLIUNUCVWISSFCYOUBFZKVROPJBQUEZGRKXVYBW'
api = Iota('http://localhost:14265', seed2)

print('\nThe balance for your seed:\n')
pprint.pprint(api.get_account_data())
