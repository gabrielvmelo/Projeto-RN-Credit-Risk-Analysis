def listToString(list, p):
    text = p.join(list)
    return text

arq = open("TRN", 'r')
text = arq.readlines()
base_len = len(text[0].split("\t"))
print(base_len)
out1 = open("out_classe_1.txt", 'w')
out2 = open("out_classe_2.txt", 'w')


c1 = 0
c2 = 0

for line in text:
    aux = line.split("\t")
    
    aux[base_len-2] = aux[base_len-2][0]
    aux[base_len-1] = aux[base_len-1][0]

    #print(aux)
    
    v1 = aux[base_len-2]
    v2 = aux[base_len-1]
    #print("{}{}".format(v1, v2))
    t = listToString(aux, "\t")
    print("work")

    if (v1 == '0') and (v2 == '1'):
        #c1.append(t)
        out1.write(t)
        c1 += 1
    elif (v1 == '1') and (v2 == '0'):
        #c2.append(t)
        out2.write(t)
        c2 += 1

#out1.writelines(c1)
#out2.writelines(c2)

print("classe 1 = {}".format(c1))
print("classe 2 = {}".format(c2))
print("TOTAL = {}".format(c1+c2))


        

