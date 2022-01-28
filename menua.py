from csv import reader
from datetime import date

with open('employee.csv') as csvList:
    csv_reader = reader(csvList)
    listaCsv = list(csv_reader)
    print(listaCsv)

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

def adinaKalkulatu():
    langilea = input("Sartu langile baten ID-a: ")
    data = listaCsv[int(langilea)][10]
    urtea = data[0:4]
    hilabetea = data[5:7]
    eguna = data[8:10]

    urtebetetzea = date(int(urtea),int(hilabetea),int(eguna))
    today = date.today()

    age = today.year - urtebetetzea.year
    if today.month < urtebetetzea.month:
        age -= 1
    elif today.month == urtebetetzea.month and today.day < urtebetetzea.day:
        age -= 1
    print("Adina: " + str(age))

def abizenarenAraberaOrdenatu():
    for i in range(1,len(listaCsv)):
        for j in range(0,len(listaCsv)-1):
            if listaCsv[j+1][8] < listaCsv[j][8]:
                aux = listaCsv[j+1]
                listaCsv[j+1] = listaCsv[j]
                listaCsv[j] = aux

    for i in range(1,len(listaCsv)):
        print(listaCsv[i])

def langilearenIzenaAldatu():
    langilea = input("Sartu langilearen ID-a: ")
    izenBerria = input("Sartu langilearen izen berria: ")
    listaCsv[int(langilea)][7] = izenBerria

aukera = 0
while(int(aukera) != 12):
    print("")
    print("---------------------")
    print("MENUA")
    print("---------------------")
    print("1-Langile baten informazioa ikusi")
    print("2-Izenaren bidez bilatu")
    print("3-Soldataren bidez bilatu(x soldata baino gehiago irabazten dutenak)")
    print("4-Herriaren bidez bilatu")
    print("5-Adinaren bidez bilatu(x urte baino gehiago dutenak)")
    print("6-Soldata altuena duen langilea ikusi")
    print("7-Soldata igo")
    print("8-Soldataren arabera ordenatu")
    print("9-Langile baten adina kalkulatu")
    print("10-Abizenaren arabera ordenatu")
    print("11-Langilearen izena aldatu")
    print("12-Irten")
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
    elif int(aukera) == 9:
        adinaKalkulatu()
    elif int(aukera) == 10:
        abizenarenAraberaOrdenatu()
    elif int(aukera) == 11:
        langilearenIzenaAldatu()
