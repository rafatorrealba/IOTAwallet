# change the address for your own address
curl --header "Content-Type: application/json" \
--request POST \
--data '{
"address":"UATGRCZNPJGEJSMEAXOXTJYKXVREPKM9LEUJZAJF9IUJLHAOYGGYQQFCEZBQCBGMRJAWHKZXHNEUIDXIXCX9UCXAID",
"value":10000000,
"message":"EINFACHIOTA",
"tag": "EINFACHIOTA"
}' \
https://faucet.comnet.einfachiota.de/pay_tokens
