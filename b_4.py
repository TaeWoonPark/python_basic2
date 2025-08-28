def main():
    # 3都府県の駅名と最高気温のデータ
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温
    total_temp = sum(data["temperature"] for data in weather_information)
    average_temp = total_temp / len(weather_information)
    print(f"Q1. 全国の平均気温: {average_temp:.1f}℃")

    # Q2. 大阪府の駅名（カンマ区切り）
    osaka_stations = [data["station"] for data in weather_information if data["prefecture"] == "大阪府"]
    osaka_station_str = ",".join(osaka_stations)
    print(f"Q2. 大阪府の駅名: {osaka_station_str}")

    # Q3. 福岡県の平均気温
    fukuoka_temps = [data["temperature"] for data in weather_information if data["prefecture"] == "福岡県"]
    fukuoka_avg = sum(fukuoka_temps) / len(fukuoka_temps)
    print(f"Q3. 福岡県の平均気温: {fukuoka_avg:.1f}℃")


if __name__ == "__main__":
    main()
