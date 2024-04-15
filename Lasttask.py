def myfunc(s):
    result = ''
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].lower()
        else:
            result += s[i].upper()
    return result(s)