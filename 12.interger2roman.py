def intToRoman(num):
    #interger = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1 : 'I'}
    t = num//1000
    h = (num%1000)//100
    d = ((num%1000)%100)//10
    u = num%10

    #print(t,h,d,u)
    s = []
    for i in range(t):
        s.append('M')
    if h <4:
        for i in range(h):
            s.append('C')
    elif h==4:
        s.append('CD')
    elif 5<=h<9:
        c1 = h-5
        s.append('D')
        for i in range(c1):
            s.append('C')
    else:
        s.append('CM')


    if d <4:
        for i in range(d):
            s.append('X')
    elif d == 4:
        s.append('XL')
    elif 5 <= d < 9:
        c2 = d-5
        print(c2)
        s.append('L')
        for i in range(c2):
            s.append('X')
    else:
        s.append('XC')

    if u <4:
        for i in range(u):
            s.append('I')
    elif u == 4:
        s.append('IV')
    elif 5<= u <9:
        c2 = u-5
        s.append('V')
        for i in range(c2):
            s.append('I')
    else:
        s.append('IX')

    return(''.join(s))

if __name__ == '__main__':
    print(intToRoman(60))