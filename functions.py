#Katie Crowdle 119325941

###Question1
def fractions(DNA):
    try:
        C = 0.0
        G = 0.0
        A = 0.0
        T = 0.0
        counter = 0.0

        for item in DNA:
            if item == "C":
                C += 1
            elif item == "G":
                G += 1
            elif item == "A":
                A += 1
            elif item == "T":
                T += 1
        counter = C + G + A + T
        if counter != 0:
            answerC = C / counter
            answerG = G / counter
            answerA = A / counter
            answerT = T / counter

            return answerC,answerG,answerT,answerA
        return C,G,T,A

    except:
        return "Please input a string"


#print(fractions("CC"))



####Question2
def F(S1,S2):
    R = []
    for e1 in S1:
        for e2 in S2:
            if e1 == e2:
                R += [e1]
                break
    return R
#print(F("0","3"))

def F_while(S1,S2):
    R = []
    i = 0
    j = 0
    while i < len(S1):
        while j < len(S2):
            if S1[i] == S2[j]:
                R += S1[i]
                break
            j += 1
        j = 0
        i += 1
    return R
#print(F_while("123","234"))

def  F_list_comp(S1,S2):
    R = [e1 for e1 in S1 for e2 in S2 if e1 == e2]
    return R
#print(F_list_comp("0","3"))

def  F_lambda(S1,S2):
    return list(map(lambda e1: e1, zip(S1,S2)))

def  F_error(S1,S2):
    R = []
    try:
        for e1 in S1:
            for e2 in S2:
                if e1 == e2:
                    R+=[e1]
        if len(R) == 0:
            R = 'List is empty'
        return R
    except:
        R = "Error"
    return R
#print(F_error("1","2"))


###Question3
def frequencies(s):
    new_s = sorted(s)
    answer = {}
    counter = 0
    try:
        if new_s == str or list or tuple:
            for char in new_s:
                if char not in answer:
                    answer[char] = 0
            for x in answer:
                answer[x] = new_s.count(x)
            return answer
    except:
        return "Error input in incorrect"
#print(frequencies("ABCD"))




####Question4

def first(s):
    s = str(s)
    answer = ""
    for char in s:
        if char not in answer:
            answer += char
    return str(answer)
#print(first("mississippi"))


###Question5
def extract(text,n,m):
    try:
        for x in range(m-1, len(text)):
            if text[x] == "":
                letter = text[x+n]
                print(letter)

    except:
        return "Error"

