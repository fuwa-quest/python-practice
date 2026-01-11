import random

a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)]

#動作確認のため答え表示
#print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

while True :
    #４桁か判断
    isok = False
    while isok == False:
        b = input(" 数を入力してね＞")
        if len(b) != 4:
            print(" ４桁の数字を入力してださい ")
        else:
            kazuok = True
            for i in range(4):
                if (b[i] <"0") or (b[i] >"9") :
                    print(" 数字ではありません ")
                    kazuok = False
                    break
                if kazuok :
                    isok = True

    #４桁の数字であったとき
    hit = 0
    for i in range(4):
        if a[i] == int(b[i]):
            hit = hit + 1

    blow = 0
    for j in range(4):
        if b[j] in b[0:j]:
            continue
        
        for i in range(4):
            
            if (int(b[j]) == a[i]) and (a[i] != int(b[i])):
                blow = blow + 1
                break

    print(" ヒット " + str(hit))
    print(" ブロー " + str(blow))

    if hit == 4:
        print(" あたり！ ")
        break
