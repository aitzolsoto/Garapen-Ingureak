#Listas (1) - 1
def listak1():
	lista1= []
	izenKopurua = input("Zenbat hitz sartu nahi dituzu listan? ")
	for i in range(int(izenKopurua)):
		hitza = input("Sartu izen bat: ")
		lista1.append(hitza)
	print("Sortu duzun lista: " + str(lista1))

#Listas (1) - 2
def listak2():
	lista1= []
	izenKopurua = input("Zenbat hitz sartu nahi dituzu listan? ")
	for i in range(int(izenKopurua)):
		hitza = input("Sartu izen bat: ")
		lista1.append(hitza)
	print("Sortu duzun lista: " + str(lista1))
	bilatzekoHitza = input("Sartu bilatu nahi duzun hitza: ")
	hitzaCount = lista1.count(bilatzekoHitza)
	print(bilatzekoHitza + " " + str(hitzaCount) + " aldiz agertzen da listan")

#Listas (1) - 3
def listak3():
	lista1= []
	izenKopurua = input("Zenbat hitz sartu nahi dituzu listan? ")
	for i in range(int(izenKopurua)):
		hitza = input("Sartu izen bat: ")
		lista1.append(hitza)
	print("Sortu duzun lista: " + str(lista1))
	hitzBerria = input("Sartu hitz berria: ")
	hitzZaharra = input("Zein da listatik kendu nahi duzun hitza? ")
	hitzarenIndexa = lista1.index(hitzZaharra)
	if hitzarenIndexa != None:
		lista1[hitzarenIndexa] = hitzBerria
	print("Lista aldatu ondoren: " + str(lista1))

#Listas (1) - 4
def listak4():
	lista1= []
	izenKopurua = input("Zenbat hitz sartu nahi dituzu listan? ")
	for i in range(int(izenKopurua)):
		hitza = input("Sartu izen bat: ")
		lista1.append(hitza)
	print("Sortu duzun lista: " + str(lista1))
	ezabatzekoHitza = input("Sartu ezabatu nahi duzun hitza: ")
	lista1.remove(ezabatzekoHitza)
	print("Lista aldatu ondoren: " + str(lista1))

#Listas (1) - 5
def listak5():
	lista1= []
	lista2= []
	izenKopurua = input("Zenbat hitz sartu nahi dituzu listan? ")
	for i in range(int(izenKopurua)):
		hitza = input("Sartu izen bat: ")
		lista1.append(hitza)
	print("Sortu duzun lista: " + str(lista1))

	hitzakLista2 =  input("Zenbat hitz ezabatu nahi dituzu: ")
	for i in range(int(hitzakLista2)):
		hitza = input("Sartu ezabatu nahi duzun izen bat: ")
		lista2.append(hitza)
		lista1.remove(hitza)
	print("Ezabatu nahi dituzun izenak: " + str(lista2))
	print("Lista aldatu ondoren: " + str(lista1))

#Listas (1) - 6
def listak6():
	lista1= []
	lista2= []
	izenKopurua = input("Zenbat hitz sartu nahi dituzu listan? ")
	for i in range(int(izenKopurua)):
		hitza = input("Sartu izen bat: ")
		lista1.append(hitza)
	print("Sortu duzun lista: " + str(lista1))

	for i in reversed(lista1):
		lista2.append(i)
	print("Lista alderantziz: " + str(lista2))

#Listas (1) - 7
def listak7():
	lista1= []
	izenKopurua = input("Zenbat hitz sartu nahi dituzu listan? ")
	for i in range(int(izenKopurua)):
		hitza = input("Sartu izen bat: ")
		lista1.append(hitza)
	print("Sortu duzun lista: " + str(lista1))

	for i in lista1:
		errepikatutakoAldiak = lista1.count(i)
		if errepikatutakoAldiak > 1:
			lista1.remove(i)
	print("Lista errepikatutakoak ezabatu ondoren: " + str(lista1))

#Listas (1) - 8
def listak8():
	lista1= []
	lista2= []
	bietanDaudenHitzak = []
	lehenengoListakoak = []
	bigarrenListakoak = []
	hitzGuztiak = []

	izenKopurua = input("Zenbat hitz sartu nahi dituzu listan? ")
	for i in range(int(izenKopurua)):
		hitza = input("Sartu izen bat: ")
		lista1.append(hitza)
	print("Lehenengo listako hitzak: " + str(lista1))

	izenKopurua = input("Zenbat hitz sartu nahi dituzu listan? ")
	for i in range(int(izenKopurua)):
		hitza = input("Sartu izen bat: ")
		lista2.append(hitza)
	print("Bigarren listako hitzak: " + str(lista2))

	for i in lista1:
		if i in lista2 and i not in bietanDaudenHitzak:
			bietanDaudenHitzak.append(i)
		if i not in lista2 and i not in lehenengoListakoak:
			lehenengoListakoak.append(i)
		if i not in hitzGuztiak:
			hitzGuztiak.append(i)

	for i in lista2:
		if i not in lista1 and i not in bigarrenListakoak:
			bigarrenListakoak.append(i)
		if i not in hitzGuztiak:
			hitzGuztiak.append(i)

	print("Bi listetan agertzen diren hitzak: " + str(bietanDaudenHitzak))
	print("Lehengo listan bakarrik agertzen diren hitzak: " + str(lehenengoListakoak))
	print("Bigarren listan bakarrik agertzen diren hitzak: " + str(bigarrenListakoak))
	print("Hitz guztiak: " + str(hitzGuztiak))

