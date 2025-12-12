def simplify(path):
    stack=[]
    address=path.split('/')
    for part in address:
        if part=='' or part=='.':
            continue
        elif part=='..':
            try:
                stack.pop()
            except IndexError as e:
                stack.append('..')
        else:
            stack.append(part)
    return '/'+'/'.join(stack)
