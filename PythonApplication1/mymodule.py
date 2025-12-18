# Selles programmis loome kasutajate haldamiseks süsteemi, mis võimaldab registreerimist, autoriseerimist,
# nime või parooli muutmist ning parooli taastamist. Kõik vajalikud funktsioonid on defineeritud MyModule.py.
import random


def genereeri_parool() -> str:
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3

    ls = list(str4)
    random.shuffle(ls)

    psword = ''.join([random.choice(ls) for x in range(12)])
    return psword


def parool_kehtiv(psw: str) -> bool:
    erimargid = ".,:;!_*-+()/#¤%&"

    return (
        any(c.isdigit() for c in psw) and
        any(c.islower() for c in psw) and
        any(c.isupper() for c in psw) and
        any(c in erimargid for c in psw)
    )


def registreerimine(kasutajad: list, paroolid: list) -> None:
    login = input("Sisesta uus kasutajanimi: ")

    if login in kasutajad:
        print("Kasutajanimi on juba olemas!")
        return

    print("A - Automaatne parool")
    print("B - Loo parool ise")
    valik = input("Vali A või B: ").upper()

    if valik == "A":
        psw = genereeri_parool()
        kasutajad.append(login)
        paroolid.append(psw)
        print("Registreerimine õnnestus!")
        print("Sinu parool:", psw)

    elif valik == "B":
        while True:
            psw = input("Sisesta parool: ")

            if parool_kehtiv(psw):
                kasutajad.append(login)
                paroolid.append(psw)
                print("Registreerimine õnnestus!")
                break
            else:
                print("Parool ei vasta nõuetele!")
    else:
        print("Vale valik!")


def autoriseerimine(kasutajad: list, paroolid: list) -> None:
    login = input("Sisesta kasutajanimi: ")
    psw = input("Sisesta parool: ")

    if login in kasutajad and paroolid[kasutajad.index(login)] == psw:
        print("Sisselogimine õnnestus!")
    else:
        print("Vale kasutajanimi või parool!")


def muutmine(kasutajad: list, paroolid: list) -> None:
    login = input("Sisesta oma kasutajanimi: ")

    if login not in kasutajad:
        print("Kasutajat ei leitud!")
        return

    i = kasutajad.index(login)

    print("1 - Muuda kasutajanimi")
    print("2 - Muuda parool")
    valik = input("Valik: ")

    if valik == "1":
        uus = input("Sisesta uus kasutajanimi: ")
        if uus in kasutajad:
            print("Kasutajanimi juba olemas!")
        else:
            kasutajad[i] = uus
            print("Kasutajanimi muudetud!")

    elif valik == "2":
        while True:
            uus_psw = input("Sisesta uus parool: ")
            if parool_kehtiv(uus_psw):
                paroolid[i] = uus_psw
                print("Parool muudetud!")
                break
            else:
                print("Parool ei vasta nõuetele!")


def parooli_taastamine(kasutajad: list, paroolid: list) -> None:
    login = input("Sisesta kasutajanimi: ")

    if login not in kasutajad:
        print("Kasutajat ei leitud!")
        return

    i = kasutajad.index(login)
    uus_psw = genereeri_parool()
    paroolid[i] = uus_psw
    print("Sinu uus parool:", uus_psw)
