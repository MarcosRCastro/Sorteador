import random
DOC_NUMEROS_JA_SORTEADOS = #inclua a constante
DOC_RELACAO_DE_COMPRADORES = #inclua a constante

# Carregar números já sorteados
def ja_sorteados():
    with open(DOC_NUMEROS_JA_SORTEADOS, "r") as arquivo:
        ja_sorteados_str = []
        for num in arquivo:
            num = num[:-1]
            ja_sorteados_str.append(num)
        
        # Converter em números inteiros
        num_ja_sorteados = []
        for i in ja_sorteados_str:
            num_ja_sorteados.append(int(i))
        
        print("Os números já sorteados são:", sorted(num_ja_sorteados))


def sorteio(num_cotas):
    
    # Abrir numeros já sorteados
    limitador = 0
    sorteados_agora = []
    with open(DOC_NUMEROS_JA_SORTEADOS, "r") as leitura_arquivo:
        ja_sorteados_str = []
        for num in leitura_arquivo:
            num = num[:-1]
            ja_sorteados_str.append(num)
        
    # Converter para número inteiro
    num_ja_sorteados = []
    for i in ja_sorteados_str:
        num_ja_sorteados.append(int(i))

    with open(DOC_RELACAO_DE_COMPRADORES, "a") as relatorio_compradores:
        relatorio_compradores.write(" Numeros comprados: ")   

    # Realizar sorteio
    while limitador < num_cotas:
        sort = random.randint(0, 1000)    

        if sort not in num_ja_sorteados:
            print("O número sorteado foi:", sort)
            num_ja_sorteados.append(sort)
            sorteados_agora.append(sort)
            with open(DOC_NUMEROS_JA_SORTEADOS, "a") as arquivo:
                arquivo.write(str(sort) + "\n")
            with open(DOC_RELACAO_DE_COMPRADORES, "a") as relatorio_compradores:
                relatorio_compradores.write(str(sort) + " | ")
            limitador += 1
    
    # Listar numeros que foram sorteados agora
    print()
    print(f"Os numeros sortedos agora foram: {sorted(sorteados_agora)}")
    print()

    

    ja_sorteados()
    
# Verificar se existem numeros disponíveis para sorteio
def verificar_se_tem_numeros_disponiveis():

    # Abrir numeros já sorteados
    with open(DOC_NUMEROS_JA_SORTEADOS, "r") as leitura_arquivo:
        ja_sorteados_str = []
        for num in leitura_arquivo:
            num = num[:-1]
            ja_sorteados_str.append(num)
    
    # Fazer contagem dos já sorteados
    cotas_ja_sorteadas = len(ja_sorteados_str)
    cotas_restantes = (1000 - cotas_ja_sorteadas)

    print(f"Já foram sorteadas {cotas_ja_sorteadas} cotas.")
    print(f"Aindas existem {cotas_restantes} cotas disponíveis para sorteio")

    return

# Decidir se o sorterio sera realizado ou nao
def decidir_se_sera_sorteado(numCotas):

    # Abrir numeros já sorteados
    with open(DOC_NUMEROS_JA_SORTEADOS, "r") as leitura_arquivo:
        ja_sorteados_str = []
        for num in leitura_arquivo:
            num = num[:-1]
            ja_sorteados_str.append(num)
    
    # Fazer contagem dos já sorteados
    cotas_ja_sorteadas = len(ja_sorteados_str)
    num_cotas = numCotas

    # Decidir se havera ou nao o sorteio
    if (cotas_ja_sorteadas + numCotas) <= 1000:
        sorteio(num_cotas)
    
    else:
        print()
        print(f"O numero de cotas selecionadas para este sorteio ({numCotas}) excede a quantidade de cotas ainda disponivel, que e de {1000 - cotas_ja_sorteadas}")
        print("O programa sera encerrado, execute novamente para incluir novos compradores.")
        quit()



def inserir_comprador():
    print()
    nome = input("Insira o nome do comprador: ")
    print()
    tel = input("Insira o telefone: ")
    print()
    
    verificar_se_tem_numeros_disponiveis()

    cotas = input("Insira o número de cotas compradas: ")
    num_cotas = int(cotas)

    with open(DOC_RELACAO_DE_COMPRADORES, "a") as arquivo_compradores:

        arquivo_compradores.write("\n" + str(nome) + " | ")
        arquivo_compradores.write(str(tel) + " | ")
        arquivo_compradores.write(str(num_cotas) + " | ")

    
    decidir_se_sera_sorteado(num_cotas)


cotas_totais = list(range(0,1000))
inserir_comprador()
