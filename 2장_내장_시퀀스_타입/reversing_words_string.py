# EXAMPLE NUMBER 1
def reverser(string1, p1=0, p2=None):
    if len(string1) < 2:
        return string1
    p2 = p2 or len(string1)-1
    while p1 < p2:
        aux = string1[p1]
        string1[p1] = string1[p2]
        string1[p2] = aux
        p1 += 1
        p2 -= 1

def reversing_words_setence_logic(string1):
    reverser(string1)
    p = 0
    start = 0
    final = []
    while p < len(string1):
        if string1[p] == u"\u0020":
            reverser(string1,start,p-1)
            start = p+1
        p += 1
    reverser(string1,start,p-1)

    return "".join(string1)

# EXAMPLE NUMBER 2 AND 3 USING PYTHON AWESOMESAUCE
def reversing_words_setence_py(str1):
    ''' reverse the words in a sentence'''
    words = str1.split()
    rev_set = " ".join(reversed(words))
    return rev_set

def reversing_words_setence_py2(str1):
    """
    Reverse the order of the words in a sentence.
    :param string: the string which words will be reversed.
    :return: the reversed string.
    """
    words = str1.split(' ')
    words.reverse()
    return ' '.join(words)

# EXAMPLE 4, VERY SILLY, USING BRUTE FORCE
def reverse_words_brute(string):
    """
    Reverse the order of the words in a sentence.
    :param string: the string which words will be reversed.
    :return: the reversed string.
    """
    word, sentence = [], []
    for character in string:
        if character != ' ':
            word.append(character)
        else:
            # So we do not keep multiple whitespaces. An empty list evaluates to False.
            if word:
                sentence.append(''.join(word))
            word = []
    # So we do not keep multiple whitespaces. An empty list evaluates to False.
    if word != '':
        sentence.append(''.join(word))
    sentence.reverse()
    return ' '.join(sentence)

# TESTS
def test_reversing_words_sentence():
    str1 = "Buffy is a Vampire Slayer"
    assert(reversing_words_setence_py(str1) == "Slayer Vampire a is Buffy")
    assert(reversing_words_setence_py2(str1) == "Slayer Vampire a is Buffy")
    assert(reverse_words_brute(str1) == "Slayer Vampire a is Buffy")
    assert(reversing_words_setence_logic(list(str1)) == "Slayer Vampire a is Buffy")

    print("Tests passed!")


if __name__ == '__main__':
    test_reversing_words_sentence()

