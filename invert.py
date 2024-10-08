def inverter_string(string):
    # Criar uma nova string vazia que vai armazenar os caracteres invertidos
    string_invertida = ''
    
    # Percorrer a string original de trás para frente
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    return string_invertida

# Entrada da string (pode ser alterada conforme desejado)
string_original = input("Digite a string que deseja inverter: ")

# Chamar a função e exibir a string invertida
print("String invertida:", inverter_string(string_original))
