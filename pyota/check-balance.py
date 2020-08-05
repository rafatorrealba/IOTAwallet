'''
Retreive the balance in iota for all addresses with balances for a given seed
'''

from iota import Iota
import pprint

# This is a demonstration seed, always generate your own seed!
seed1 = 'PKJLCEGBFVJMFKNPIWJE9TT9BYTBMRGVPFAKLHWYBXJQHYKZHEFYSSARDRJGQSSEAACGARFGEGBQXI9MT'
seed2 = 'DMSGOXLIHJESEOOP9LLPVXVGUTCV9JZZMSAYYXUFMG9GBGQIJEESVAEFXRC9EAOPL9UCUQOEKVLUBJJRS'

api = Iota('http://localhost:14265', seed2)

print('\nThe balance for your seed:\n')
pprint.pprint(api.get_account_data())
