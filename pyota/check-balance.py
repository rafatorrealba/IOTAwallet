'''
Retreive the balance in iota for all addresses with balances for a given seed
'''

from iota import Iota
import pprint

# This is a demonstration seed, always generate your own seed!
seed1 = 'KVFRCVGIZLALCU9WSITGHCQVUZVJQSXSMZGZUBSLMKCFWZONWTHDMBNQUFBS9LPUTHTRBNRTIYXNJY'
seed2 = 'VVXIFPXCUMBVZGZPHGWQPVAOAICHHILKUKOYEYTHWKWUPSJLKNWKXYJHOTQDUX9FLC9KXMEQTPRVBZ'

api = Iota('http://localhost:14265', seed2)

print('\nThe balance for your seed:\n')
pprint.pprint(api.get_account_data())
