def multiploak():
	lista5 = []
	lista7 = []
	for i in range(1500,2700):
		if i % 5 == 0:
			##print("5en multiploa: " + str(i))
			lista5.append(i)
		elif i % 7 == 0:
			##print("7ren multiploa: " + str(i))
			lista7.append(i)
	print("5en multiploak: ")
	print(lista5)
	print("7ren multiploak: ")
	print(lista7)

def celsiusFahrenheit():
	print("1.Celsiusetik Fahrenheitera")
	print("2.Fahrenheitik celsiusera")
	aukera = input("Sartu zenbaki bat: ")

	if int(aukera) == 1:
		celsius = input("Sartu graduak celsisus formatuan: ")
		fahrenheit = (int(celsius) * 9) / 5 + 32
		print(celsius + "C " + str(fahrenheit) + " F dira")
	elif int(aukera) == 2:
		fahrenheit = input("Sartu graduak fahrenheit formatuan: ")
		celsius = ((int(fahrenheit) - 32) / 9) * 5
		print(fahrenheit + " F " + str(round(celsius)) + " C dira")


def asteriskoakInprimatu():
	zenbakia = input("Sartu zenbaki bat: ")

	for i in range(0, int(zenbakia)):
		for j in range(0, int(zenbakia)):
			if j <= i:
				print("* ", end='')
		print()
	for i in range(1, int(zenbakia)):
		for j in range(1, int(zenbakia)):
			if j + i <= int(zenbakia):
				print("* ", end='')
		print()

def zerrendakoBikoitiak():
	zerrenda = (1, 2, 3, 4, 5, 6, 7, 8, 9)
	bakoitiak = 0
	bikoitiak = 0
	for i in range(0, len(zerrenda)):
		if zerrenda[i] % 2 == 0:
			bikoitiak += 1
		else:
			bakoitiak += 1
	print("Zenbaki bikotiti kopurua: " + str(bikoitiak))
	print("Zenbaki bakoiti kopurua: " + str(bakoitiak))

def fizzbuzz():
	for i in range(0,51):
		if i % 3 == 0 and i % 5 == 0:
			print("fizzbuzz")
		elif i % 3 == 0:
			print("fizz")
		elif i % 5 == 0:
			print("buzz")
		else:
			print(str(i))


def letrakDigituakKontatu():
	letrak = 0
	digituak = 0
	esaldia = input("Idatzi zerbait: ")

	while len(esaldia) > 0:
		c = esaldia % 10
		if c.isalpha():
			letrak += 1
		elif c.isdigit():
			digituak += 1

		esaldia = esaldia / 10

	print("Digituak: " + str(digituak))
	print("Letrak: " + str(letrak))

def digituKopurua():
	letrak = 0
	digituak = 0
	esaldia = input("Sartu esaldi bat: ")
	for i in range(0,len(esaldia)):
		if(esaldia[i].isdigit()):
			digituak += 1
		elif(esaldia[i].isalpha()):
			letrak += 1
	print("Letrak: " + str(letrak))
	print("Digituak: " + str(digituak))

def aLetraInprimatu():
	for i in range(0,7):
		if i == 0:
			print(" *** ")
		elif i == 3:
			print("*****")
		else:
			print("*   *")

def kontsonanteaDa():
	hizkia = input("Idatzi alfabetoko letra bat: ")
	if hizkia[0].lower() == "a" or hizkia[0].lower() == 'e' or hizkia[0].lower() == 'i' or hizkia[0].lower() == 'o' or hizkia[0].lower() == 'u':
		print(hizkia[0] + " bokala da")
	else:
		print(hizkia[0] + " kontsonantea da")

def urtaroa():
	hilabetea = input("Sartu hilabete bat: ")
	eguna = input("Sartu hilabeteko eguna: ")
	if (hilabetea.lower() == "martxoa" and int(eguna) >= 20 and int(eguna) <= 31) or (hilabetea.lower() == "apirila" and int(eguna) >= 1 and int(eguna) <= 30) or (hilabetea.lower() == "maiatza" and int(eguna) >= 1 and int(eguna) <= 31) or (hilabetea.lower() == "ekaina" and int(eguna) < 21 and int(eguna) <= 30):
		print("Urtaroa udaberria da")
	elif (hilabetea.lower() == "ekaina" and int(eguna) >= 21 and int(eguna) <= 30) or (hilabetea.lower() == "uztaila" and int(eguna) >= 1 and int(eguna) <= 31) or (hilabetea.lower() == "abuztua" and int(eguna) >= 1 and int(eguna) <= 31) or (hilabetea.lower() == "iraila" and int(eguna) < 23 and int(eguna) <= 30):
		print("Urtaroa uda da")
	elif (hilabetea.lower() == "iraila" and int(eguna) >= 23 and int(eguna) <= 30) or (hilabetea.lower() == "urria" and int(eguna) >= 1 and int(eguna) <= 31) or (hilabetea.lower() == "azaroa" and int(eguna) >= 1 and int(eguna) <= 31) or (hilabetea.lower() == "abendua" and int(eguna) < 21 and int(eguna) <= 31):
		print("Urtaroa udazkena da")
	elif (hilabetea.lower() == "abendua" and int(eguna) >= 21 and int(eguna) <= 31) or (hilabetea.lower() == "urtarrila" and int(eguna) >= 1 and int(eguna) <= 31) or (hilabetea.lower() == "otsaila" and int(eguna) >= 1 and int(eguna) <= 28) or (hilabetea.lower() == "martxoa" and int(eguna) < 20 and int(eguna) <= 31):
		print("Urtaroa negua da")

