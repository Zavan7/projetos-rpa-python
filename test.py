import xlsxwriter

# Cria um novo arquivo e uma planilha
workbook = xlsxwriter.Workbook('exemplo.xlsx')
worksheet = workbook.add_worksheet()

# Escreve alguns dados na planilha
worksheet.write('A1', 'Hello')
worksheet.write('A2', 'World')

# Fecha e salva o arquivo
workbook.close()
