def reversing_words_slice(word):
    new_word = []
    words = word.split(' ')
    for word in words[::-1]:
        new_word.append(word)
    return ' '.join(new_word)


if __name__ == '__main__':
    str1 = "Buffy is a Vampire Slayer"
    str2 = reversing_words(str1)
    print(str2)