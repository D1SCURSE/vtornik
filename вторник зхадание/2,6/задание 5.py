def main():
    import sys

    input = sys.stdin.read
    data = input().strip().splitlines()

    n = int(data[0]) 
    titles = []
    current_title = []

    for line in data[1:]:
        if line == '*':
            if current_title:
                titles.append('-'.join(current_title))
                current_title = []
        else:
            current_title.append(line.strip())

    titles.reverse()
    result = ','.join(titles)

    print(result)

if __name__ == "__main__":
    main()
