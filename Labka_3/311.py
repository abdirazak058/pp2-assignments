def murat_abdilda(men_men):
    tak = []
    jyp = []

    for i in range(len(men_men)):
        if i % 2 == 1:
            tak.append(men_men[i])
        else:
            jyp.append(men_men[i])

    print(tak)
    print(jyp)





arr = list(map(int, input().split()))
murat_abdilda(arr)
