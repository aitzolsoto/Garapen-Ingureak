from csv import reader

def langileaBilatuId():
    idLangilea = input("Sartu langilearen ID-a: ")
    value = listaCsv[int(idLangilea)]
    print(value)

def langileakBilatuIzenBidez():
    izena = input("Sartu izen bat: ")
    for i in range(len(listaCsv)):
        if listaCsv[i][7] == izena:
            print(listaCsv[i])

def langileakBilatuSoldataBidez():
    soldata = input("Sartu soldata: ")
    for i in range(len(listaCsv)):
        if (listaCsv[i][3] > soldata):
            print(listaCsv[i])

def langileakBilatuHerriarenBidez():
    herria = input("Sartu herri baten izena: ")
    for i in range(len(listaCsv)):
        if(listaCsv[i][9] == herria):
            print(listaCsv[i])

def langileakBilatuAdinarenBidez():
    adina = input("Sartu adina: ")
    for i in range(len(listaCsv)):
        if(listaCsv[i][1] > adina):
            print(listaCsv[i])

def soldataAltuena():
    maxSoldata = "0"
    langilea = 0
    for i in range(1,len(listaCsv)):
        if listaCsv[i][3] > maxSoldata:
            maxSoldata = listaCsv[i][3]
            langilea = i
    print(listaCsv[langilea])

def soldataIgo():
    langilea = input("Sartu langilearen ID-a: ")
    soldataBerria = input("Sartu langilearen soldata berria: ")
    listaCsv[int(langilea)][3] = soldataBerria

def soldatarenAraberaOrdenatu():

    for i in range(1,len(listaCsv)):
        for j in range(0,len(listaCsv)-1):
            if listaCsv[j+1][3] < listaCsv[j][3]:
                aux = listaCsv[j+1]
                listaCsv[j+1] = listaCsv[j]
                listaCsv[j] = aux

    for i in range(1,len(listaCsv)):
        print(listaCsv[i])

with open('employee.csv') as csvList:
    csv_reader = reader(csvList)
    listaCsv = list(csv_reader)
    print(listaCsv)
aukera = 0
while(int(aukera) != 9):
    print("")
    print("---------------------")
    print("MENUA")
    print("---------------------")
    print("1-Langile baten informazioa ikusi")
    print("2-Izenaren bidez bilatu")
    print("3-Soldataren bidez bilatu(x soldata baino gehiago irabazten dutenak)")
    print("4-Herriaren bidez bilatu")
    print("5-Adinaren bidez bilatu(x urte baino gehiago dutenak")
    print("6-Soldata altuena duen langilea ikusi")
    print("7-Soldata igo")
    print("8-Soldataren arabera ordenatu")
    print("9-Irten")
    aukera = input("Sartu zenbaki bat: ")

    if int(aukera) == 1:
        langileaBilatuId()
    elif int(aukera) == 2:
        langileakBilatuIzenBidez()
    elif int(aukera) == 3:
        langileakBilatuSoldataBidez()
    elif int(aukera) == 4:
        langileakBilatuHerriarenBidez()
    elif int(aukera) == 5:
        langileakBilatuAdinarenBidez()
    elif int(aukera) == 6:
        soldataAltuena()
    elif int(aukera) == 7:
        soldataIgo()
    elif int(aukera) == 8:
        soldatarenAraberaOrdenatu()
