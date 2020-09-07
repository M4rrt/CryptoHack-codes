from Crypto.Util.number import bytes_to_long
import Decoding as DC
# takes a string and returns it in ascii table
def ascii_encode(original):
    encodede = [ord(i)for i in original]
    return encodede


def hex_encode(original):
    return original.encode().hex()


def Hex_0x_encode(original):
    return hex(bytes_to_long(original.encode()))

