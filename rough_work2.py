
def LetterChanges(str):

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    changes = "bcdEfghIjklmnOpqrstUvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZA"

    mapping = {u: v for (u,v) in zip(str+letters,str+changes)}
    return "".join([mapping[c] for c in str])

print (LetterChanges('fun times!'))