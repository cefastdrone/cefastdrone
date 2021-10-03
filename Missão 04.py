from funções import *
# Nesse dicionário devem ser adicionadas as informações sobre cada pacote 1, 2, 3, 4 e 5
# O pacote contem as informções, qual base ele está e a situação:
#   entregue, não entregue, ou fora de jogo, caso tenha sido derrubado em algum processo
dict_packages = {
    'pacote_1': {'base': [], 'destinatário': [], 'entregue': 'Não'},
    'pacote_2': {'base': [], 'destinatário': [], 'entregue': 'Não'},
    'pacote_3': {'base': [], 'destinatário': [], 'entregue': 'Não'},
    'pacote_4': {'base': [], 'destinatário': [], 'entregue': 'Não'},
    'pacote_5': {'base': [], 'destinatário': [], 'entregue': 'Não'}
                 }

drone = Drone()

# Lista com todas as bases que deve criada na missão 1
bases = []

drone.takeoff()

for base in bases:
    drone.move(
            base.get_base_position()[0],      # X
            base.get_base_position()[1] + 1,  # Y
            base.get_base_position()[2]       # Z
    )
    if drone.check_base(dict_packages):
        continue
    empty_base = base


# Implementar checagem para podermos ver se o pacote foi entregue ou se caiu no caminho.
for c in range(len(bases)):
    for values in dict_packages:
        if values['destinatário'][0] == empty_base:

            # Vai até a base com o pacote
            drone.move(
                values['destinatário'][0].get_base_position()[0],
                values['destinatário'][0].get_base_position()[1],
                values['destinatário'][0].get_base_position()[3]
            )

            # Pega o pacote
            drone.take_package()

            # Vai até a base vazia
            drone.move(
                empty_base.get_position()[0],
                empty_base.get_position()[1] + 1,
                empty_base.get_position()[2]
            )

            # Deixa o pacote
            drone.drop_package()

            empty_base = values['base'][0]
        pass

    # Devemos agora implementar a devolução dos pacotes as bases.
    #   Esse processo vai depender do fator tempo que não se pode ser medido diretamente
    #       Dado esse motivo, precisamos de uma saída diferente para determinar quantos pacotes serão entregues




