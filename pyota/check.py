import pprint
from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from iota.crypto.types import Seed

node1 = 'https://nodes.comnet.thetangle.org:443'
node2 = 'http://localhost:14265'

seed = 'JMQGUNIURZVUMFORRZKY9S9XBSRLUPDO9EMDDQVNXSTBSTVJIGTGVXPIHGTFNKLJZCPRUJOKHAPFIDKFE'
print('Seed:' , seed)

api = Iota(node2, seed)
security_level = 2
balance = api.get_account_data()
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(balance)
#print('The balance of seed is:', balance['balance'])
