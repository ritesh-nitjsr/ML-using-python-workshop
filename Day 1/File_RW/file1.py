content = []

with open('test.csv', 'r') as f:
    for line in f:
        z = line.split(',')
        _z = [int(x) for x in z]
        content.append(_z)
content.sort(key = lambda x : x[1])
with open('submit.csv', 'w') as f:
    for i in range(len(content)):
        f.write(str(content[i][0])+","+str(content[i][1])+","+str(content[i][2])+"\n")
