def roman2interger(s):
    roman = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    t=0
    for i in range(len(s)-1):
        #if i < len(s) - 1:
        if roman[s[i]] < roman[s[i+1]]:
            t=t-roman[s[i]]
        else:
            t=t+roman[s[i]]
        #else:
            t = t + roman[s[i]]
    return t + roman[s[-1]]
if __name__ == '__main__':
    s = 'X'
    t = roman2interger(s)
    print(t)
