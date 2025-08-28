# beautiful kuku_py

# 行数と列数を入力してもらう

rows = int(input("行数を入力してもらう:"))
cols = int(input("列数を入力してください:"))

# 掛け算の表を表示する

for j in range(1, rows + 1):  # 縦
    for i in range(1, cols + 1):  # 横

        result = i * j
        # 結果が2桁以下ならスペースを追加して揃える

        if result < 10:
            print(f"{i} x {j} = {result} |", end=" ")
        elif result < 100:
            print(f"{i} x {j} = {result} |", end=" ")
        else:
            print(f"{i} x {j} = {result} |", end=" ")  # 3桁はそのまま
    print()
