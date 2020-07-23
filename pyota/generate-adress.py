from iota import Iota

# This is a demonstration seed, always generate your own seed!

print('seed':)
seed = input()

print('iota-node:')

api = Iota(input(), seed)

# We want the first address for this seed (index 0), make sure it hasn't been spent from before!
addresses = api.get_new_addresses(index=0, count=1, security_level=2, checksum=True)

address = addresses['addresses'][0]

print('\nThe first available address for your seed: %s' % address)
print('Go to https://faucet.comnet.einfachiota.de/#/ and paste this address here to receive devnet tokens now\n\n')

