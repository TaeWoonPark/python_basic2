# スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
# 合計値
# 最大値
# 最小値
# 平均値
# ただし、計算用の組み込み関数やライブラリは使わないこと(sum()やnp.mean()などはNG print()はOK)
# 1つの統計量につき、それ専用の関数を実装すること
# 実行例


def calc_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calc_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def calc_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value


def calc_average(numbers):
    total = calc_sum(numbers)
    count = 0
    for _ in numbers:
        count += 1
    return total // count  # 小数点なしで整数平均を返す


def main():
    raw_input = input("データを入力してください(スペース区切り) > ")
    numbers = [int(n) for n in raw_input.split()]

    print("合計値:", calc_sum(numbers))
    print("最大値:", calc_max(numbers))
    print("最小値:", calc_min(numbers))
    print("平均値:", calc_average(numbers))


if __name__ == "__main__":
    main()
