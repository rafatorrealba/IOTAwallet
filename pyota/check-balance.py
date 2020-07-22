from iota import Iota
import pprint

# This is a demonstration seed, always generate your own seed!

print('Please ingress your iota seed:')
seed = input(str())

print('Please ingress the address of the node:')
api = Iota(input(), seed)


balance = api.get_account_data()
print('The balance for your seed is: ', balance['balance'])
