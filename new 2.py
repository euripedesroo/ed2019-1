#First In, First Out
#coding:latin1
class cadastro():
    def _init_(self, cpf = None, idi = None, fone =None):
        self.cpf = cpf
        self.idi = idi
        self.fone = fone

    def main():
        l = [None, None, None, None]
        op = 0
        topo = 0
        base = -1
		cont = 0
        print("escolha uma das opcoes abaixo")
        print("1. cadastro")
        print("2. remover")
        print("3. imprimir")
        while(op < 4):
            if (op == 1):
                inserir(topo, base, l)
            elif(op == 2):
                remover(topo, base, l)
            elif(op == 3):
                print(topo, base, l)

    def inserir(topo, base, l):
#fazer inserção dos dados
        if(base <4):
            l.cadastro = cadastro()
            l.base =  base+1
            print("insira os dados abaixo")
            l.cpf = int(input ("insira o cpf"))
            l.fone = int(input("insira o telefone"))
            l.idi = l.idi+1
            base = base+1
			cont = cont+1
            return base

        else:
            if (topo == 0):
                print("pilha cheia")
            else:
                j = 0
                for j in range (topo, base+1):
                    l[j] = l[cont]
                    j=j+1
                for j in range (j,6):
                    l[j] = None
                    print("compactou")

    def remover(topo, base, l):
        select = 0
        pos = 0
        if (cauda == -1):
            print("pilha vazia")

        else:
            for cont in range(topo, base+1):
                print("selecione a posição que vc quer remover")
                print("1. base")
                print("2. topo")
                print("3. posicao especifica")
                while(select <3):
                    if (select == 1):
                        l[cont].base == None
                    elif(select ==2):
                        l[cont].topo = None
                    elif(select == 3):
                        l[cont] = int(input("digite a prosicao a ser removida"))
                        l[cont] = None
						

    def imprimir(topo, base, l):
        if (cauda == -1):
            print("pilha vazia")
        else:
            for i in range (topo, base+1):
                print("")
                print(l[i].idi)
                print(l[i].cpf)
                print(l[i].fone)
main()







