# MODO | FUNÇÃO

# r - somente leitura
# w - escrita (caso ja exista o arquivo, ele cria um novo do zero)
# a - leitura e escita (adiciona conteudo no arquivo)
# r+ - leitura e escrite
# w+ - escrita( semelhante ao modo w)
# a+ - leitura e escrita (abre o arquivo para atualização)


# LER ARQUIVOS
# arquivo = open ("Meuarquivo.txt")

# texto_completo = arquivo.read()

# print(texto_completo)


#CRIAR ARQUIVOS
w = open("arquivo2.txt", "w") 

w.write("Esse eh o aaaaaaaaaaaaa \naaa \n")

w.close()