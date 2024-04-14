def task3():
    """
    We count all yous words in string which started with small letter (a..z)
    :return: Count of words
    """
    mystring = input("Enter string to check\n")
    words = mystring.split()
    cnt = 0
    for word in words:
        cnt += int(word[0].islower())
    return cnt
