def reverse(x):
    #if -(2**31-1)< x <(2**31-1):
    if x >0:
        t = int(str(abs(x))[::-1])
    else:
        t = -1*int(str(abs(x))[::-1])

    if -(2**31-1)< t <(2**31-1):
        return t
    else:
        return 0
if __name__ == '__main__':
    a = reverse(9646324351)
    print(a)


