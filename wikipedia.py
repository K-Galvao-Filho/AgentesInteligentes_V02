import requests

def pesquisar_wikipedia(consultas, num_resultados=3):
    """
    Pesquisa artigos na Wikipedia em português para uma lista de tópicos, garantindo pelo menos um item por tópico.
    Args:
        consultas (list or str): Um tópico de pesquisa ou lista de tópicos.
        num_resultados (int): Número máximo de artigos a retornar por tópico.
    Returns:
        list: Lista de dicionários com título, URL e trecho do artigo para cada tópico.
    """
    print(f"Pesquisando na Wikipedia: {consultas}")
    
    # Se consultas for uma string, converte para lista com um item
    if isinstance(consultas, str):
        consultas = [consultas]
    
    # Validação
    if not isinstance(consultas, list):
        print("Erro: consultas deve ser uma string ou lista de strings.")
        return []
    if not all(isinstance(c, str) for c in consultas):
        print("Erro: todos os itens de consultas devem ser strings.")
        return []
    
    try:
        url = "https://pt.wikipedia.org/w/api.php"  # URL correta da API
        todos_artigos = []
        
        for consulta in consultas:
            print(f"Buscando: {consulta}")
            params = {
                "action": "query",
                "format": "json",
                "list": "search",
                "srsearch": consulta,
                "srlimit": num_resultados,
                "utf8": 1
            }
            response = requests.get(url, params=params)
            response.raise_for_status()  # Levanta exceção para erros HTTP
            data = response.json()
            results = data.get("query", {}).get("search", [])
            
            artigos = []
            for item in results:
                title = item["title"]
                snippet = item["snippet"].replace("<span class=\"searchmatch\">", "").replace("</span>", "")
                # URL do artigo, não da API
                article_url = f"https://pt.wikipedia.org/wiki/{title.replace(' ', '_')}"
                artigos.append({
                    "Tópico": consulta,
                    "Título": title,
                    "URL": article_url,
                    "Trecho": snippet
                })
            
            # Garantir pelo menos um item por tópico
            if not artigos:
                artigos.append({
                    "Tópico": consulta,
                    "Título": "Nenhum artigo encontrado",
                    "URL": "",
                    "Trecho": "Não foram encontrados artigos relevantes para este tópico."
                })
            
            # Adicionar pelo menos o primeiro item (ou mais, até num_resultados)
            todos_artigos.extend(artigos[:max(1, num_resultados)])
        
        print(f"Artigos encontrados: {todos_artigos}")
        return todos_artigos
    
    except Exception as e:
        print(f"Erro ao buscar na Wikipedia: {e}")
        return []