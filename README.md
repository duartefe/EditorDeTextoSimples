# Editor de Texto Simples

## Introdução

Este é um editor de texto simples, desenvolvido em Python, baseado no editor Vi do Linux. Ele permite que você edite e manipule arquivos de texto utilizando uma lista circular duplamente ligada. O programa é orientado por teclas e oferece comandos semelhantes aos do Vi para realizar ações de edição, como abrir arquivos, salvar, buscar, substituir e manipular o texto.

## Requisitos

- **Python**: 3.13.0 ou superior
- **Sistema operacional**: Windows 10 (recomendado para testes)
- **Editor de código**: Visual Studio Code
- **Bibliotecas**: Não há dependências externas além da biblioteca padrão do Python.

## Instruções de Execução

1. Salve todos os arquivos do exercício na mesma pasta.
2. Execute o arquivo `EP1.py`:
   1. Abra o arquivo no Visual Studio Code e execute com o comando "F5"
   2. Ou abra um prompt de comando (Cmd), navegue até a pasta onde os arquivos estão localizados e execute o comando:
      ```bash
      python EP1.py
      ```
3. O programa iniciará um loop de comandos onde você poderá interagir com o editor, carregando um arquivo de texto, realizando modificações e salvando as alterações.

## Comandos Disponíveis

A seguir estão os comandos disponíveis no editor, com suas descrições:

### Comandos de Arquivo

- `:e <nome_arquivo>`: Carregar um arquivo de texto no editor e exibir seu conteúdo.
- `:w`: Salvar as modificações no arquivo atualmente carregado.
- `:w <nome_arquivo>`: Salvar as modificações no arquivo especificado.
- `:wq`: Salvar as modificações e sair do editor.
- `:q!`: Sair do editor sem salvar as modificações.
- `:ZZ`: Gravar conteúdo em arquivo, se alterado.

### Comandos de Edição de Texto

- `:v LinIni LinFim`: Marcar um texto da lista (para cópia ou corte) de `LinIni` até `LinFim`.
- `:y`: Copiar o texto marcado para uma lista de cópia.
- `:c`: Cortar o texto marcado.
- `:p LinIniPaste`: Colar o texto copiado ou cortado a partir da linha especificada.
- `:s`: Exibir o conteúdo completo do programa com o número de cada linha.
- `:s Lin`: Exibir o conteúdo da linha especificada.
- `:s LinIni LinFim`: Exibir um intervalo de linhas do programa.
- `:x Lin`: Apagar a linha de posição `Lin`.
- `:xG Lin`: Apagar a partir da linha `Lin` até o final da lista.
- `:XG Lin`: Apagar da linha `Lin` até o início da lista.

### Comandos de Busca e Substituição

- `:/ elemento`: Localizar e exibir linhas que contêm o elemento especificado.
- `:/ elem elemTroca`: Substituir `elem` por `elemTroca` em todas as linhas.

### Comandos de Modificação e Adição

- `:o`: Realizar a edição de várias linhas e inserir na lista.
- `:a posLin`: Adicionar linhas após a posição `posLin`.
- `:i posLin`: Adicionar linhas antes da posição `posLin`.

### Comando de Ajuda

- `:help`: Exibir os comandos disponíveis no editor.

## Exemplos de Testes

1. **Carregar Arquivo**
   - Comando: `:e teste.txt`
   - Saída esperada: O arquivo `teste.txt` será carregado e seu conteúdo será exibido na tela. Se o arquivo não for encontrado, será exibida uma mensagem de erro.

2. **Salvar Modificações**
   - Comando: `:w`
   - Saída esperada: O arquivo carregado será salvo com as modificações realizadas. Se não houver um arquivo carregado, será exibido um erro informando que é necessário especificar um arquivo.

3. **Substituir Texto**
   - Comando: `:/ 15 16`
   - Saída esperada: Todas as ocorrências de `15` serão substituídas por `16` nas linhas do arquivo carregado.

4. **Excluir Linha**
   - Comando: `:x 5`
   - Saída esperada: A linha de número 5 será excluída do arquivo.

5. **Sair Sem Salvar**
   - Comando: `:q!`
   - Saída esperada: O editor será fechado sem salvar as modificações feitas.

6. **Exibir Intervalo de Linhas**
   - Comando: `:s 5 10`
   - Saída esperada: O conteúdo das linhas 5 a 10 será exibido com numeração. O usuário será perguntado se deseja continuar a exibição das próximas 10 linhas.

## Considerações Finais

Este editor foi desenvolvido como parte de um exercício de Mestrado em Computação Aplicada e segue os requisitos especificados no exercício-programa 1. O código implementa um editor simples baseado em lista circular duplamente ligada, permitindo realizar edições em arquivos de texto com comandos inspirados no Vi do Linux.

Caso haja dúvidas ou sugestões, entre em contato.
