def verifica_letra_a(texto):
    # Converte a string para minúsculas para contar todas as ocorrências de 'a' e 'A'
    contador = texto.lower().count('a')
    
    # Verifica a presença e quantidade da letra 'a'
    if contador > 0:
        return f"A letra 'a' aparece {contador} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

# Entrada do usuário
texto = input("Informe uma string: ")
print(verifica_letra_a(texto))
