from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from iota.crypto.types import Seed

# This is a demonstration seed, always generate your own seed!
seed1 = 'BLICFZQCUKH9YDPYKXLQFQNTUAEINQSB9NASLCMBQ99ICLQOPZCFFIQRJGXXVSFHKZSO9WLLZAGDUGADX'

seed2 = '9JQCUTFBAMVBSNYIGBAUCCEFABCNNFMMLYIJ9RAXZNSTCKDVSESTGXIXCCUFEGRVHA9YNLITFDZQZUFRW' 

print('sending iota tokens sending iota tokens from wallet1 to wallet2...')

# The address to send  iota tokens, this are address of test you made generate your own address

# address1 = 'QKMQNCSR9BUUIHSEVBFJAANEYJVQVKGMRWZBRPLOHLZ9DUQGTTWMNJCBTDBMDIG99YNXHZ9UQM9ONVFF9'


address = 'OLONXHYDCAWCULZYOILPDGLFRPUGTZLXQBKRHHKHPXGYZZTLYXKHUSFNWBBPNKGVIBUIHQDFYVTBTKWWX'

# the iota node :
api = Iota('http://localhost:14265', seed1)


print('Constructing transfer of 50i...')

tx = ProposedTransaction(
address=Address(address),
value = 50,
message = TryteString.from_unicode('I just sent you 50i, use it wisely!'),
tag=Tag('VALUETX')
)

result = api.send_transfer(transfers=[tx], min_weight_magnitude=10 )

print('Check your transaction on the Tangle!')
print('Bundle: ')
print(result['bundle'].hash)


api1 = Iota('http://localhost:14265', seed1)
api2 = Iota('http://localhost:14265', seed2)


balance1 = api1.get_account_data()
print('The balance of th wallet1 is: ', balance1['balance'])


balance2= api2.get_account_data()

print('The balance of th wallet2 is: ', balance2['balance'])
