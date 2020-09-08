from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64 , codecs
import Decoding as DC


# encode a string to ascii table
def ascii_encode(original):
    encodede = [ord(i)for i in original]
    return encodede


# encode a string into a Hex string
def hex_encode(original):
    return original.encode().hex()

    
# encode the string into a Hex string with 0x in the start of it 
def Hex_0x_encode(original):
    return hex(bytes_to_long(original.encode()))

# encode a string into base64 
def base64_encode(original):
    return base64.b64encode(original.encode())

# takes a string and encode it in rot_13
def rot_13_encode(original):
    return codecs.encode(original,"rot_13")
