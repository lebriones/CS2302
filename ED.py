def edit_distance(string1, string2, len1, len2):
    ed = [[0 for i in range(len2 + 1)] for i in range(len1 + 1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0:
                ed[i][j] = j
            elif j == 0:
                ed[i][j] = i
            elif string1[i-1] == string2[j-1]:
                ed[i][j] = ed[i-1][j-1]
            else:
                ed[i][j] = 1 + min(ed[i][j-1], ed[i-1][j], ed[i-1][j-1])
    return ed[len1][len2]