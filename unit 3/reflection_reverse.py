def reverse(seq):
    SeqType = type(seq)
    emtpySeq = SeqType()

    if seq == emtpySeq:
        return emtpySeq

    restrev = reverse(seq[1:])
    first = seq[0:1]

    result = restrev + first
    return result


def main():
    print(reverse([1,2,3,4,5]))
    print(reverse("hello there"))


if __name__ == "__main__":
    main()