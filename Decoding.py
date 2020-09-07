import base64
import codecs

# works with ASCII bytes to make them a letters
def ascii(ords):
    decodede = "".join((chr(o) for o in ords))
    return decodede

# makes hex string into utf-8 strings
def hex_decode(ords):
    return bytes.fromhex(ords).decode('utf-8')

# get hex strings startes in 0x and make them utf-8 stringd
def bigint_decode(ords):
     return bytes.fromhex(ords[2:]).decode('utf-8')

# decode base64 Strings
def base_64_decode(ords):
    message = base64.b64decode(ords) 
    return message.decode('ascii')


# decode Rot_13 Strings
def rot_13_decode(ords):
    return codecs.decode(ords,"rot_13")
