def one_edit_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)

    return False

def one_edit_replace(s1, s2):
    edited = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if edited:
                return False
            edited = True
    return True

def one_edit_insert(s1, s2):
    index1 = 0
    index2 = 0
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

s1 = "pale"
s2 = "ple"
print(one_edit_away(s1, s2))  # True

s1 = "pales"
s2 = "pale"
print(one_edit_away(s1, s2))  # True

s1 = "pale"
s2 = "bale"
print(one_edit_away(s1, s2))  # True

s1 = "pale"
s2 = "bake"
print(one_edit_away(s1, s2))  # False
