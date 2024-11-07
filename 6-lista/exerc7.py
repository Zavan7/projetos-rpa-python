frutas = ["maçã", "banana", "manga", "uva", "abacaxi", "laranja"]

frutas_longas = [fruta for fruta in frutas if len(fruta) > 5]

print(f"Frutas com mais de 5 caracteres: {frutas_longas}")