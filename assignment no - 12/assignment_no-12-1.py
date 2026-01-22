
def VowelOrNot(ch):
    if ch in "aeiou":
        print("Entered alphabet is vowel")

    else:
        print("Enterd alphabet is consonant")

def main():
    cha = print("Enter the alphabet: ")
    cha = input()

    VowelOrNot(cha)


if __name__ == "__main__":
    main()