class Pracownik:
    def __init__(self, imie, placa):
        pozioma = float(placa)
        poziomb = float(placa)
        poziomc = round(round(pozioma * 0.0976, 2) + round(pozioma * 0.015, 2) + round(pozioma * 0.0245, 2), 2)
        poziomd = poziomb - poziomc
        poziome = round(poziomd * 0.09, 2)
        poziomf = round(poziomd * 0.0775, 2)
        poziomg = 111.25
        poziomh = round(pozioma - poziomg - poziomc)
        poziomi = round((poziomh * 0.18), 2) - 46.33
        poziomj = round(poziomi - poziomf)
        poziomk = round(pozioma - poziomc - poziome - poziomj, 2)
        pozioml = round(pozioma * 0.0976, 2) + round(pozioma * 0.065, 2) + round(pozioma * 0.0193, 2) + round(pozioma * 0.0245, 2) + round(pozioma * 0.001, 2)
        poziomm = pozioma + pozioml
        self.imiepracownika = imie
        self.wynagrodzeniepracownikanetto = poziomk
        self.skladkipracodawcy = pozioml
        self.lacznykosztpracownika = poziomm

sumakosztupracodawcy = 0
y = []
i = input().strip()
j = 1
while j <= int(i):
    x = []
    x.append(input().strip().split())
    moj_pracownik = Pracownik(x[0][0], int(x[0][1]))
    y.append(moj_pracownik.imiepracownika)
    y.append(moj_pracownik.wynagrodzeniepracownikanetto)
    y.append(moj_pracownik.skladkipracodawcy)
    y.append(moj_pracownik.lacznykosztpracownika)
    j = j + 1
    sumakosztupracodawcy = sumakosztupracodawcy + moj_pracownik.lacznykosztpracownika

j = 0
while j < len(y):
    print(y[j], format(y[j+1],'.2f'), format(y[j+2],'.2f'), format(y[j+3],'.2f'))
    j = j + 4

print(sumakosztupracodawcy)