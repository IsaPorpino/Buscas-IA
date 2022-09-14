class Grafo:
    def __init__(self, lista_vizinhos):
        self.lista_vizinhos = lista_vizinhos

    def get_vizinhos(self, no_analise):
        return self.lista_vizinhos[no_analise]

    # função para checar a heuristica de cada nó
    def heuristica(self, n):
        heuristica = {
            'A': 50,
            'B': 45,
            'C': 40,
            'D': 42,
            'E': 42,
            'F': 32,
            'G': 28,
            'H': 25,
            'I': 30,
            'J': 57,
            'K': 38,
            'L': 29,
            'M': 18,
            'N': 20,
            'O': 22,
            'P': 29,
            'Q': 28,
            'R': 19,
            'S': 10,
            'T': 10,
            'U': 20,
            'V': 0,
        }
        return heuristica[n]

    def aestrela(self, inicio, objetivo):
        # borda é a lista de nós que já foram abertos mas que ainda não foram explorados
        # inicia com o nó inicial
        # a lista_fechada é a lista de nós que já foram explorados
        borda = [inicio]
        lista_fechada = []

        # dist_acumulada contém a distância do acumulada do inicio até o nó em análise
        # é inicializado em 0
        dist_acumulada = {}
        dist_acumulada[inicio] = 0

        # pai contém o mapeamento do nó pai de todos os nós
        pai = {}
        pai[inicio] = inicio

        # Enquanto existir nós na borda, o algoritmo será executado
        while len(borda) > 0:
            no_atual = None

            #consulta os nós da borda para encontrar nó com menor custo estimado
            for proximo_no in borda:
                if no_atual == None or dist_acumulada[proximo_no] + self.heuristica(proximo_no) < dist_acumulada[no_atual] + self.heuristica(no_atual):
                    no_atual = proximo_no

            # se o nó encontrado for o objetivo, o caminho é reconstruido pra dar o resultado
            if no_atual == objetivo:
                custo = dist_acumulada[no_atual]
                caminho = []

                #vai acrescentar os nós do caminho do fim até o inicio (que é pai de si mesmo)
                while pai[no_atual] != no_atual:
                    caminho.append(no_atual)
                    no_atual = pai[no_atual]

                caminho.append(inicio)

                #inverte a ordem do caminho pra ir do inicio até o objetivo
                caminho.reverse()

                print('\nCaminho Encontrado: {}'.format(caminho))
                print('\nCusto do caminho: ', custo)
                print('Borda: ', borda)
                print('lista fechada: ', lista_fechada)

                return caminho

            # checa todos os vizinhos do no atual para colocar na borda e colocar o custo
            for (vizinho, distancia) in self.get_vizinhos(no_atual):
                # se o viziho já está na lista fechada o algoritmo passa direto
                if vizinho in lista_fechada:
                    continue

                # se o vizinho já estiver na borda, checar se o caminho vindo do nó atual é
                # menos custoso que o custo anterior atribuido ao vizinho
                # se for menos custoso, atualiza os dados do custo acumulado do vizinho e qual seu pai
                elif vizinho in borda:
                    if dist_acumulada[vizinho] > dist_acumulada[no_atual] + distancia:
                        dist_acumulada[vizinho] = dist_acumulada[no_atual] + distancia
                        pai[vizinho] = no_atual
                    else:
                        continue

                # se o nó vizinho não está nem na borda nem na lista fechada, ele é acrescentado à borda
                # informa que o nó atual é pai do nó vizinho
                # calcula o custo para chegar no vizinho vindo do pai
                elif vizinho not in borda and vizinho not in lista_fechada:
                    borda.append(vizinho)
                    pai[vizinho] = no_atual
                    dist_acumulada[vizinho] = dist_acumulada[no_atual] + distancia

            borda.remove(no_atual)
            lista_fechada.append(no_atual)
            print('\n', borda)
            print(lista_fechada)

    def custo_uniforme(self, inicio, objetivo):
        # borda é a lista de nós que já foram abertos mas que ainda não foram explorados
        # inicia com o nó inicial
        # a lista_fechada é a lista de nós que já foram explorados
        borda = [inicio]
        lista_fechada = []

        # dist_acumulada contém a distância do acumulada do inicio até o nó em análise
        # é inicializado em 0
        dist_acumulada = {}
        dist_acumulada[inicio] = 0

        # pai contém o mapeamento do nó pai de todos os nós
        pai = {}
        pai[inicio] = inicio

        # Enquanto existir nós na borda, o algoritmo será executado
        while len(borda) > 0:
            no_atual = None

            # consulta os nós da borda para encontrar nó com menor custo acumulado
            for proximo_no in borda:
                if no_atual == None or dist_acumulada[proximo_no] < dist_acumulada[no_atual]:
                    no_atual = proximo_no

            # se o nó encontrado for o objetivo, o caminho é reconstruido pra dar o resultado
            if no_atual == objetivo:
                custo = dist_acumulada[no_atual]
                caminho = []

                # vai acrescentar os nós do caminho do fim até o inicio (que é pai de si mesmo)
                while pai[no_atual] != no_atual:
                    caminho.append(no_atual)
                    no_atual = pai[no_atual]

                caminho.append(inicio)

                # inverte a ordem do caminho pra ir do inicio até o objetivo
                caminho.reverse()

                print('\nCaminho Encontrado: {}'.format(caminho))
                print('\nCusto do caminho: ', custo)
                print('Borda: ', borda)
                print('lista fechada: ', lista_fechada)

                return caminho

            # checa todos os vizinhos do no atual para colocar na borda e colocar o custo
            for (vizinho, distancia) in self.get_vizinhos(no_atual):
                # se o viziho já está na lista fechada o algoritmo passa direto
                if vizinho in lista_fechada:
                    continue

                # se o vizinho já estiver na borda, checar se o caminho vindo do nó atual é
                # menos custoso que o custo anterior atribuido ao vizinho
                # se for menos custoso, atualiza os dados do custo acumulado do vizinho e qual seu pai
                elif vizinho in borda:
                    if dist_acumulada[vizinho] > dist_acumulada[no_atual] + distancia:
                        dist_acumulada[vizinho] = dist_acumulada[no_atual] + distancia
                        pai[vizinho] = no_atual
                    else:
                        continue

                # se o nó visinho não está nem na borda nem na lista fechada, ele é acrescentado à borda
                # informa que o nó atual é pai do nó vizinho
                # calcula o custo para chegar no vizinho vindo do pai
                elif vizinho not in borda and vizinho not in lista_fechada:
                    borda.append(vizinho)
                    pai[vizinho] = no_atual
                    dist_acumulada[vizinho] = dist_acumulada[no_atual] + distancia

            borda.remove(no_atual)
            lista_fechada.append(no_atual)
            print('\n', borda)
            print(lista_fechada)