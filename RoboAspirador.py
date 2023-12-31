import random

class AgenteAspira:
    def __init__(self, energia_inicial):
        self.localizacao = 'A'
        self.energia = energia_inicial
        self.bolsa_sujeira = 0

    def locomocao(self, ambiente):
        if self.localizacao in ambiente.localizacoes:
            localizacoes_disponiveis = [loc for loc in ambiente.localizacoes if loc != self.localizacao and not ambiente.tem_sujeira(loc)]
            if localizacoes_disponiveis:
                nova_localizacao = random.choice(localizacoes_disponiveis)
                self.localizacao = nova_localizacao
                self.energia -= 1

    def definir_atividade(self, ambiente):
        if self.bolsa_sujeira == 10 or self.energia == 0:
            return 'VoltarParaCasa'
        elif ambiente.tem_sujeira(self.localizacao):
            return 'Aspirar'
        else:
            return 'Mover'

    def volta(self):
        self.energia -= 1
        self.localizacao = 'A'
        self.bolsa_sujeira = 0

    def limpar(self, ambiente):
        self.energia -= 1
        ambiente.remover_sujeira(self.localizacao)
        self.bolsa_sujeira += 2


class MeioAmbiente:
    def __init__(self):
        self.localizacoes = [
            'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P'
        ]
        self.sujeira = {random.choice(self.localizacoes) for _ in range(10)}

    def tem_sujeira(self, localizacao):
        return localizacao in self.sujeira

    def remover_sujeira(self, localizacao):
        if localizacao in self.sujeira:
            self.sujeira.remove(localizacao)

if __name__ == "__main__":
    agente = AgenteAspira(100)
    ambiente = MeioAmbiente()

    while agente.energia > 0:
        acao = agente.definir_atividade(ambiente)

        if acao == 'VoltarParaCasa':
            agente.volta()
        elif acao == 'Aspirar':
            agente.limpar(ambiente)
        elif acao == 'Mover':
            agente.locomocao(ambiente)

        print(f"Localizacao: {agente.localizacao}, Energia: {agente.energia}, Bolsa de Sujeira: {agente.bolsa_sujeira}")

        if all(not ambiente.tem_sujeira(loc) for loc in ambiente.localizacoes):
            print("Todas as localizações estão limpas. Encerrando.")
            break  # Corrigido para sair do loop quando todas as localizações estão limpas