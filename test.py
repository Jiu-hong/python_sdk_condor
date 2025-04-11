import base64
import binascii


def hex_to_ec_pem(hex_string):
    """
    Convert a hex string private key to EC PEM format

    Args:
        hex_string (str): The private key in hex string format

    Returns:
        str: PEM formatted EC private key
    """
    try:
        # Convert hex string to bytes
        private_key_bytes = binascii.unhexlify(hex_string)

        # Create ASN.1 structure for EC private key
        asn1_sequence = (
            b'\x30\x2e' +  # SEQUENCE, length 46
            b'\x02\x01\x01' +  # INTEGER (1)
            b'\x04\x20' + private_key_bytes +  # OCTET STRING (32 bytes)
            b'\xa0\x07' +  # [0]
            b'\x06\x05' +  # OBJECT IDENTIFIER
            b'\x2b\x81\x04\x00\x0a'  # secp256k1 OID
        )

        # Convert to base64
        b64_data = base64.b64encode(asn1_sequence).decode('ascii')

        # Format PEM
        pem = f"-----BEGIN EC PRIVATE KEY-----\n{b64_data}\n-----END EC PRIVATE KEY-----"
        return pem

    except Exception as e:
        raise Exception(f"Error converting hex to PEM: {str(e)}")


hex_private_key = "85f45a4fe1f86bc4f11900465e2a669f89e04c758631bf6428bb995a2fdfbb5e"
# Example usage
# if __name__ == "__main__":
#     # Your hex string private key
#     hex_private_key = "85f45a4fe1f86bc4f11900465e2a669f89e04c758631bf6428bb995a2fdfbb5e"

#     try:
#         pem_data = hex_to_ec_pem(hex_private_key)
#         print("Generated PEM format:")
#         print(pem_data)

#     except Exception as e:
#         print(f"Error: {str(e)}")


private_key_bytes = binascii.unhexlify(hex_private_key)

print("pk_bytes1:", private_key_bytes)
print("pk_bytes2:", bytes.fromhex(hex_private_key))
