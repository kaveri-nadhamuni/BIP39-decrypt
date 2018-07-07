#generate a concatenated binary string i.e. ENT out of the index combindation list
def ENTGenerator(indexCombos):
    possibleENTs = []
    for combo in indexCombos:
        binaryNums = []
        for num in combo:
            binaryNums.append(bin(num).lstrip('-0b').zfill(11))
        possibleENTs.append([((''.join(map(str,binaryNums))))])
    return possibleENTs
