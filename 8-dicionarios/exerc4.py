estacionamento = {
    "A1": {
        "marca": "Toyota",
        "modelo": "Corolla",
        "dono": "Sr. Silva"
    },
    "B2": {
        "marca": "Honda",
        "modelo": "Civic",
        "dono": "Dona Maria"
    },
    "C3": {
        "marca": "Ford",
        "modelo": "Mustang",
        "dono": "Sr. Jorge"
    }
}


carro_B2 = estacionamento["B2"]["modelo"]
print(f'O carro estacionado na vaga B2 é o: {carro_B2}')

estacionamento["A1"]['dono'] = 'Sra Lucia'
print (f'O dono do carro, na vaga A1 é a: {estacionamento["A1"]['dono']}')

estacionamento['D4'] = {
        "marca": "Chevrolet",
        "modelo": "Onix",
        "dono": "Sr Roberto" 
}

