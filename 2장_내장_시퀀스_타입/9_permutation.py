def perm(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        for cc in perm(s[i+1:] + s[:i]):
           res.append(c + cc)
    return res

if __name__ == '__main__':
    result = perm("123")
    print(result)