# DEFINICOES DE CLASSES

class Noh:
    """
    Esta classe define o Nó de um grafo
    É instanciado com um identificador (String) e a classe pertencente
    """

    def __init__(self, no_id, classe):
        self.no_id = no_id
        self.classe = classe
        self.dono = None
        self.distancia = 0
        self.custo = 10000
        self.estado = ''
        self.vizinhanca = []
        self.foi_visitado = False

    def inserir_na_vizinhanca(self, adicionar):
        #Posso adicionar tanto um quanto uma lista de vizinhos
        self.vizinhanca.extend(adicionar)

    def print_noh(self):
        print(self)
        
        for colega in self.vizinhanca:
            print(colega)

    def __str__(self):
        return f"Nó {self.no_id} | Custo {self.custo} | Classe {self.classe}"


class Colega:
    """
    Esta classe define um vizinho que será adicionado a um Noh
    Recebe como parametro o No e o seu peso
    """

    def __init__(self, noh, peso):
        self.noh = noh
        self.peso = peso
        self.e_melhor = False

    def __str__(self):
        if self.e_melhor:
            return f"Nó {self.noh.no_id}(Peso: {self.peso}) | PERTENCE AO CAMINHO MINIMO"
        else:
            return f"Nó {self.noh.no_id}(Peso: {self.peso})"


# FUNCOES

def get_menor_peso(coleguinhas):
    menor = coleguinhas[0]

    for colega in coleguinhas:
        if (not colega.noh.foi_visitado) and (menor.peso > colega.peso) :
            menor = colega
    
    return menor

def get_menor_custo(noh_list):
    menor = noh_list[0]
    for noh in noh_list:
        if menor.custo > noh.custo:
            menor = noh
    
    return menor

def add_amostra(noh_list):
    custos_list = []
    print("Adicionando amostras de Teste")
    for noh in noh_list:
        peso = int(input(f'Qual o peso da aresta conectada a {noh.no_id}?'))
        if peso > noh.custo:
            custos_list.append(peso)
        else:
            custos_list.append(noh.custo)
        
    indice_menor = 0
    for i, custo in enumerate(custos_list):
        if custos_list[indice_menor] > custo:
            indice_menor = i

    return noh_list[indice_menor].classe, custos_list[indice_menor]


def get_melhores(grafo):
    nao_visitei = []
    melhores = []
    atual = grafo[0]
    ja_foi = 0

    while ja_foi < len(grafo):
        atual.foi_visitado = True
        ja_foi += 1

        for colega in atual.vizinhanca:
            if not colega.noh.foi_visitado:
                nao_visitei.append(colega)

        menor_peso = get_menor_peso(nao_visitei)

        menor_peso.e_melhor = True
        melhores.append((atual, menor_peso))
        atual = menor_peso.noh
        
    ultimo = melhores[-1]
    
    melhores.append((ultimo[1].noh, None))
    return melhores
    