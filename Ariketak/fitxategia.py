with open('fitxategiAriketa2.txt') as f:
    lerroak = f.readlines()
    aukera = "0"

    while int(aukera) != -1:
        print("1.Hitz bat kontatu")
        print("2.Fitxategiko azken esaldia pantailaratu")
        print("3.Hitz bat ordezkatu")
        print("4.Textua ordezkatu letra bat izan ezik")
        print("5.Aldatu letra bakoitza hurrengoarengatik")
        aukera = input("Sartu zenbaki bat(-1 amaitzeko): ")

        if int(aukera) == 1:
            hitza = input("Sartu kontatu nahi duzun hitza: ")
            hitzKopurua = 0
            for i in lerroak:
                hitzKopurua += i.count(hitza)
            print(hitza + " hitza " + str(hitzKopurua) + " aldiz agertzen da")
        elif int(aukera) == 2:
            print(lerroak[len(lerroak)-1])
        elif int(aukera) == 3:
            hitzBerria = input("Sartu hitz berria: ")
            hitzZaharra = input("Sartu ordezkatu nahi duzun hitza: ")
            for i in lerroak:
                print(i.replace(hitzZaharra,hitzBerria))
        elif int(aukera) == 4:
            letra = input("Sartu letra bat: ")
            for i in lerroak:
                for j in range(len(i)):
                    if i[j] == " ":
                        print(" ",end="")
                    elif i[j] != letra:
                        print("*",end="")
                    else:
                        print(i[j],end="")
                print("")
        elif int(aukera) == 5:
            for i in lerroak:
                for j in range(len(i)):
                    if i[j] == " ":
                        print(" ",end="")
                    elif i[j] == "z":
                        hurrengoa = chr(97)
                        print(str(hurrengoa), end="")
                    elif i[j] == "Z":
                        hurrengoa = chr(65)
                        print(str(hurrengoa), end="")
                    elif i[j] != "z" or i[j] != "Z":
                        letraAsc = ord(i[j])
                        hurrengoa = chr(letraAsc+1)
                        print(str(hurrengoa),end="")
                    else:
                        print(i[j],end="")
                print("")
        print("---------------")
