from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString

api = Iota(input(), testnet = True) 
address = 'ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9VEERIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDXNYVAPLZAW'

message = TryteString.from_unicode('Hola')

tx = ProposedTransaction(
address = Address(address),
message = message,
value = 0
)

result = api.send_transfer(transfers = [tx])

print(result['bundle'].tail_transaction.hash)
