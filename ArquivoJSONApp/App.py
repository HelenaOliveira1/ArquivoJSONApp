'''
    Função principal do código.
'''

import json #importa JSON

def incluirContato(arquivoContatos): #Cria função para incluir contatos ao objeto JSON

    nome = str(input("Digite nome do contato: "))
    nascimento = str(input("Digite nascimento do contato: "))
    contato = {"nome": nome, "nascimento": nascimento}
    open("contatos.txt", "w", encoding="utf8")
    arquivoContatos.append(contato)


def main(Args = []): #Função menu - Sintetizatodo o código

    arquivoContatos = open("contatos.txt", encoding="utf8") #Abre Arquivo de Contatos

    jsonObj = json.loads(arquivoContatos.read()) #tranformando arquivos em JSON

    print(jsonObj)

    aux = 0
    for contato in jsonObj: #inicializa um loop para iterar os contatos

        print("Contato", aux+1)
        print("Nome:", jsonObj[aux]["nome"])
        print("Nascimento:", jsonObj[aux]["nascimento"])

        aux += 1

    incluirContato(arquivoContatos)

if __name__ == "__main__":
    main()
