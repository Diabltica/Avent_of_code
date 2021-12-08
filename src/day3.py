with open("input_day3.txt", "r") as f:
    Lines = f.readlines()

ogr = ''
print(ogr)
list_correct = []
count_one = 0
for line in Lines:
    if line[0] == '1':
        count_one += 1
    elif line[0] == '0':
        count_one -= 1
if count_one >= 0:
    ogr += '1'
else:
    ogr += '0'

print(ogr)
#add correct string to the list
for line in Lines:
    if line[0] == ogr[0]:
        list_correct.append(line)



for i in range(1,12,1):
    count_one = 0
    
    for line in list_correct:
        if line[i] == '1':
            count_one += 1
        elif line[i] == '0':
            count_one -= 1

    if count_one >= 0:
        ogr += '1'
    else:
        ogr += '0'
    buffer = [] 
    for line in list_correct:
        if line[i] != ogr[i]:
            buffer.append(line)
    print(buffer)
    for i in range(len(buffer)):
        list_correct.pop(list_correct.index(buffer[i]))
        #else:
            #print(ogr[i],line[i])

print(list_correct)
print(ogr)
if ogr[0] == '1':
    csr = '0'
else:
    csr = '1'
list_correct.pop()

for line in Lines:
    if line[0] == csr[0]:
        list_correct.append(line)

print(list_correct)
for i in range(1,12,1):
    count_one = 0
    if len(list_correct) != 1:
        for line in list_correct:
            if line[i] == '1':
                count_one += 1
            elif line[i] == '0':
                count_one -= 1

        if count_one >= 0:
            csr += '0'
        elif count_one < 0:
            csr += '1'
        buffer = []
        for line in list_correct:
            #if len(list_correct) != 1:
            if line[i] != csr[i]:
                print(line[i], csr[i])
                buffer.append(line)
        print("Bonjour")
        print(list_correct)
        for i in range(len(buffer)):
            list_correct.pop(list_correct.index(buffer[i]))
            #else:
                #print(ogr[i],line[i])
    else:
        csr =''
        for i in range(len(list_correct[0]) - 1):
            csr += list_correct[0][i]


print(csr)

def bd(to_convert):
    size = len(to_convert)
    temp = 0
    for j in range(size):
        temp = temp + int(to_convert[j]) * 2 ** ((size - 1) - j)
    return temp

a = bd(ogr)
b = bd(csr)

print(a)
print(b)

print(a*b)
