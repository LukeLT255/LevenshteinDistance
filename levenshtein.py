def levenshteinDistance(str1, str2):
    table = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(len(table[0])):
        table[0][i] = i
    for i in range(len(table)):
        table[i][0] = i

    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1]) + 1
    return table[-1][-1]


if __name__ == '__main__':
    str1 = input('Enter any sequence of characters.' + '\n')
    str2 = input('Enter any sequence of characters.' + '\n')
    print(levenshteinDistance(str1, str2))
