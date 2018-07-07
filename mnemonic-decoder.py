import hashlib

s=['canvas', 'taxi', 'pudding', 'rent', 'exchange', 'remain', 'erosion', 'august', 'engage', 'family', 'bus', 'swamp', 'gown', 'later', 'shoe', 'chaos', 'erode', 'where', 'spring', 'fever', 'mother', 'half', 'enrich', 'blast']
slist=[]
for i in s:
    slist.append([i])

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


#For each word, find index range that could be given based on the first two letters/ index for the last word
def wordIndex(sentence): 
    #Find index of last element
    #https://stackoverflow.com/questions/3961265/get-line-number-of-certain-phrase-in-file-python
    for num, line in enumerate(open('/Users/kaveri/Documents/Internship-code/coding-challenge/python-mnemonic/mnemonic/wordlist/english.txt'),0):
        if sentence[-1][0] in line:
            sentence[-1].append(num) 
    
    #find the list of indexes it could be for each word       
    for i in sentence[0:len(sentence)-1]:
        for num, line in enumerate(open('/Users/kaveri/Documents/Internship-code/coding-challenge/python-mnemonic/mnemonic/wordlist/english.txt'),0):
            if i[0][0:2]==line[0:2]:
                i.append(num)
    return sentence


#https://stackoverflow.com/questions/4233742/permutations-of-a-list-of-lists
def permu(lists):
    def fn(lists, group=[], result=[]):
        if not lists:
            result.append(group)
            return
        first, rest = lists[0], lists[1:]
        for letter in first:
            fn(rest, group + [letter], result)
    result = []
    fn(lists, result=result)
    return result
 
#generate all combinations of word indices  
def findCombos(sentence,checksumBinaryCS):
    #create a list of lists of only the possible index numbers of each word
    sentenceIndices = []
    for i in sentence:
        sentenceIndices.append(i[1:len(i)])
    print ('sentenceIndices',sentenceIndices)

    #cycle through and make a list that has all possible index number combos - all possible 24 words 
    #https://stackoverflow.com/questions/4233742/permutations-of-a-list-of-lists
    if __name__ == '__main__':
        ll = [sentenceIndices]
        newList=[]
        [[newList.append(p) for p in permu(l)] for i,l in enumerate(ll)]
        print(newList)
    #OR just do:
    #sentenceIndexCombos=(list(itertools.product(*sentenceIndices)))
    
#generate a concatenated binary string i.e. ENT out of the index combindation list
def ENTGenerator(indexCombos):
    possibleENTs = []
    for combo in indexCombos:
        binaryNums = []
        for num in combo:
            binaryNums.append(bin(num).lstrip('-0b').zfill(11))
        possibleENTs.append([((''.join(map(str,binaryNums))))])
    return possibleENTs

def hashChecker(possibleENTs,checksum,CSLength,sentence):
    for ENT in possibleENTs:        
        #https://stackoverflow.com/questions/1425493/convert-hex-to-binary
        binaryHash = (bin(int((hashlib.sha224(ENT.encode('utf-8')).hexdigest()), 16))[2:].zfill(256))
        if binaryHash[0:CSLength]==checksum:
            correctIndex = possibleENTs.index(ENT)
    return correctIndex

#creates the final, correct mnemonic given the correct list of indices for the words
def constructMnemonic(correctIndex,indexCombos):
    correctCombo = indexCombos[correctIndex]
    correctMnemonicList=[]
    for i in correctCombo:
        #https://stackoverflow.com/questions/10467913/print-specific-line-in-a-txt-file-in-python
        with open('/Users/kaveri/Documents/Internship-code/test/test-txt.txt') as f:
            for num, line in enumerate(f, 1):
                if num == i:
                    correctMnemonicList.append(str(line).strip('\n'))
    correctMnemonicPhrase=''
    for i in correctMnemonicList:
        correctMnemonicPhrase= correctMnemonicPhrase+i.strip('\'')
    correctMnemonicPhrase=correctMnemonicPhrase.strip('\'')
    return correctMnemonicPhrase
