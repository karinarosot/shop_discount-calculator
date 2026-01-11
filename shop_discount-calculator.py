wiek = int(input("Podaj wiek: "))
kwota = int(input("Podaj kwote twoich zakupow: "))
rabat = kwota * 0.2
kwota_po_rabacie = kwota - rabat
if wiek < 18 or wiek > 65:
    print("Twoja cena po rabacie to: ", float(kwota_po_rabacie))
else:
    print("przykro mi nie spelniasz warunków do przyznania rabatu :(")

pasi = input("czy pasuje ci ta kwota?")
if pasi == "yes":
    print("to fajnie kupuj u nas wiecej :)))")
if pasi == "no" and (wiek < 18 or wiek > 65):
    inny = float(input("A ile % bys chcial?"))
    procent = float(1 - (inny / 100))
    if inny > 50:
        print("nie ma opcji, to biedra")
    else:
        print("okej twoja obecna cena z kartka biedronka, to: ", float(kwota_po_rabacie*procent))
if pasi == "no" and wiek < 65:
    lat = int("65")- wiek
    print("nie mozemy przyznac ci rabatu nawet jesli cena ci sie nie podoba, przyjdz za", lat, "lat po wiekszy rabat")
if pasi == "no" and wiek < 18:
    lat_dwa = int("18")- wiek
    print("nie mozemy przyznac ci rabatu nawet jesli cena ci sie nie podoba, przyjdz za ", lat_dwa, "lat po wiekszy rabat")








