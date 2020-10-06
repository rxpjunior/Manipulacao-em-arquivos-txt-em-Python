#Arquivos a serem abertos para pesquisa
antiInflamatorio = open("antInflamatorio.txt","r")
substituiOvoLeite = open("substituiOvoLeite.txt","r")
inflamatorio = open("inflamatorio.txt","r")

#Arquivo aberto para escrita do cardapio
cardapio = open("cardapio.txt","w")

#Carregando os itens dos arquivos txt para listas (itens separados por virgula)
for linha in antiInflamatorio:
    vetAntiInflamatorio = linha.split(',')
for linha in substituiOvoLeite:
    vetSubstituiOvoLeite = linha.split(',')
for linha in inflamatorio:
    vetInflamatorio = linha.split(',')

#Fechando os arquivos de texto de pesquisa
antiInflamatorio.close()
substituiOvoLeite.close()
inflamatorio.close()

#Carregando no arquivo cardapio apenas itens que nao existam na lista de inflamatorios
cardapio.write('Alimentos antinflamatorios\n')
for item in vetAntiInflamatorio:
    if item not in vetInflamatorio:
        cardapio.write(item+'\n')

cardapio.write('\n\nAlimentos que substituem leite e ovo\n')        
for item in vetSubstituiOvoLeite:
    if item not in vetInflamatorio:
        cardapio.write(item+'\n')

#Fechando o arquivo do cardapio    
cardapio.close()

#Arquivo aberto para leitura do cardapio
cardapio = open("cardapio.txt","r")

#Exibindo o resultado
for linha in cardapio:
    print(linha)

#Fechando o arquivo do cardapio    
cardapio.close()

