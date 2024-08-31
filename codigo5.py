# String de exemplo (pode ser substituída por uma entrada do usuário)
string_original = "Teste"

# Inicializa uma string vazia para armazenar a string invertida
string_invertida = ""

# Percorre a string original de trás para frente
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

# Exibe a string invertida
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
