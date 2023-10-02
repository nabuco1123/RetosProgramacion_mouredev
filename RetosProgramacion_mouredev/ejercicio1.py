def obtener_parametros_url(url:str) -> list:
    query = url.split("?")
    if len(query)<=1:
        return []
    parametros = query[1].split("&")
    valor_parametros=[]
    for parametro in parametros:
        valor_parametros.append(parametro.split("=")[1])
    return valor_parametros

if __name__ == "__main__":
    url = "https://retosdeprogramacion.com?year=2023&challenge=0&test=true"
    parametros = obtener_parametros_url(url)
    print(*parametros)
