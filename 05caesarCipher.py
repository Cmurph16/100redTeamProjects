import sys

# function to apply caesar shift
def encode(suppliedInp):
    encodedVal = []
    for letter in suppliedInp:
        # skipping spaces because it just makes a lot of #'s
        if letter == ' ':
            continue
        # adds shift value (default shift = 3) to number value of letter and switces back to letter
        encodedVal.append(chr(ord(letter)+3))
    # return string of the shifted array
    return ''.join(encodedVal)

def decode(message):
    decodedVal = []
    for letter in message:
        # remove the shift value from the unicode number with the letter
        decodedVal.append(chr(ord(letter)-3))
    # return string of the unshifted array
    return ''.join(decodedVal)

def main():
    # if no encode or decode flag sent in
    if (len(sys.argv)<2):
        print('Need to supply an e or d flag to either (e)ncode or (d)ecode')
        sys.exit(0)
    # if the first argument isn't an encode or decode flag
    if (sys.argv[1].lower() != 'e' and sys.argv[1].lower() != 'd'):
        print('The first argument needs to be either an e or d flag to either (e)ncode or (d)ecode')
        sys.exit(0)
    # encode loop
    if (sys.argv[1].lower() == 'e'):
        if (len(sys.argv)>2):
            # passed in message with cli
            caesar = encode(sys.argv[2])
        else:
            # no message passed in. Prompting user
            suppliedInp = input("Message to encode: ")
            caesar = encode(suppliedInp)
        print('Caesar encoding: {}'.format(caesar))
    else:
        # decode loop
        if((len(sys.argv)>2)):
            # passed in message with cli
            decodedMes = decode(sys.argv[2])
        else:
            # no message passed in. Prompting user
            suppliedInp = input("Message to decode: ")
            decodedMes = decode(suppliedInp)
        print('Decoded message: {}'.format(decodedMes))

# default script stuff
if __name__ == '__main__':
    main()