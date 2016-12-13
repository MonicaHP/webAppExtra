import json

class clientes:
    dataCliente = []

    def readCliente(self):
        with open('data/clientes.json','r') as file:
            dataClientes = json.load(file)
            self.dataClientes = dataClientes['results']

    def getCliente(self):
        clientes = []
        for row in self.dataClientes:
            cliente = row['cliente']
            if cliente not in clientes:
                clientes.append(cliente)
        return clientes



