attackerlist = []
defenderlist = []
speedsterlist = []
supportlist = []
allrounder = []


class Pokemon:
    __nome = ""
    __tipo = ""

    def __init__(self, nm, tp):
        self.__nome = nm
        self.__tipo = tp

    def getNome(self):
        return self.__nome

    def getTipo(self):
        return self.__tipo

    def setNome(self, nm):
        self.__nome = nm

    def setTipo(self, tp):
        self.__tipo = tp

    def exibirdados(self):
        return f"Nome: {self.__nome} Tipo: {self.__tipo}"


class Defender(Pokemon):
    __hp = ""
    __def = ""

    def __init__(self, nm, tp, h, defen):
        super().__init__(nm, tp)
        self.__hp = h
        self.__def = defen

    def gethp(self):
        return self.__hp

    def getdef(self):
        return self.__def

    def sethp(self, h):
        self.__hp = h

    def setdef(self, defen):
        self.__def = defen

    def exibirdadosD(self):
        return super().exibirdados() + f" Hp: {self.__hp} Def: {self.__def}"


class Attacker(Pokemon):
    __attack = ""
    __spattack = ""

    def __init__(self, nm, tp, attk, spttk):
        super().__init__(nm, tp)
        self.__attack = attk
        self.__spattack = spttk

    def getAttack(self):
        return self.__attack

    def getSpattack(self):
        return self.__spattack

    def setAttack(self, attk):
        self.__attack = attk

    def setSpattack(self, spttk):
        self.__spattack = spttk

    def exibirdadosA(self):
        return super().exibirdados(
        ) + f" Attack: {self.__attack} SpAttack: {self.__spattack}"


class Speedster(Pokemon):
    __speed = ""

    def __init__(self, nm, tp, spe):
        super().__init__(nm, tp)
        self.__speed = spe

    def getspeed(self):
        return self.__nome

    def setspeed(self, spe):
        self.__speed = spe

    def exibirdadosT(self):
        return super().exibirdados() + f" Speed {self.__speed}"

class Allrouder(Pokemon):

    __attack = ""
    __def = ""

    def __init__(self, nm, tp, attk, defen):
        super().__init__(nm, tp)
        self.__attack = attk
        self.__def = defen

    def getAttack(self):
        return self.__attack

    def getDef(self):
        return self.__def

    def setAttack(self, attk):
        self.__attack = attk

    def setDef(self, defen):
        self.__def = defen

    def exibirdadosR(self):
        return super().exibirdados(
        ) + f" Attack: {self.__attack} Def: {self.__def}"


class Support(Pokemon):
    __hp = ""
    __spdef = ""

    def __init__(self, nm, tp, h, spd):
        super().__init__(nm, tp)
        self.__hp = h
        self.__spdef = spd

    def getHp(self):
        return self.__hp

    def getSpdef(self):
        return self.__spdef

    def setHp(self, h):
        self.__hp = h

    def setSpdef(self, spd):
        self.__spdef = spd

    def exibirdadosS(self):
        return super().exibirdados(
        ) + f" Hp: {self.__hp} Spdef: {self.__spdef}"


lista = []
while (True):
    print("-" * 30)
    print("Bem-Vindo ao Unite DB!")
    print("(No Interface Mode)")
    print("-" * 30)
    print(" " + "MENU")
    print("1. Listar Pokes")
    print("2. Incluir Pokes")
    print("3. Remover Pokes")
    print("4. Exibir Pokes")
    print("5. Sair")
    print("-" * 30)
    op = int(input("Digite uma opção: "))
    if op == 5:
        break

    if op == 1:
        print("-" * 30)
        print("Listar Pokemon:")
        print("-" * 30)
        for c in lista:
            print(f"Nome: {c.getNome()} Tipo: {c.getTipo()}")
    elif op == 2:
        print("Tipos de Pokemon:")
        print("-" * 30)
        print("1. DEFENDER")
        print("2. ATTACKER")
        print("3. SPEEDSTER")
        print("4. ALL-ROUNDER")
        print("5. SUPORT")
        print("-" * 30)
        tipo = input("Informe o tipo de pokemon que você quer incluir: ")
        if tipo == "1":
            nm = input("Nome do Pokemon: ")
            h = input("HP do Pokemon: ")
            defen = input("DEFESA do Pokemon: ")
            pokemon = Defender(nm, "Defender", h, defen)
            lista.append(pokemon)
        elif tipo == "2":
            nm = input("Nome do Pokemon: ")
            attk = input("ATAQUE do Pokemon: ")
            spttk = input("SP.ATAQUE do Pokemon: ")
            pokemon = Attacker(nm, "Attacker", attk, spttk)
            lista.append(pokemon)
        elif tipo == "3":
            nm = input("Nome do Pokemon: ")
            spe = input("VELOCIDADE do Pokemon: ")
            pokemon = Speedster(nm, "Speedster", spe)
            lista.append(pokemon)
        elif tipo == "4":
            nm = input("Nome do Pokemon: ")
            attk = input("ATAQUE do Pokemon: ")
            defen = input("DEFESA do Pokemon: ")
            pokemon = Allrouder(nm, "Allrounder", attk, defen )
            lista.append(pokemon)
        elif tipo == "5":
            nm = input("Nome do Pokemon: ")
            h = input("HP do Pokemon: ")
            spd = input("SP.DEF do Pokemon: ")
            pokemon = Support(nm, "Suport", h, spd)
            lista.append(pokemon)
            print("Pokemon Incluido!")
        else:
            print("Tipo inválido!")
    elif op == 3:
        nome = input("Nome do Pokemon: ")
        check = False
        for c in lista:

            if c.getNome() == nome:
                lista.remove(c)
                print("Pokemon removido!")
                check = True
                break
        if not (check):
            print("Pokemon não localizado.")
    elif op == 4:
        nome = input("Nome do Pokemon: ")
        check = False
        for c in lista:

            if c.getNome() == nome:
                print(c.exibirdados())
                check = True
                break
        if not (check):
            print("Pokemon não localizado")
    else:
        print("Opção Inválida")
        print("-" * 30)
print("Fim")
