def resumo_vendas (vendas_smartphones, vendas_smartwatches):
    mais_vendido = 'Smartphone' if vendas_smartphones > vendas_smartwatches else 'Smartwatches'
    total_vendido = vendas_smartwatches + vendas_smartphones
    return mais_vendido, total_vendido

mais_vendido, total_vendido = resumo_vendas(80, 70)
print(f'O produto mais vendido foi: {mais_vendido}')
print(f'O total vendido foi: {total_vendido}\n')

vendas_semana = [(70, 65), (80, 82), (90, 88)]

for a, b in vendas_semana:
    print(f'Vendas de Smartphone da semana: {a} e de Smartwatches foi: {b}\n')


smartphone = 65
smartwatche = 70

smartphone, smartwatche = smartwatche, smartphone

print(f'Vendas da segunda-feira foram \nSmartphones: {smartphone} \nSmartwatches: {smartwatche}')