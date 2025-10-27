def BinaryConverter():
    Number = input("Enter a number: ")
    print(bin(int(Number)))


def MathoBinary():
    Number = input("Enter a number: ")
    print(int(Number,base=2))


def Converter():
    Number = int(input("Enter a number: "))
    print(bin(Number))


def NewConverter():
    Number = int(input("Enter a number: "))
    BinaryNumber = ""
    while Number > 0 :
        remainder = Number % 2
        BinaryNumber = str(remainder) + BinaryNumber
        Number = Number // 2
    print(BinaryNumber)

NewConverter()

