def revList(lst):
    if lst==[]:
        return []

    restrev = revList(lst[1:])
    first = lst[0:1]

    result = restrev + first

    return result


def main():
    print(revList([1,2,3,4,5,6]))


if __name__ == "__main__":
    main()