class Veiculo:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
    
    def acelerar(self):
        return f'o {self.modelo} está acelerando.'
    
    def frear(self):
        return f'o {self.modelo} está freando.'
    
class Carro(Veiculo):
    def __init__(self, modelo, cor):
        super().__init__(modelo)
        self.cor = cor
    
    def abrir_porta(self):
        return f'a porta do {self.modelo} está aberta.'
    
class Moto(Veiculo):
    def __init__(self, modelo, cilindrada):
        super().__init__(modelo)
        self.cilindrada = cilindrada

    def empinar(self):
        return f'a {self.modelo} está empinando.'
    
if __name__ == '__main__':

 carro_generico = Veiculo('nissan')
 carro1 = Carro('Versa', 'branco')
 moto1 = Moto('CB500', '500 cilindradas')
 