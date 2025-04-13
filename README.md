This is python sdk for casper 2.0.

### clvalue examples:


clmap

```
value = CLMap({CLU8(3): CLOption(CLString("Jim"))})

empty_value = CLMap({}, {CLOption(CLU32(NoneHolder())): CLString(NoneHolder())})
```

cllist

```
value = CLList([CLOption(CLString("hello")), CLOption(CLString("world"))])
empty_value = CLList([], CLList([CLBool(NoneHolder())]))
```

cloption:
```
value = CLOption(CLString("hello"))
empty_value = CLOption(CLString(NoneHolder()))
```

clresult:
```
ok_result = CLResult(
    Ok(CLOption(CLTuple2((CLString("hello"), CLU64(123))))),
    Err(CLU32(NoneHolder())),
    True
)

err_result = CLResult(
    Ok(CLU32(NoneHolder())),
    Err(CLOption(CLTuple2((CLString("hello"), CLU64(123))))),
    False
)
```

cltuple3
```
value = CLTuple3((
            CLString("hello"),
            CLBool(True),
            CLURef(
                "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007")
        ))

empty_value = CLTuple3((
            CLString(NoneHolder()),
            CLBool(NoneHolder()),
            CLURef(NoneHolder())
        ))
```

### put_transaction
[examples](./examples/put_transaction/)

### put_deploy
[examples](./examples/put_deploy/)