STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


#     """Read in `file` and print out the frequency of words in that file."""
#     pass


def print_word_freq(file):
    with open(file) as f:
        input = f.read()

    # take original text input
    
    print("input")
    print(input)
    # input = 'One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment. His many legs, pitifully thin compared with the size of the rest of him, waved about helplessly as he looked.'
    # makes original text lowercase
    input = input.lower()
    input = input.replace('\n', '')

    
    # list of punctuation
    punc = '"!@#$%^&*()_-<>+=,./'
    
    # removes punctuation
    cleaninput = ''
    
    for char in input:
        if char not in punc:
            cleaninput = cleaninput + char
    cleaninput = cleaninput.split(" ")
    
    # removes stop words
    nostopinputclean = ""
    
    for each in cleaninput:
        if each not in STOP_WORDS:
            nostopinputclean = nostopinputclean + " " + each

    nostopinputclean = nostopinputclean.split(" ")
    nostopinputclean.pop(0)
    print("nostopinputclean: ")
    print(nostopinputclean)

    dictList = ['']

    for each in nostopinputclean:
        if each not in dictList:
            dictList.append(each)

    dictList.pop(0)
    print(dictList)

    dictionary = {}
    for each in dictList:
        dictionary.update({each: 0})

    for each in nostopinputclean:
        dictionary[each] += 1

    print(dictionary)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
    description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

