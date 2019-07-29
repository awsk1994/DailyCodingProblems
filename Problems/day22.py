'''
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

def words(words, sentence):
    d = {0: ''}
    for i in range(len(sentence) + 1):
        dd = d.copy()
        for start_index, d_word in d.items():
            word_at_i = sentence[start_index:i]
            if word_at_i in words:
                dd[i] = word_at_i
        d = dd # Need to use a copy because we will be editing d while modifying it otherwise.

    array = []
    i = len(sentence)
    while i > 0:
        if i in d:
            w = d[i]
            array.append(w)
            i -= len(w)
        else:
            return []
    return list(reversed(array))
    
def main():
    print("opt | sentence = {}, words are = {}".format("bedbathandbeyond", words(['bed', 'bath', 'and', 'beyond'], "bedbathandbeyond")))
    print("opt | sentence = {}, words are = {}".format("bedbathandbeyond", words(['bed', 'be', 'dba', 'th', 'bathy', 'and', 'beyond'], "bedbathandbeyond")))
    print("opt | sentence = {}, words are = {}".format("bedbathandbeyond", words(['bed', 'bathy', 'and', 'beyond'], "bedbathandbeyond")))

if __name__ == "__main__":
    main()
