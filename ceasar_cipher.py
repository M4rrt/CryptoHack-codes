# encode a stings with ceasar cipher using a key to rotation between -26 and 26
# word   : String - the word to be enceded
# string : Int    - number between -26 and 26
def caesar_cipher_r(word, n):
    def verification(i,n,vi,vf):
        letter = ''
        if (ord(i)+n) > vf:
                x = (ord(i) + n) - (vf+1)
                letter += chr(vi + x)
        elif(ord(i) + n) < vi :
                x = vi - (ord(i) + n)
                letter += chr(vf+1 - x)
        else:
            letter += chr(ord(i) + n)
        return letter 
    
    letter = ''

    for i in word:
        if i.islower():
            letter += verification(i,n,97,122)

        elif i.isupper():
            letter += verification(i,n,65,90)

        elif i == ' ':
            letter+= ' '

    return letter