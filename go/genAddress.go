package main

import (
    . "github.com/iotaledger/iota.go/api"
    "github.com/iotaledger/iota.go/trinary"
    "fmt"
)

var node1 = "https://nodes.comnet.thetangle.org:443"
var node2 = "http://localhost:14265"

// The seed that will be used to generate an address
const seed = trinary.Trytes("QWWSFKYVHAQRCWVNAKXQXRICWRIDTYMMCFMHWEVQNAZXLGDPLARMWGZGRCCEOPQXHVBOYFTSOMALIYRNC")

// Define the security level of the address
const securityLevel = 2

func main() {
    // Connect to a node
    api, err := ComposeAPI(HTTPClientSettings{URI: node1})
    must(err)
    
    // Generate an unspent address with security level 2
    // If this address is spent, this method returns the next unspent address with the lowest index
    addresses, err := api.GetNewAddress(seed, GetNewAddressOptions{Security:securityLevel})
    must(err)

    fmt.Println("\nYour address is: ", addresses[0])
}

func must(err error) {
    if err != nil {
        panic(err)
    }
}
