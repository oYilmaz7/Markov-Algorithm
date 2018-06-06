dict = {}
tickets = []
enk = 0
enb = 0
level = 4
# mxcol = 4
# mxlen = 150
chars = []
posses =[]
with open('irisdata.txt') as openfile:
    for line in openfile:
        line_ = line.split(",")
        line2 = []
        mx = []
        for k in line_:
            k = k.strip()
            line2.append(k)
        mxcol = line2.__len__() - 1
        if dict.has_key(line2[line2.__len__() - 1]):
            mx = dict[line2[line2.__len__() - 1]]
            mx.append(line2)
            dict[line2[line2.__len__() - 1]] = mx
        else:
            mx.append(line2)
            dict[line2[line2.__len__() - 1]] = mx
            tickets.append(line2[mxcol])
            # mx.append(line2)

mxlen = mx.__len__() * tickets.__len__()

# print dict.keys()
# print dict['Iris-setosa']

ticketslen = tickets.__len__()
# print mxcol
# dict[tickets[0]]

charsize = (mxcol) * level

for i in range(0, charsize):
    chars.append(chr(ord('a') + i))
ticketn = tickets.__len__()

for k in range(0, ticketslen):
    for j in range(0, mxcol):
        enk = dict[tickets[k]][0][j]
        enb = dict[tickets[k]][0][j]
        for i in range(0, len(dict[tickets[0]])):
            if dict[tickets[k]][i][j] <= enk:
                enk = dict[tickets[k]][i][j]
            if dict[tickets[k]][i][j] >= enb:
                enb = dict[tickets[k]][i][j]

        inter = (float(enb) - float(enk)) / mxcol

        for i in range(0, len(dict[tickets[0]])):
            for x in range(0, level):
                if float(dict[tickets[k]][i][j]) <= float(enk) + inter * (x + 1):
                    dict[tickets[k]][i][j] = chars[level * j + x]
                    # print dict[tickets[k]][i][j]
                    break










                    # print inter
                    # print enk
                    # print "\n\n"


def poss(mx, harf):
    sayac = 0
    for i in range(0, len(mx)):
        if mx[i][0] == harf:
            sayac += 1
    return float(sayac) / float(len(mx))


def poss2(mx, harf1, harf2):
    index = -1
    sayac = 0
    for i in range(0, len(mx)):
        for j in range(0, 4):
            if mx[i][j] == harf1:
                index = j

    for i in range(0, len(mx)):
        if (mx[i][index] == harf1) and (mx[i][index + 1] == harf2):
            sayac += 1

    return sayac


# x=poss2(dict [tickets[2]],"c","g")
# print x



# print dict [tickets[0]]
# print dict [tickets[1]]
# print dict [tickets[2]]
# print chars


def poss3(mx, harf1, harf2, harf3, harf4):
    index = -1
    sayac = 0
    for i in range(0, len(mx)):
        for j in range(0, 4):
            if mx[i][j] == harf1:
                index = j

    for i in range(0, len(mx)):
        if (mx[i][index] == harf1) and (mx[i][index + 1] == harf2) and (mx[i][index + 2] == harf3) and (
            mx[i][index + 3] == harf4):
            sayac += 1

    return sayac


x=poss3(dict [tickets[0]],"c","g","k","m")
print x

for i in range(0, charsize / level):
    x = poss(dict[tickets[0]], chars[i])
    #print x





z = poss2(dict[tickets[0]], "g", "k")
print z

y=poss(dict[tickets[0]],"c")
#print y