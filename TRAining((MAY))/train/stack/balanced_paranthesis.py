
'''#BALANCED PARANTHESIS
s=input()
def isB(s):
    stack=[]
    brackets={'(':')','{':'}','[':']'}
    opening=['(','{','[']
    for c in s:
        if c in opening:
            stack.append(c)
        else:
            if not stack:
                return 'false'
            else:
                top=stack[-1]
                if brackets[top]==c:
                    stack.pop()
    if stack==[]:
        return 'Valid'
    else:
        return 'Invalid'
print(isB(s))
'''
#MORE EFFCIENT
def isB(s):
    stack = []
    brackets = {'(':')', '{':'}', '[':']'}
    for c in s:
        if c in brackets:
            stack.append(c)
        else:
            if not stack:
                return 'Invalid'
            top = stack[-1]
            if brackets[top] == c:
                stack.pop()
            else:
                return 'Invalid'
    return 'Valid' if not stack else 'Invalid'
s=input()
print(isB(s))
