class No:
    """
    Representa um nó na lista circular duplamente ligada.
    """
    def __init__(self, dado):
        self.dado = dado  # O conteúdo do nó (uma linha de texto)
        self.proximo = None  # Referência para o próximo nó
        self.anterior = None  # Referência para o nó anterior
        self.modificado = False  # Variável de controle para rastrear modificações
        self.nome_arquivo = None  # Adiciona um atributo para armazenar o nome do arquivo

class ListaCircularDuplamenteLigada:
    """
    Implementa uma lista circular duplamente ligada.
    """
    def __init__(self):
        self.cabeca = None  # Referência para o primeiro nó

    def esta_vazia(self):
        return self.cabeca is None

    def adicionar(self, dado):
        """
        Adiciona um novo nó ao final da lista.
        """
        novo_no = No(dado)
        if self.esta_vazia():
            self.cabeca = novo_no
            self.cabeca.proximo = self.cabeca
            self.cabeca.anterior = self.cabeca
        else:
            cauda = self.cabeca.anterior
            cauda.proximo = novo_no
            novo_no.anterior = cauda
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
        
        self.modificado = True  # Marca como modificado

    def adicionar_apos(self, posLin):
        """
        Permite a edição de uma ou mais linhas e insere na lista após a posição posLin.
        O término da entrada é dado por um ':a' em uma linha vazia.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return
        atual = self.cabeca
        linha_numero = 1
        while True:
            if linha_numero == posLin:
                while True:
                    nova_linha = input("Digite a nova linha (ou ':a' para terminar): ").strip()
                    if nova_linha == ':a':
                        break
                    novo_no = No(nova_linha)
                    novo_no.proximo = atual.proximo
                    novo_no.anterior = atual
                    atual.proximo.anterior = novo_no
                    atual.proximo = novo_no
                    atual = novo_no
                self.modificado = True
                print(f"Linhas adicionadas após a linha {posLin}.")
                return
            atual = atual.proximo
            linha_numero += 1
            if atual == self.cabeca:
                break
        print(f"Linha {posLin} não encontrada.")

    def adicionar_antes(self, posLin):
        """
        Permite a edição de uma ou mais linhas e insere na lista antes da posição posLin.
        O término da entrada é dado por um ':i' em uma linha vazia.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return
        atual = self.cabeca
        linha_numero = 1
        while True:
            if linha_numero == posLin:
                while True:
                    nova_linha = input("Digite a nova linha (ou ':i' para terminar): ").strip()
                    if nova_linha == ':i':
                        break
                    novo_no = No(nova_linha)
                    novo_no.proximo = atual
                    novo_no.anterior = atual.anterior
                    atual.anterior.proximo = novo_no
                    atual.anterior = novo_no
                    atual = novo_no
                self.modificado = True
                print(f"Linhas adicionadas antes da linha {posLin}.")
                return
            atual = atual.proximo
            linha_numero += 1
            if atual == self.cabeca:
                break
        print(f"Linha {posLin} não encontrada.")

    def editar_linha(self, lin):
        """
        Permite editar o conteúdo de uma linha específica.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1

        while True:
            if linha_numero == lin:
                print(f"Linha atual ({linha_numero}): {atual.dado}")
                novo_conteudo = input("Digite o novo conteúdo para a linha: ").strip()
                atual.dado = novo_conteudo
                self.modificado = True  # Marca como modificado
                print(f"Linha {linha_numero} atualizada com sucesso.")
                return
            atual = atual.proximo
            linha_numero += 1

            if atual == self.cabeca:
                break

        print(f"Linha {lin} não encontrada.")

    def editar_varias_linhas(self):
        """
        Realiza a edição de várias linhas, zera a lista e as insere.
        O término da entrada é dado por um ':o' em uma linha vazia.
        """
        self.cabeca = None
        while True:
            nova_linha = input("Digite a nova linha (ou ':o' para terminar): ").strip()
            if nova_linha == ':o':
                break
            self.adicionar(nova_linha)
        self.modificado = True
        print("Edição de várias linhas concluída.")

    def exibir_sem_numeracao(self):
        """
        Exibe todo o conteúdo da lista circular duplamente ligada sem a numeração das linhas.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca

        while True:
            print(atual.dado)
            atual = atual.proximo

            if atual == self.cabeca:
                break

    def exibir(self):
        """
        Exibe o conteúdo da lista circular duplamente ligada.
        Exibe 10 linhas por vez, numeradas.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1
        linhas_exibidas = 0

        while True:
            print(f"{linha_numero}: {atual.dado}")
            atual = atual.proximo
            linha_numero += 1
            linhas_exibidas += 1

            if atual == self.cabeca:
                break

            if linhas_exibidas == 10:
                continuar = input("Exibir mais 10 linhas? (s/n): ").strip().lower()
                if continuar != 's':
                    break
                linhas_exibidas = 0

    def carregar_arquivo(self, nome_arquivo):
        """
        Carrega um arquivo de texto e armazena cada linha na lista circular duplamente ligada.
        Em seguida, exibe o conteúdo carregado sem a numeração das linhas.
        """
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    self.adicionar(linha.rstrip("\n"))
            self.nome_arquivo = nome_arquivo
            self.modificado = False
            print(f"Arquivo '{nome_arquivo}' carregado com sucesso.")
            self.exibir_sem_numeracao()
        except FileNotFoundError:
            print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")

    def salvar_arquivo(self, nome_arquivo):
        """
        Salva o conteúdo da lista circular duplamente ligada em um arquivo de texto.
        """
        try:
            with open(nome_arquivo, 'w') as arquivo:
                atual = self.cabeca
                if atual:
                    while True:
                        arquivo.write(atual.dado + '\n')
                        atual = atual.proximo
                        if atual == self.cabeca:
                            break
            print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")

    def salvar_e_sair(self):
        """
        Salva o conteúdo da lista circular duplamente ligada em um arquivo de texto e sai do editor.
        """
        if self.nome_arquivo:
            self.salvar_arquivo(self.nome_arquivo)
            print("Saindo do editor...")
            exit()
        else:
            print("Erro: Nenhum arquivo carregado para salvar.")

    def copiar(self, lin_ini, lin_fim):
        """
        Copia o texto do intervalo de linhas especificado (lin_ini a lin_fim).
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1
        self.buffer = []

        while True:
            if linha_numero >= lin_ini and linha_numero <= lin_fim:
                self.buffer.append(atual.dado)
            atual = atual.proximo
            linha_numero += 1

            if atual == self.cabeca or linha_numero > lin_fim:
                break

        self.modificado = False

        print(f"Texto copiado das linhas {lin_ini} a {lin_fim}.")

    def cortar(self, lin_ini, lin_fim):
        """
        Corta o texto do intervalo de linhas especificado (lin_ini a lin_fim).
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1
        self.buffer = []

        while True:
            proximo = atual.proximo
            if linha_numero >= lin_ini and linha_numero <= lin_fim:
                self.buffer.append(atual.dado)
                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                if atual == self.cabeca:
                    self.cabeca = proximo
            atual = proximo
            linha_numero += 1

            if atual == self.cabeca or linha_numero > lin_fim:
                break

        self.modificado = True  # Marca como modificado

        print(f"Texto cortado das linhas {lin_ini} a {lin_fim}.")

    def colar(self, lin_ini_paste):
        """
        Cola o texto copiado ou cortado a partir da linha especificada (lin_ini_paste).
        """
        if not hasattr(self, 'buffer') or not self.buffer:
            print("Nenhum texto copiado ou cortado para colar.")
            return

        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1

        while True:
            if linha_numero == lin_ini_paste:
                for dado in self.buffer:
                    novo_no = No(dado)
                    novo_no.proximo = atual.proximo
                    novo_no.anterior = atual
                    atual.proximo.anterior = novo_no
                    atual.proximo = novo_no
                    atual = novo_no
            atual = atual.proximo
            linha_numero += 1

            if atual == self.cabeca or linha_numero > lin_ini_paste + len(self.buffer):
                break

        self.modificado = True  # Marca como modificado

        print(f"Texto colado a partir da linha {lin_ini_paste}.")

    def excluir_linha(self, lin):
        """
        Exclui uma linha específica (lin).
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1

        while True:
            if linha_numero == lin:
                if atual == self.cabeca:
                    self.cabeca = atual.proximo
                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                print(f"Linha {lin} excluída.")
                return
            atual = atual.proximo
            linha_numero += 1

            if atual == self.cabeca:
                break

        self.modificado = True  # Marca como modificado

        print(f"Linha {lin} não encontrada.")

    def excluir_ate_inicio(self, lin):
        """
        Apaga da linha lin até o início da lista.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1

        while True:
            proximo = atual.proximo
            if linha_numero <= lin:
                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                if atual == self.cabeca:
                    self.cabeca = proximo
            atual = proximo
            linha_numero += 1

            if atual == self.cabeca or linha_numero > lin:
                break

        self.modificado = True  # Marca como modificado

        print(f"Linhas da {lin} até o início excluídas.")

    def excluir_ate_final(self, lin):
        """
        Exclui a partir de uma linha específica (lin) até o final.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1

        while True:
            proximo = atual.proximo
            if linha_numero >= lin:
                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                if atual == self.cabeca:
                    self.cabeca = proximo
            atual = proximo
            linha_numero += 1

            if atual == self.cabeca:
                break

        self.modificado = True  # Marca como modificado

        print(f"Linhas a partir da {lin} até o final excluídas.")

    def exibir_linha(self, lin):
        """
        Exibe uma linha específica (lin).
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1

        while True:
            if linha_numero == lin:
                print(f"{linha_numero}: {atual.dado}")
                return
            atual = atual.proximo
            linha_numero += 1

            if atual == self.cabeca:
                break

        print(f"Linha {lin} não encontrada.")

    def exibir_intervalo(self, lin_ini, lin_fim):
        """
        Exibe um intervalo de linhas especificado (lin_ini a lin_fim).
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1

        while True:
            if linha_numero >= lin_ini and linha_numero <= lin_fim:
                print(f"{linha_numero}: {atual.dado}")
            atual = atual.proximo
            linha_numero += 1

            if atual == self.cabeca or linha_numero > lin_fim:
                break

    def sair(self):
        """
        Sai do editor, verificando se há modificações não salvas.
        """
        if self.modificado:
            print("Há modificações não salvas. Use ':q!' para sair sem salvar.")
        else:
            print("Saindo do editor...")
            exit()

    def sair_sem_salvar(self):
        """
        Sai do editor sem salvar as modificações.
        """
        print("Saindo do editor sem salvar...")
        exit()

    def gravar_se_alterado(self, nome_arquivo):
        """
        Grava o conteúdo em arquivo, se alterado.
        """
        if self.modificado:
            self.salvar_arquivo(nome_arquivo)
            self.modificado = False
            print(f"Conteúdo gravado em '{nome_arquivo}'.")
        else:
            print("Nenhuma modificação a ser salva.")

    def marcar_texto(self, lin_ini, lin_fim):
        """
        Marca um texto da lista (para cópia ou corte) de lin_ini até lin_fim.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        if lin_ini > lin_fim or lin_ini < 1:
            print("Intervalo inválido.")
            return

        atual = self.cabeca
        linha_numero = 1
        self.buffer = []

        while True:
            if linha_numero >= lin_ini and linha_numero <= lin_fim:
                self.buffer.append(atual.dado)
            atual = atual.proximo
            linha_numero += 1

            if atual == self.cabeca or linha_numero > lin_fim:
                break

        print(f"Texto marcado das linhas {lin_ini} a {lin_fim}.")

    def localizar_elemento(self, elemento):
        """
        Percorre a lista, localiza a(s) linha(s) na(s) qual(is) o(s) elemento(s) encontra(m)-se e exibi-la(s) por completo.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1
        encontrado = False

        while True:
            if elemento in atual.dado:
                print(f"{linha_numero}: {atual.dado}")
                encontrado = True
            atual = atual.proximo
            linha_numero += 1

            if atual == self.cabeca:
                break

        if not encontrado:
            print(f"Elemento '{elemento}' não encontrado.")

    def substituir_elemento(self, elem, elem_troca):
        """
        Percorre a lista, localiza o elem e realiza a troca por elem_troca em todas as linhas do código fonte.
        """
        if self.esta_vazia():
            print("A lista está vazia.")
            return

        atual = self.cabeca
        linha_numero = 1
        encontrado = False

        while True:
            if elem in atual.dado:
                atual.dado = atual.dado.replace(elem, elem_troca)
                print(f"Linha {linha_numero}: '{elem}' substituído por '{elem_troca}'.")
                encontrado = True
            atual = atual.proximo
            linha_numero += 1

            if atual == self.cabeca:
                break

        if not encontrado:
            print(f"Elemento '{elem}' não encontrado.")
        else:
            self.modificado = True

    def exibir_ajuda(self):
        """
        Exibe os comandos disponíveis no editor de texto com suas descrições, em blocos de 5 comandos.
        """
        comandos = [
            (":e <nome_arquivo>", "Carregar um arquivo de texto no editor."),
            (":w", "Salvar as modificações no arquivo atualmente carregado."),
            (":w <nome_arquivo>", "Salvar as modificações no arquivo especificado."),
            (":wq", "Salvar as modificações e sair do editor."),
            (":q!", "Sair do editor sem salvar as modificações."),
            (":ZZ", "Gravar conteúdo em arquivo, se alterado."),
            (":v LinIni LinFim", "Marcar um texto da lista (para cópia ou corte) de LinIni até LinFim."),
            (":y", "Copiar o texto marcado para uma lista de cópia."),
            (":c", "Cortar o texto marcado."),
            (":p LinIniPaste", "Colar o texto copiado ou cortado a partir da linha especificada."),
            (":s", "Exibir o conteúdo completo do programa com o número de cada linha."),
            (":s Lin", "Exibir o conteúdo da linha especificada."),
            (":s LinIni LinFim", "Exibir um intervalo de linhas do programa."),
            (":x Lin", "Apagar a linha de posição Lin."),
            (":xG Lin", "Apagar a partir da linha Lin até o final da lista."),
            (":XG Lin", "Apagar da linha Lin até o início da lista."),
            (":/ elemento", "Localizar e exibir linhas que contêm o elemento especificado."),
            (":/ elem elemTroca", "Substituir elem por elemTroca em todas as linhas."),
            (":o", "Realizar a edição de várias linhas e inserir na lista."),
            (":a posLin", "Adicionar linhas após a posição posLin."),
            (":i posLin", "Adicionar linhas antes da posição posLin."),
            (":help", "Exibir os comandos disponíveis no editor.")
        ]
        
        # Exibe os comandos em blocos de 5
        for i in range(0, len(comandos), 5):
            for comando, descricao in comandos[i:i+5]:
                print(f"{comando} - {descricao}")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    lista = ListaCircularDuplamenteLigada()
    print("Editor de Texto - Digite ':help' para listar os comandos disponíveis.")

    while True:
        comando = input("Digite um comando: ").strip()
        if comando.startswith(":edit"):
            partes = comando.split()
            if len(partes) == 2 and partes[1].isdigit():
                lin = int(partes[1])
                lista.editar_linha(lin)
            else:
                print("Erro: Você deve especificar o número da linha após ':edit'.")
        elif comando.startswith(":e"):
            partes = comando.split(maxsplit=1)
            if len(partes) == 2:
                nome_arquivo = partes[1]
                lista.carregar_arquivo(nome_arquivo)
            else:
                print("Erro: Você deve especificar o nome do arquivo após ':e'.")
        elif comando == ":help":
            lista.exibir_ajuda()
        elif comando == ":s":
            lista.exibir()
        elif comando.startswith(":s "):
            partes = comando.split()
            if len(partes) == 2:
                lin = int(partes[1])
                lista.exibir_linha(lin)
            elif len(partes) == 3:
                lin_ini = int(partes[1])
                lin_fim = int(partes[2])
                lista.exibir_intervalo(lin_ini, lin_fim)
            else:
                print("Erro: Você deve especificar a linha ou intervalo de linhas após ':s'.")
        elif comando == ":wq":
            lista.salvar_e_sair()        
        elif comando == ":w":
            if lista.nome_arquivo:  
                lista.salvar_arquivo(lista.nome_arquivo)
                lista.modificado = False  # Marca como não modificado após salvar
            else:
                print("Erro: Nenhum arquivo carregado para salvar. Use ':w <nome_arquivo>'.")
        elif comando.startswith(":w "):
            partes = comando.split(maxsplit=1)
            if len(partes) == 2:
                nome_arquivo = partes[1]
                lista.salvar_arquivo(nome_arquivo)
                lista.modificado = False  # Marca como não modificado após salvar
            else:
                print("Erro: Você deve especificar o nome do arquivo após ':w'.")
        elif comando == ":q!":
            lista.sair_sem_salvar()
        elif comando == ":q":
            lista.sair()
        elif comando == ":ZZ":
            partes = comando.split(maxsplit=1)
            if len(partes) == 2:
                nome_arquivo = partes[1]
                lista.gravar_se_alterado(nome_arquivo)
            else:
                print("Erro: Você deve especificar o nome do arquivo após ':ZZ'.")
        elif comando.startswith(":y"):
            partes = comando.split()
            if len(partes) == 3:
                lin_ini = int(partes[1])
                lin_fim = int(partes[2])
                lista.copiar(lin_ini, lin_fim)
            else:
                print("Erro: Você deve especificar as linhas inicial e final após ':y'.")
        elif comando.startswith(":c"):
            partes = comando.split()
            if len(partes) == 3:
                lin_ini = int(partes[1])
                lin_fim = int(partes[2])
                lista.cortar(lin_ini, lin_fim)
            else:
                print("Erro: Você deve especificar as linhas inicial e final após ':c'.")
        elif comando.startswith(":p"):
            partes = comando.split()
            if len(partes) == 2:
                lin_ini_paste = int(partes[1])
                lista.colar(lin_ini_paste)
            else:
                print("Erro: Você deve especificar a linha inicial para colar após ':p'.")
        elif comando.startswith(":x "):
            partes = comando.split()
            if len(partes) == 2:
                lin = int(partes[1])
                lista.excluir_linha(lin)
            else:
                print("Erro: Você deve especificar a linha a ser excluída após ':x'.")
        elif comando.startswith(":xG "):
            partes = comando.split()
            if len(partes) == 2:
                lin = int(partes[1])
                lista.excluir_ate_final(lin)
            else:
                print("Erro: Você deve especificar a linha inicial após ':xG'.")
        elif comando.startswith(":XG "):
            partes = comando.split()
            if len(partes) == 2:
                lin = int(partes[1])
                lista.excluir_ate_inicio(lin)
            else:
                print("Erro: Você deve especificar a linha inicial após ':XG'.")
        elif comando.startswith(":/ "):
            partes = comando.split(maxsplit=2)
            if len(partes) == 2:
                # Caso de busca simples
                elemento = partes[1]
                lista.localizar_elemento(elemento)
            elif len(partes) == 3:
                # Caso de substituição
                elem = partes[1]
                elem_troca = partes[2]
                lista.substituir_elemento(elem, elem_troca)
            else:
                print("Erro: Comando inválido. Use ':/ elemento' para buscar ou ':/ elem elemTroca' para substituir.")
        elif comando.startswith(":v"):
            partes = comando.split()
            if len(partes) == 3:
                lin_ini = int(partes[1])
                lin_fim = int(partes[2])
                lista.marcar_texto(lin_ini, lin_fim)
            else:
                print("Erro: Você deve especificar as linhas inicial e final após ':v'.")
        elif comando.startswith(":a "):
            partes = comando.split()
            if len(partes) == 2:
                posLin = int(partes[1])
                lista.adicionar_apos(posLin)
            else:
                print("Erro: Você deve especificar a posição após a qual adicionar as linhas após ':a'.")
        elif comando.startswith(":i "):
            partes = comando.split()
            if len(partes) == 2:
                posLin = int(partes[1])
                lista.adicionar_antes(posLin)
            else:
                print("Erro: Você deve especificar a posição antes da qual adicionar as linhas após ':i'.")
        elif comando == ":o":
            lista.editar_varias_linhas()
        else:
            print("Comando não reconhecido. Tente novamente.")