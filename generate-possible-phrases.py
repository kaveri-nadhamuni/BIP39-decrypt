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
