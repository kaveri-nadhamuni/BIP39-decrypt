#find checksum
def getChecksum(sentence):
    ENTLength= int(len(slist)*11*32/33)
    CSLength = int(ENTLength/32)
    for num, line in enumerate(open('/Users/kaveri/Documents/Internship-code/coding-challenge/python-mnemonic/mnemonic/wordlist/english.txt'),0):
        if sentence[-1][0] in line:
            lastWordDecimal=num
    #create a 11-bit integer which corresponds to the last word
    lastWordBinary= bin(lastWordDecimal).lstrip('-0b').zfill(11)
    
    #extract the last CSlength digits of the 11-bit integer = checksum
    checksum=lastWordBinary[(len(lastWordBinary)-CSLength):(len(lastWordBinary))]
    
    #print (ENTLength, CSLength,checksumBinaryCSLength,lastWordBinary)
    return ENTLength, CSLength,checksum,lastWordBinary
