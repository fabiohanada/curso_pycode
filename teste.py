class Celular:
    marca = 'Nokia'
    modelo = 'Tijolao'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'
    
    def fazer_ligacoes(self):
        print('Fazendo ligacao...')
    
    def jogar_cobrinha(self):
        print('Jogando cobrinha...')
        
    def despertador(self):
        print('Despertando...')
        
celular = Celular()


print(celular.marca)
print(celular.modelo)
print(celular.cor)

celular.fazer_ligacoes()