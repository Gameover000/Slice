def Slice(text,znak):
    spisok = []
    a = ""
    for i in text:
        if i != znak:
            a += i
        else:
            spisok.append(a)
            a = ""
    spisok.append(a)
    if(spisok[-1] == ""):
        del spisok[-1]
    return spisok