def biderketaTaula():
	zenbakia = input("Sartu zenbaki bat: ")
	for i in range(1,11):
		emaitza = int(zenbakia) * i
		print(zenbakia + " X " + str(i) + " = " + str(emaitza))

def zenbakienBukleak():
	for i in range(1,10):
		for j in range(0,i):
			print(str(i), end="")
		print("")

import random
def zenbakiaAsmatu():
	asmatzekoZenbakia = random.randint(1,9)
	asmatuta = False
	while not asmatuta:
		zenbakia = input("Sartu zenbaki bat: ")
		if int(zenbakia) == asmatzekoZenbakia:
			asmatuta = True
			print("Asmatu duzu, zenbakia " + zenbakia + " da")
		else:
			print("Saiatu berriro")

def esaldiaAlderantziz():
	esaldia = input("Sartu esaldi bat: ")
	for i in range(len(esaldia)-1,-1,-1):
		print(esaldia[i], end="")

def digituBakoitiak():
	for i in range(100,401):
		bakoitia = True
		for j in range(0,len(str(i))):
			digit = str(i)[j]
			if int(digit) % 2 == 0:
				bakoitia = False
		if bakoitia:
			print(str(i) + ",",end = "")


def batazBestekoa():
	z1 = input("Sartu lehenengo zenbakia: ")
	z2 = input("Sartu bigarren zenbakia: ")
	z3 = input("Sartu hirugarren zenbakia: ")

	emaitza = (int(z1) + int(z2) + int(z3)) / 3
	print("Bataz bestekoa: " + str(emaitza))

def listarenBatuketa():
	zenbakia = "0"
	lista1 = []
	while not (int(zenbakia) == -1):
		zenbakia = input("Sartu zenbaki bat(-1 amaitzeko): ")
		if int(zenbakia) != -1:
			lista1.append(int(zenbakia))
	emaitza = 0
	for i in lista1:
		emaitza += i
	print("Emaitza: " + str(emaitza))

def listarenBiderketa():
	zenbakia = "0"
	lista1 = []
	while not (int(zenbakia) == -1):
		zenbakia = input("Sartu zenbaki bat(-1 amaitzeko): ")
		if int(zenbakia) != -1:
			lista1.append(int(zenbakia))
	emaitza = 1
	for i in lista1:
		emaitza *= i
	print("Emaitza: " + str(emaitza))

def zenbakiHandiena():
	zenbakia = "0"
	lista1 = []
	while int(zenbakia) != -1:
		zenbakia = input("Sartu zenbaki bat(-1 amaitzeko): ")
		if int(zenbakia) != -1:
			lista1.append(int(zenbakia))
	zenbakiHandiena = 0
	for i in lista1:
		if i > zenbakiHandiena:
			zenbakiHandiena = i
	print("Listako zenbaki handiena: " + str(zenbakiHandiena))

def zenbakiTxikiena():
	zenbakia = "0"
	lista1 = []
	while int(zenbakia) != -1:
		zenbakia = input("Sartu zenbaki bat(-1 amaitzeko): ")
		if int(zenbakia) != -1:
			lista1.append(int(zenbakia))
	zenbakiTxikiena = lista1[0]
	for i in lista1:
		if i < zenbakiTxikiena:
			zenbakiTxikiena = i
	print("Listako zenbaki txikiena: " + str(zenbakiTxikiena))

def zenbakiErrepikatuak():
	zenbakia = "0"
	lista1 = []

	while int(zenbakia) != -1:
		zenbakia = input("Sartu zenbaki bat(-1 amaitzeko): ")
		if int(zenbakia) != -1:
			lista1.append(int(zenbakia))
	print("Lista zenbakiak ezabatu aurretik:")
	print(lista1)


	print("Lista zenbakiak ezabatu ondoren")
	print(lista1)

zenbakiErrepikatuak()