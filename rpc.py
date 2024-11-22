import requests

url = 'https://rpc.testnet.casperlabs.io/rpc'
myobj = {
    "id": -573285493134384228,
    "jsonrpc": "2.0",
    "method": "account_put_deploy",
    "params": {
        "deploy": {
            "hash": "c4a579064ee5eabea8e4c924ca4e92a3bcd613da7bfa0dc28ca0396e46dd8d70",
            "header": {
                "account": "010068920746ecf5870e18911ee1fc5db975e0e97fffcbbf52f5045ad6c9838d2f",
                "timestamp": "2024-11-21T10:25:45.403Z",
                "ttl": "1h",
                "gas_price": 1,
                "body_hash": "631864c2d24f18ab302d58382e662513c73eef617179664cbc1be1789eb665ad",
                "dependencies": [],
                "chain_name": "casper-test"
            },
            "payment": {
                "ModuleBytes": {
                    "module_bytes": "",
                    "args": [
                        [
                            "amount",
                            {
                                "cl_type": "U512",
                                "bytes": "0400ca9a3b",
                                "parsed": "1000000000"
                            }
                        ]
                    ]
                }
            },
            "session": {
                "StoredContractByHash": {
                    "hash": "16def1f26e22235bfb8d58fa1fcea580a9f1eba68706a7d88bee1c659006a01d",
                    "entry_point": "store_key",
                    "args": [
                        [
                            "recipient",
                            {
                                "cl_type": "Key",
                                "bytes": "00d9758b25962f4cba82ba0047389af97a70acb7df43b391f9ffb293801bea5061",
                                "parsed": {
                                    "Account": "account-hash-d9758b25962f4cba82ba0047389af97a70acb7df43b391f9ffb293801bea5061"
                                }
                            }
                        ],
                        [
                            "token_ids",
                            {
                                "cl_type": {
                                    "Option": {
                                        "List": "String"
                                    }
                                },
                                "bytes": "0101000000060000006f72616e6765",
                                "parsed": [
                                    "orange"
                                ]
                            }
                        ],
                        [
                            "token_metas",
                            {
                                "cl_type": {
                                    "List": {
                                        "Map": {
                                            "key": "String",
                                            "value": "String"
                                        }
                                    }
                                },
                                "bytes": "01000000010000000300000069636505000000637265616d",
                                "parsed": [
                                    [
                                        {
                                            "key": "ice",
                                            "value": "cream"
                                        }
                                    ]
                                ]
                            }
                        ],
                        [
                            "token_commissions",
                            {
                                "cl_type": {
                                    "List": {
                                        "Map": {
                                            "key": "String",
                                            "value": "String"
                                        }
                                    }
                                },
                                "bytes": "01000000010000000300000069636505000000637265616d",
                                "parsed": [
                                    [
                                        {
                                            "key": "ice",
                                            "value": "cream"
                                        }
                                    ]
                                ]
                            }
                        ]
                    ]
                }
            },
            "approvals": [
                {
                    "signer": "010068920746ecf5870e18911ee1fc5db975e0e97fffcbbf52f5045ad6c9838d2f",
                    "signature": "0117df7ed7fde546548a60f77730ebeb9181fa59d1a8e93b5e29ff1c373719f3b2b9aa289d4d049ea7596413d75998eb874f4166df663ae6fe76e12d9aa816b007"
                }
            ]
        }
    }
}

x = requests.post(url, json=myobj)
print(x.text)
