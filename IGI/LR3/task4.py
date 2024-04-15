def task4() -> str:
    """
    a) Count the words in string
    b) Find the longest word and its number
    :return: String without even words
    """
    mystring = input("Enter string to check words\n")
    words = mystring.split()
    ans_string = ""
    print(f"Words count: {len(words)}")
    max_index, max_word = max(enumerate(words), key=lambda x: x[1])
    for i, word in enumerate(words):
        if i % 2 == 1:
            ans_string += word + ' '

    return ans_string
