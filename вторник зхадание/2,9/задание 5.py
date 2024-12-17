def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])
    birthday_dict = defaultdict(list)

    for i in range(1, N + 1):
        name, day, month = data[i].split()
        day = int(day)
        birthday_dict[month].append((day, name))

    for month in birthday_dict:
        birthday_dict[month].sort(key=lambda x: (x[0], x[1]))

    M = int(data[N + 1])
    results = []

    for i in range(N + 2, N + 2 + M):
        query_month = data[i].strip()
        if query_month in birthday_dict:
            result = " ".join(f"{name} {day}" for day, name in birthday_dict[query_month])
            results.append(result)
        else:
            results.append("")

    print("\n".join(results))

if __name__ == "__main__":
    main()
