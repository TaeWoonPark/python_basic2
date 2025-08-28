rows = int(input("行数を入力してください: "))
cols = int(input("列数を入力してください: "))

for j in range(1, rows + 1):
    for i in range(1, cols + 1):
        # 式全体を18文字に固定（100以上にも対応）
        print(f"{i} x {j} = {i*j:2}", end=" | ")

    print()



