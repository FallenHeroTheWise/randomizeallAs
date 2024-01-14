
import docx
import random

duzgunsuz=False
class Question:
    def __init__(self, q, a, b, c, d, e):
        self.q=q
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e

symbols = (u"абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ",
           u"abbgdeezijklmnoprctufh'y'eABBGDEEZIJKLMNOPRCTUFH'Y'E")

tr = {ord(a): ord(b) for a, b in zip(*symbols)}

def cyrillic2latin(input):
    return input.translate(tr)

def main():

    questions = []
    con = 0
    f = open("read.txt", 'r+', encoding='utf-8')
    lines = f.readlines()
    lines[54].replace("", "")
    random.seed(10)
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    q = ''
    dictf = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
    for line in lines:
        line=line.replace("", "").strip()
        line=cyrillic2latin(line)

        if line.upper().startswith('A)'):
            con = 1
            a = ''
        if con == 0:
            q += line + "\n"
        if line.upper().startswith('B)'):
            con = 2
            b = ''
        elif line.upper().startswith('C)'):
            con = 3
            c = ''
        elif line.upper().startswith('D)'):
            con = 4
            d = ''
        elif line.upper().startswith('E)'):
            e = line[1:]
            questions.append(Question(q, a, b, c, d, e))
            con = 0
            q = ''
        line = line[1:]
        if con == 1:
            if duzgunsuz:
                a += '' + line
            else:
                a += "__" + line
        if con == 2:
            b += line
        if con == 3:
            c += line
        if con == 4:
            d += line
    length = len(questions)
    print(length)
    if duzgunsuz:
        v = open(f"duzgunsuz{length}.txt", 'w', encoding='utf-8')
    else:
        v = open(f"duzgunlu{length}.txt", 'w', encoding='utf-8')
    lis = []
    cc = 1
    for q in questions:
        lis.append(q.q + '\n')
        ans = [q.a, q.b, q.c, q.d, q.e]
        random.shuffle(ans)
        for an in ans:
            lis.append(dictf[cc] + an + '\n')
            cc += 1
        if cc == 6:
            lis.append('\n\n')
            cc = 1
    v.write(''.join(lis))




if True:
    main()
    duzgunsuz=True
    main()


        
    

