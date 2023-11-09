def solution(s):    
    s = list(s)
    stack = []
    
    for i in s:
        try:
            if i == '(':
                stack.append('s')
            elif i == ')':
                stack.pop()
        except IndexError:
            return False
    
    return False if stack else True