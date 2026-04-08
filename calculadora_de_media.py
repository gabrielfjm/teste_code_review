# Verifica se pelo menos um número foi digitado antes de calcular a média
if qtde > 0:
    # 4. Calcula a média
    media = soma / (qtde-1)

    # 5. Exibe o resultado final
    print(f"A média dos números digitados é: {media:.2f}")
else:
    print("Nenhum número foi digitado para calcular a média.")

print("Fim do algoritmo.")