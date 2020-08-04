from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from iota.crypto.types import Seed

# This is a demonstration seed, always generate your own seed!
seed1 = 'LSWXWSUSTKLOUHBMHDM9XBPVAHPPTHA9DAKK9XJLQQSNDJCBJCJAVJCRCJZGVRXIQGFCZPMUFQSTHQQNA'
seed2 = 'MCBCJGLSFCGD9A99UEIOJUDBHDCCXKHXTHOVNJLWFKXLIUNUCVWISSFCYOUBFZKVROPJBQUEZGRKXVYBW' 

print('sending iota tokens sending iota tokens from wallet1:', seed1, 'to', 'wallet2:', seed2)

# The address to send  iota tokens, this are address of test you made generate your own address

address1 = 'GPSGMJSOOFIGWBPKVPFIUPPLRQCVXFHSZA9PLFHJWBMEUNPFNOEVQSJPZOMPQYR9YTHXGSWZQOVPNXJHC'
address2 = 'MQTQGWVKOMWDXANTQHXMTUNYAHWUYMWARXXWYDDCJC9WRRHNJDRTKKQMMWIPOEIEWWXSBGVTSKJEGRZND'

# the iota node :
api = Iota('http://localhost:14265', seed1)


tx = ProposedTransaction(
address=Address(address2),
value = 10
)

result = api.send_transfer(transfers=[tx], min_weight_magnitude=10 )
print('Bundle: ')
print(result['bundle'])


