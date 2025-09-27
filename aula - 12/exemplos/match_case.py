
def operacao(acao): 
  match acao:
    case "soma": 
      return "soma..."
    case "subtracao": 
      return "subtracao..."
    case "multiplicacao": 
      return "multiplicacao..."
    case "divisao": 
      return "divisao..."
    case _:
      return "acao desconhecida"
  

print(operacao("soma"))
