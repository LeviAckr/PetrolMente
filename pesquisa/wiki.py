import requests
import webbrowser
from googlesearch import search
import wikipedia

def pesquisar_wikipedia(termo):
    try:
        # Define o idioma como português
        wikipedia.set_lang("pt")
        
        # Realiza a pesquisa na Wikipedia
        resultados = wikipedia.search(termo)
        if len(resultados) > 0:
            # Obtém o primeiro resultado
            titulo = resultados[0]
            # Obtém o resumo do artigo
            resumo = wikipedia.summary(titulo)
            # Exibe o resumo no terminal
            print(f"Resultado da pesquisa: {titulo}\n")
            print(resumo)
        else:
            print("Nenhum resultado encontrado.")
    except wikipedia.exceptions.DisambiguationError as e:
        print("A pesquisa retornou múltiplos resultados. Seja mais específico.")
    except wikipedia.exceptions.PageError as e:
        print("Nenhum resultado encontrado.")

# Solicita ao usuário o termo de pesquisa
termo_pesquisa = input("Faça sua pesquisa:: ")

# Chama a função de pesquisa
pesquisar_wikipedia(termo_pesquisa)