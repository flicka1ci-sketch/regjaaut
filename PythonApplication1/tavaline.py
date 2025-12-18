from mymodule import *

kasutajad = []
paroolid = []

while True:
    print("\n--- MENÜÜ ---")
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Nime või parooli muutmine")
    print("4 - Unustatud parooli taastamine")
    print("5 - Välju")

    valik = input("Vali: ")

    if valik == "1":
        registreerimine(kasutajad, paroolid)
    elif valik == "2":
        autoriseerimine(kasutajad, paroolid)
    elif valik == "3":
        muutmine(kasutajad, paroolid)
    elif valik == "4":
        parooli_taastamine(kasutajad, paroolid)
    elif valik == "5":
        print("Programmi töö lõpetatud.")
        break
    else:
        print("Vale valik!")
