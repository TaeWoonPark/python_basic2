import random


def main():    # ユーザーから入力を受け取る
    n = int(input("サイコロの面の数は?: "))
    m = int(input("何回振りますか?: "))

    # サイコロをm回振って結果をリストに入れる
    results = []
    for _ in range(m):
        roll = random.randint(1, n)  # 1〜nのランダムな整数
        results.append(roll)

    # 結果を表示
    print(results)


if __name__ == "__main__":
    main()
