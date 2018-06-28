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
        self.vizinhos.extend(adicionar)

    def print_noh(self):
        print(self)
        
        for colega in self.vizinhanca:
            print(colega)

    def __str__(self):
        return f"Nó {self.no_id} | Custo {self.custo} | Classe {self.classe}"
