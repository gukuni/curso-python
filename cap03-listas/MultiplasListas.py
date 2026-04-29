equipamento = []
valor = []
numero_serial = []
departamento = []
resposta = "S"
while resposta == "S":
    equipamento.append(input("Equipamento: "))
    valor.append(float(input("Valor: ")))
    numero_serial.append(int(input("DIgite o número serial: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite S se quiser continuar: ").upper()
for indice in range(0,len(equipamento)):
    print(f"Equipamento{indice+1}")
    print(f"Nome: {equipamento[indice]}")
    print(f"Valor: {valor[indice]}")
    print(f"Número serial: {numero_serial[indice]}")
    print(f"Departamento {departamento[indice]}")
