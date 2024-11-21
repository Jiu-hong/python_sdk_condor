with open("contract/cep18.wasm", mode='rb') as file:  # b is important -> binary
    fileContent = file.read()

print(fileContent.hex())
