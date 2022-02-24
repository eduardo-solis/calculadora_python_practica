class Operaciones:
    
    def __init__(self, n1, n2, operacion):
        self.n1 = n1
        self.n2 = n2
        self.operacion = operacion
    
    def calcular(self):
        if self.operacion == 'Sumar':
            return self.sumar()
        elif self.operacion == 'Restar':
            return self.restar()
        elif self.operacion == 'Multiplicar':
            return self.multiplicar()
        else:
            return self.dividir()
        
    def sumar(self):
        return self.n1 + self.n2
    
    def restar(self):
        return self.n1 - self.n2
    
    def multiplicar(self):
        return self.n1 * self.n2
    
    def dividir(self):
        if self.n2 == 0:
            return 0
        else:
            return self.n1 / self.n2