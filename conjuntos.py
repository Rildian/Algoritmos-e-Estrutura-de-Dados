frutas = set(["abacate", "tomate", "banana"])
vegetais = set(["beterrada", "tomate", "cenoura"])

print(f"Resultado da união: {frutas | vegetais}") 
print(f"Resultado da intersecção: {frutas & vegetais}") 
print(f"Resultado da diferença: {frutas - vegetais}") 
print(f"Resultado da diferença: {vegetais - frutas}")
