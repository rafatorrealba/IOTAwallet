from iota import Iota
import pprint

# This is a demonstration seed, always generate your own seed!
seed = input(str())

api = Iota(input(), seed)


balance = api.get_account_data()
print('The balance for your seed is: ', balance['balance'])
