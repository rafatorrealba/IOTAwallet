'''
This example just checks the basic functioning of the API and
prints out the node information of the node you are connected to.
'''

from iota import Iota
import pprint

api = Iota('http://localhost:14265') 

# Using pprint instead of print for a nicer looking result in the console
pprint.pprint(api.get_node_info())
