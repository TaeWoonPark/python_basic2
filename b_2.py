# kuku_2.py


# ユーザーに行数と列数を聞く

rows = int(input("行数を入力してください:"))
cols = int(input("列数を入力してください:"))

for i in range(1, rows + 1):  # 1~行数まで
    for j in range(1, cols + 1):  # 1~列数まで
        print(i * j, end=" ")  # 掛け算の結果を横に並べる
    print()  # 一行終わったら改行
