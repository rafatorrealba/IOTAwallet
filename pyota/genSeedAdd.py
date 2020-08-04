from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from iota.crypto.types import Seed

seed = Seed.random()
print('Your seed is' ,seed)

api = Iota('http://localhost:14265', seed)

security_level = 2
address = api.get_new_addresses(index=0, count=1, security_level = security_level)['addresses'][0]

is_spent = api.were_addresses_spent_from([address])['states'][0]

if is_spent:
    print('Address %s is spent!' % address )
else:
    print('Your address is: %s' % address )


