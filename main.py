from buscas import Grafo

def principal():
    i = 1

    lista_vizinhos = {
        'A': [('B', 10), ('C', 11), ('D', 13)],
        'B': [('A', 10), ('F', 14), ('E', 14)],
        'C': [('A', 11), ('G', 10), ('H', 10)],
        'D': [('A', 13), ('I', 10), ('J', 10)],
        'E': [('B', 14), ('K', 11), ('L', 14)],
        'F': [('B', 14), ('G', 10), ('L', 12), ('M', 14)],
        'G': [('C', 10), ('F', 10), ('M', 10)],
        'H': [('C', 10), ('N', 10)],
        'I': [('D', 10), ('N', 10), ('O', 10)],
        'J': [('D', 10)],
        'K': [('E', 11), ('P', 10)],
        'L': [('E', 14), ('F', 12), ('R', 11), ('Q', 10)],
        'M': [('F', 14), ('G', 10), ('R', 14), ('S', 10)],
        'N': [('H', 10), ('I', 10), ('T', 12)],
        'O': [('I', 10), ('T', 13)],
        'P': [('K', 10), ('U', 10)],
        'Q': [('L', 10), ('U', 10)],
        'R': [('L', 11), ('M', 14), ('S', 10)],
        'S': [('M', 10), ('R', 10), ('V', 10)],
        'T': [('N', 12), ('O', 13), ('V', 10)],
        'U': [('P', 10), ('Q', 10), ('V', 21)],
        'V': [('S', 10), ('T', 10), ('U', 21)],
    }

    grafo = Grafo(lista_vizinhos)

    while i == 1:
        escolha = int(input('\nQual Busca Deseja Fazer? \n1-Custo Uniforme\n2-A*\n3-Encerrar o Programa\n'))

        if(escolha == 3):
            i ==3
            print("Programa Encerrado")
            break

        elif (escolha == 1):
            inicio = input('Escolha um nó para começar:\n A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V \n').upper()
            objetivo = input('Escolha um nó objetivo:\n A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V \n').upper()
            grafo.custo_uniforme(inicio, objetivo)

        elif (escolha == 2):
            inicio = input('Escolha um nó para começar:\n A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T \n').upper()
            grafo.aestrela(inicio, 'V')


if __name__ == '__main__':
    principal();