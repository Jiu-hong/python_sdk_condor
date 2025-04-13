# Python SDK for Casper 2.0

A Python Software Development Kit (SDK) for interacting with the Casper 2.0 blockchain network.

## Overview

This SDK provides a comprehensive set of tools and utilities for developing applications on the Casper blockchain. It includes support for various CL (Casper) value types, transaction handling, and deployment management.

## Features

- CL Value Type Support
- Transaction Management
- Deploy Operations
- Comprehensive Testing Suite


## Usage Examples

### CL Value Types

#### CLMap
```python
# Create a map with a key-value pair
value = CLMap({CLU8(3): CLOption(CLString("Jim"))})

# Create an empty map with type information
empty_value = CLMap({}, {CLOption(CLU32(NoneHolder())): CLString(NoneHolder())})
```

#### CLList
```python
# Create a list of optional strings
value = CLList([CLOption(CLString("hello")), CLOption(CLString("world"))])

# Create an empty list with type information
empty_value = CLList([], CLList([CLBool(NoneHolder())]))
```

#### CLOption
```python
# Create an optional string
value = CLOption(CLString("hello"))

# Create an empty option with type information
empty_value = CLOption(CLString(NoneHolder()))
```

#### CLResult
```python
# Create a successful result
ok_result = CLResult(
    Ok(CLOption(CLTuple2((CLString("hello"), CLU64(123))))),
    Err(CLU32(NoneHolder())),
    True
)

# Create an error result
err_result = CLResult(
    Ok(CLU32(NoneHolder())),
    Err(CLOption(CLTuple2((CLString("hello"), CLU64(123))))),
    False
)
```

#### CLTuple3
```python
# Create a tuple with three values
value = CLTuple3((
    CLString("hello"),
    CLBool(True),
    CLURef("uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007")
))
```

### Transaction Operations

For detailed examples of transaction operations, see the [transaction examples](./examples/put_transaction/).

### Deploy Operations

For detailed examples of deploy operations, see the [deploy examples](./examples/put_deploy/).

## Testing

The SDK includes a comprehensive test suite covering all CL value types and operations. Run the tests using:

```bash
python -m pytest packages/tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
