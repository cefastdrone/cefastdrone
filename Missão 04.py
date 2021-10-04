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
        base.get_base_position()[0],  # X
        base.get_base_position()[1] + 1,  # Y
        base.get_base_position()[2]  # Z
    )

    if drone.check_base(dict_packages):
        continue
    empty_base = base

# Implementar checagem para podermos ver se o pacote foi entregue ou se caiu no caminho.
for c in range(len(bases)):
    tot1 = 0
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

# Devemos agora implementar a devolução dos pacotes as bases.
#   Esse processo vai depender do fator tempo que não se pode ser medido diretamente
#       Dado esse motivo, precisamos de uma saída diferente para determinar quantos pacotes serão entregues

numero_de_pacotes = 2  # Qauntos pacotes devem ser pegos
visited_bases = []
for c in range(0, numero_de_pacotes):
    # Qual base está mais próxima?
    nearest_base = 0
    tot2 = 'É a primeira'
    for base in bases:
        if not (base in visited_bases):
            if tot2 == 'É a primeira':
                nearest_base = base
                tot2 = 'Não é mais a primeira'
            else:
                dist_currently_base = base.get_base_position()[0] + \
                                      base.get_base_position()[1] + \
                                      base.get_base_position()[2]

                dist_nearest_base = nearest_base.get_base_position()[0] + \
                                    nearest_base.get_base_position()[1] + \
                                    nearest_base.get_base_position()[2]
                if dist_currently_base <= dist_nearest_base:
                    nearest_base = base

    # vai até a base
    drone.move(
        nearest_base.get_base_position()[0],
        nearest_base.get_base_position()[1] + 1,
        nearest_base.get_base_position()[2]
    )

    # Pega o pacote
    drone.take_package()
    visited_bases.append(nearest_base)

    # Leva até a base costeira
    drone.move(0, 1, 0)
    drone.drop_package('costeira')


# Devemos fazer com que ele volte para a base costeira e pouse
# Terá outros pacotes na base costeira que não poderam estar atrapalhando
# o drone tanto a recolnhecer a base quanto a pousar
drone.move(0, 1, 0)
drone.land()
