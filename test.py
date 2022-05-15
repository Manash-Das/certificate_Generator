def main():
    global a
    a=5
    b=6


def second():
    a=7
    b=10
    main()
    print(a)
second()
