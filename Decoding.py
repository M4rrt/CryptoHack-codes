import base64
import codecs

# Decode the 'encoded' ASCII string
def ascii_decode(encoded):
    decoded = "".join((chr(o) for o in encoded))
    return decoded

# Decode the 'encoded' hex string
def hex_decode(encoded):
    return bytes.fromhex(encoded).decode('utf-8')

# Decode the 'encoded' hex string started with '0x'
def hex_0x_decode(encoded):
     return bytes.fromhex(encoded[2:]).decode('utf-8')

# Decode the 'encoded' base64 string
def base64_decode(encoded):
    decoded = base64.b64decode(encoded) 
    return decoded.decode('ascii')


# Decode the 'encoded' Rot_13 string
def rot_13_decode(encoded):
    return codecs.decode(encoded,"rot_13")
