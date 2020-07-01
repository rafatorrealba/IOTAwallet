from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
 


seed = 'HLXQDU9SBFHEWIAFGGKGZTHJRMDFBWDKEQFZJHFSJZTSJ9ZUDDNDMBHTGVD9BMZLVTGGVERJCZSAITQZW'

monto =  int(input())
api = Iota('https://nodes.devnet.iota.org:443', seed)

# The address to send 1i
address = 'VHFOCLDDYSSKKDRFWQFOWGKIFSQDNKLFMWPKWL9ENU9DFPVDOWCMOVZHUMIKYAEZLKRXRAZMEFELZVWTXESMPHQZWX'


tx = ProposedTransaction(
    address=Address(address),
    message=TryteString.from_unicode('This transaction should include 1i!'),
    tag=Tag('VALUETX'),
    value= monto
)

tx = api.prepare_transfer(transfers=[tx])

result = api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=9)

print('Transaction sent to the tangle!')
print('https://devnet.thetangle.org/address/%s' % address)