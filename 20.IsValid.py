def isValid(s):
    #x = str(s)
    dict = {')':'(',']':'[','}':'{'}
    #z = Stack()
    stack = []
    for i in s:
        if i in dict.values():
            stack.append(i)
        elif i in dict.keys():
            if stack == [] or dict[i] != stack.pop():
                return False
        else:
            return False
    if s == "(" or  "[" or  "{":
        return False
    else:
        return True

if __name__ == '__main__':
    s="{}"
    print(isValid(s))
