from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from iota.crypto.types import Seed

seed1 = 'QWWSFKYVHAQRCWVNAKXQXRICWRIDTYMMCFMHWEVQNAZXLGDPLARMWGZGRCCEOPQXHVBOYFTSOMALIYRNC'
seed2 = 'SPZS9DFXXCOUV99KZKK9XCPWKGWCHCDAMWTRNEDDP9DGWUKZHJUFUOHAGFAXRHITI9MIWAYMNQTUGXCTP'
print('Seed1 is: ' , seed1, 'seed2 is: ', seed1)

api = Iota('http://localhost:14265', seed1)
security_level = 2

address1 = 'KWLFOZIECPQRNZWJPBD9JBKDWYRPBLOXQRTSGVZMJL9JCNUUSPTHIOIKBUAHPFTFPAHGQNTBGOCDDFNPB'
address2 = 'HNWUNBRBKQTRVBDKRCMEXPVATDVO9ZPSNMZLRFDEDCSC9KTZSYEUMQSFUUUKKXRICTKWZLWBLJA9PYMVA'
print('Address1 is: ', address1, 'adress2 is:', address2)

balance = api.get_account_data()
print('The balance for your seed is: ', balance['balance'])

#tx = ProposedTransaction(
#address=Address(address2),
#value = 1000
#)

#result = api.send_transfer(transfers=[tx], min_weight_magnitude=10 )
#print('Bundle: ')
#print(result['bundle'])


