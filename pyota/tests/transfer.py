from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from iota.crypto.types import Seed

node1 = 'https://nodes.comnet.thetangle.org:443'
node2 = 'http://localhost:14265'

seed1 = 'QVZCNIFLUY9GXPGKLY9VTFPFS9PLTFAUQDOHNLVRYJONGAX9TPDXDEJ9OXFR9RRKGFUJNXOJUAATRKNTX'
seed2 = 'TSGVUYISRDCWWOWTIQKPTEUELXKFPCSITBJDCYVLN9LSUYGLWGRGDRJX9SEWIOPXKFUEOXYAXUPPCQFYX'
print('Seed 1 is:' , seed1)
print('Seed 2 is:' , seed2, '\n')

address1 = 'QVZCNIFLUY9GXPGKLY9VTFPFS9PLTFAUQDOHNLVRYJONGAX9TPDXDEJ9OXFR9RRKGFUJNXOJUAATRKNTX'
address2 = 'TSGVUYISRDCWWOWTIQKPTEUELXKFPCSITBJDCYVLN9LSUYGLWGRGDRJX9SEWIOPXKFUEOXYAXUPPCQFYX'
print('Address 1 is:' , address1)
print('Address 2 is:' , address2, '\n')

api = Iota(node1, seed1)
security_level = 2

balance = api.get_account_data()
print('The balance of seed1 is: ', balance['balance'])

tx = ProposedTransaction(
address=Address(address2),
value = 500)

result = api.send_transfer(transfers=[tx], min_weight_magnitude=10 )
print('Bundle: ')
print(result['bundle'].hash)
