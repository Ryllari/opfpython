from opf import *

    
noh_1 = Noh('noh_1', 'Classe1')
noh_2 = Noh('noh_2', 'Classe2')
noh_3 = Noh('noh_3', 'Classe3')
noh_4 = Noh('noh_4', 'Classe1')
noh_5 = Noh('noh_5', 'Classe2')

noh_1.inserir_na_vizinhanca([
    Colega(noh_2, 4),
    Colega(noh_3, 12),
    Colega(noh_4, 7),
    Colega(noh_5, 15),
])

noh_2.inserir_na_vizinhanca([
    Colega(noh_1, 14),
    Colega(noh_3, 21),
    Colega(noh_4, 10),
    Colega(noh_5, 1),
])

noh_3.inserir_na_vizinhanca([
    Colega(noh_2, 5),
    Colega(noh_1, 2),
    Colega(noh_4, 20),
    Colega(noh_5, 13),
])

noh_4.inserir_na_vizinhanca([
    Colega(noh_2, 6),
    Colega(noh_3, 18),
    Colega(noh_1, 5),
    Colega(noh_5, 4),
])

noh_5.inserir_na_vizinhanca([
    Colega(noh_2, 17),
    Colega(noh_3, 12),
    Colega(noh_4, 3),
    Colega(noh_1, 1),
])

grafo = [noh_1, noh_2, noh_3, noh_4, noh_5]

# MAIN
if __name__ == "__main__":
    print("Vamos Comecar!")
    print("Estado Inicial do Grafo:")
    for noh in grafo:
        noh.print_noh()

    melhor = get_melhores(grafo)
    for dado in melhor:
        noh = dado[0]
        colega = dado[1]
        if (not colega is None) and (noh.classe != colega.noh.classe):
            noh.custo = 0
            colega.noh.custo = 0

    print("\n Grafo Caminho Mínimo:")
    for noh in grafo:
        noh.print_noh()
            
    while len(grafo) != 0:
        menor = get_menor_custo(grafo)

        for colega in menor.vizinhanca:
            if colega.peso < colega.noh.custo:
                colega.noh.custo = colega.peso
                colega.noh.classe = menor.classe
                colega.noh.conquistador = menor
        
        grafo.remove(menor)
    
    grafo = [noh_1, noh_2, noh_3, noh_4, noh_5]

    print("\n Grafo Custo Atualizado:")
    for noh in grafo:
        noh.print_noh()

    resultado = add_amostra(grafo)

    print(f'\nResultado: Clase {resultado[0]} | Custo {resultado[1]}')


