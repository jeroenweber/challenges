f = 'input.txt'
modus = 'r'
presents = 0
c = (0,0)
visited = set()
try:
    file = open(f, modus)
    text = file.read()
    for i in text:
        print(i)
        if i == '>':
            c1 = (c[0]+1,c[1])
        elif i == '^':
            c1 = (c[0],c[1]+1)
        elif i == 'v':
            c1 = (c[0],c[1]-1)
        else:
            c1 = (c[0]-1,c[1])
        visited.add(c1)
        c = c1
        file.close()
except FileNotFoundError as fnfe:
    print(fnfe.args)
    print("File " + f + ' bestaat niet.')
finally:
    pass

print(len(visited)+1)