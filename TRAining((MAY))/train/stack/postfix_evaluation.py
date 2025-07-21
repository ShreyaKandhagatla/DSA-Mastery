def postfix(exp):
    stack = []
    
    for i in exp.split(','):#to make it as a list
        if (i[-1].isdigit()):
            stack.append(int(i))
        else:
            right = stack.pop()
            left = stack.pop()

            if i == '+':
                stack.append(left + right)
            elif i == '-':
                stack.append(left - right)
            elif i == '*':
                stack.append(left * right)
            elif i == '/':
                stack.append(left / right)
            elif i == '^':
                stack.append(left ** right)
            else:
                print("BYe Bye")
    
    return stack[-1]#top of stack
exp=input()
print(postfix(exp))

