from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64 , codecs
import Decoding as DC


# Encodes the String 'original'  with ascii table
def ascii_encode(original):
    encodede = [ord(i)for i in original]
    return encodede


# Encodes the String 'original' whith Hex
def hex_encode(original):
    return original.encode().hex()

    
# Encodes the String 'original' with Hex putting '0x' in the start of it 
def Hex_0x_encode(original):
    return hex(bytes_to_long(original.encode()))

# Encodes the String 'original' with base64 
def base64_encode(original):
    return base64.b64encode(original.encode())

# Encodes the String 'original' with rot_13
def rot_13_encode(original):
    return codecs.encode(original,"rot_13")
