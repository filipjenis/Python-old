def fromBrainfuck():
    code = input("Zadajte Brainfuck kód:")

    pointer=0
    char_lst=[0]
    final=[]

    for a in code:
        if a==">":
            char_lst.append(0)

    i=0
    while i < len(code):
        if code[i] == ">":
            pointer += 1
        elif code[i] == "<":
            pointer -= 1
        elif code[i] == "+":
            if char_lst[pointer]<255:
                char_lst[pointer] += 1
            else:
                char_lst[pointer] = 0
        elif code[i] == "-":
            if char_lst[pointer]>0:
                char_lst[pointer] -= 1
            else:
                char_lst[pointer] = 255
        elif code[i] == ".":
            final.append(chr(char_lst[pointer]))
        elif code[i] == ",":
            char_lst[pointer] = ord(input("Zadaj charakter(pointer:" + str(pointer) + "):"))
        elif code[i] == "[":
            if char_lst[pointer] == 0:
                braces = 1
                while braces > 0:
                    i += 1
                    if code[i] == "[": braces += 1
                    if code[i] == "]": braces -= 1
        elif code[i] == "]":
            braces = 1
            while braces > 0:
                i -= 1
                if code[i] == "[": braces -= 1
                if code[i] == "]": braces += 1
            i -= 1

        i += 1

    print("".join(final))

def toBrainfuck():
    text = input("Zadajte text:")

ask=0
while ask<1:
    print("1: Brainfuck - text")
    print("2: text - Brainfuck")
    inp = input("Preklad?")
    if inp == "1": fromBrainfuck()
    if inp == "2": toBrainfuck()
    if inp == "": ask += 1
    print("")