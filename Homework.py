largeLetter = [["  A  ",
                " A A ",
                " AAA ",
                "A   A",
                "A   A", ],

               ["BBBB ",
                "B   B",
                "BBBBB",
                "B   B",
                "BBBB "], [

                   " cccc",
                   "c    ",
                   "c    ",
                   "c    ",
                   " cccc", ], [

                   "DDDD ",
                   "D   D",
                   "D   D",
                   "D   D",
                   "DDDD "], [

                   "EEEEE",
                   "E    ",
                   "EEEE ",
                   "E    ",
                   "EEEEE"], [

                   "FFFFF",
                   "F    ",
                   "FFFF ",
                   "F    ",
                   "F    "], [

                   " GGG ",
                   "G    ",
                   "G  GG",
                   "G   G",
                   " GGG "], [

                   "H   H",
                   "H   H",
                   "HHHHH",
                   "H   H",
                   "H   H"], [

                   "IIIII",
                   "  I  ",
                   "  I  ",
                   "  I  ",
                   "IIIII"], [

                   " JJJJ",
                   "   J ",
                   "   J ",
                   "   J ",
                   "JJJ  "], [

                   "K   K",
                   "K KK ",
                   "KK   ",
                   "K KK ",
                   "K   K"], [

                   "L    ",
                   "L    ",
                   "L    ",
                   "L    ",
                   "LLLLL"], [

                   "M   M",
                   "MM MM",
                   "M M M",
                   "M   M",
                   "M   M"], [

                   "N   N",
                   "NN  N",
                   "N N N",
                   "N  NN",
                   "N   N"], [

                   " OOO ",
                   "O   O",
                   "O   O",
                   "O   O",
                   " OOO "], [

                   "PPPP ",
                   "P   P",
                   "PPPP ",
                   "P    ",
                   "P    "], [

                   " QQ  ",
                   "Q  Q ",
                   "Q QQ ",
                   "Q  Q ",
                   " QQ Q"], [

                   "RRRR ",
                   "R   R",
                   "RRRR ",
                   "R  R ",
                   "R   R"], [

                   " SSSS",
                   "S    ",
                   " SSS ",
                   "    S",
                   "SSSS "], [

                   "TTTTT",
                   "  T  ",
                   "  T  ",
                   "  T  ",
                   "  T  "], [

                   "U   U",
                   "U   U",
                   "U   U",
                   "U   U",
                   " UUU "], [

                   "V   V",
                   "V   V",
                   " V V ",
                   " V V ",
                   "  V  "], [

                   "W   W",
                   "W   W",
                   "W   W",
                   "W W W",
                   " W W "], [

                   "X   X",
                   " X X ",
                   "  X  ",
                   " X X ",
                   "X   X"], [

                   "Y   Y",
                   " Y Y ",
                   "  Y  ",
                   "  Y  ",
                   "  Y  "], [

                   "ZZZZZ",
                   "   Z ",
                   "  Z  ",
                   " Z   ",
                   "ZZZZZ"]]

# Outer loop, For repeating whle process
while True:
    largeText = input("Large Text>").upper()
    file = open('out.txt', 'w')

    while True:

        method = input("Calital \"C\" , Lowercase \"L\" or Subtext \"S\" >").upper()
        if method == "C" or method == "L":
            break
        if method == "S":
            subtext = ""
            while len(subtext) == 0:
                subtext = input("Subtext is >")
            positionInSubtext = 0
            subtextLength = len(subtext)
            break
    largeTextSections = []
    print()
    while len(largeText) > 19:
        largeTextSections.append(largeText[:19])
        largeText = largeText[19:]
    if len(largeText) > 0:
        largeTextSections.append(largeText)
    for section in largeTextSections:
        for i in range(5):
            string = ""
            for line in section:
                if line == " ":
                    string += " " * 5
                else:
                    if method == "S":
                        for character in range(5):
                            newstr = largeLetter[ord(line) - 65][i]
                            if largeLetter[ord(line) - 65][i][character] == " ":
                                string += " "
                            else:
                                string += subtext[positionInSubtext]
                                positionInSubtext = (positionInSubtext + 1) % subtextLength
                    elif method == "L":
                        string += largeLetter[ord(line) - 65][i].lower()
                    else:
                        string += largeLetter[ord(line) - 65][i]
                    string += "  "

            file.write(string)
            file.write('\n')
    if input("Do you wish to exit \"Y\"/\"N\" >").upper() == "Y":
        break
