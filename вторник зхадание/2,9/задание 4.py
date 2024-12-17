def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    N = int(data[0])
    phonebook = {}

    for i in range(1, N + 1):
        phone, name = data[i].split()
        if name not in phonebook:
            phonebook[name] = []
        phonebook[name].append(phone)

    M = int(data[N + 1])
    results = []

    for j in range(N + 2, N + 2 + M):
        query_name = data[j]
        if query_name in phonebook:
            results.append(" ".join(phonebook[query_name]))
        else:
            results.append("Нет в телефонной книге")

    print("\n".join(results))


if __name__ == "__main__":
    main()
