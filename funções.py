class Base:
    def __init__(self, position, tipo):
        # posição deverá ser uma lista que terá 3 valores, [x, y, z]
        self.position = position

        # Tipo deve determinar se a base é terrestre ou se é maritima, que estará sujeita ao arrasto.
        self.tipo = tipo

        # Lista com as bases
    def marcar_pacote(self, pacote):
        self.pacote = pacote
        """
        Quado tirarmos o pacote, o pacote == None. 
        Quando colocarmos o pacote na base, marcamo com o pacote. 
        Quando apenas lermos, marcamos com o pacote que foi lido
        """

    def get_base_position(self):
        if self.tipo == 'maritima':
            return self.position
        elif self.tipo == 'terrestre':
            posição_fixa = (self.position[0], self.position[1], self.position[2])
            return posição_fixa


class Drone:
    def takeoff(self):
        """
        Inicializa o drone e o mantem no lugar até receber o próximo comando
        """

    def hover(self):
        """
        cancela o último comando e fica no lugar parado
        """

    def land(self):
        """
        Pousa o drone
        """
        # Comunicar com a câmera caso não esteja carregando nenhum pacote ou apenas com o GPS caso esteja

    def move(self, x, y, z):
        """
        O drone se move até a localidade marcada como sendo x, y, z
        :param x:
        :param y:
        :param z:
        :return:
        """
        # Precisa receber a informação de onde o drone precisa chegar, coordenadas, e de onde ele está.
        # A partir dessas informações ele deve conseguir se mover em linha reta entre um ponto e outro.
        # A função só pode acabar quando ele tiver chegado no local

    def turn_by(self, x, y, z):
        """
        Muda a direção do drone de acordo com os parâmetros
        :param x: roll
        :param y: pitch
        :param z: yaw
        """

    def get_postion(self):
        """
        :return: posição do drone em relação ao ponto on ele começou como um dicionário
        """
        # Comunicar com o gps para saber aonde está

    def get_orientation(self):
        """
        :return: Orientação do drone em relação a posição em que ele começou como um dicionário
        'roll':  , 'pitch':  , 'yaw':
        """

    def check_base(self, dict_packages):
        """
        Missão 4
        O drone deve ler o qr code que estiver na base e então armazenar os valores no dict_packages
        Cada pacote 1, 2, 3, ... está relacionado com uma base pré-definida
        :return: True if there is a package there or False if not
        """

    def take_package(self, drone):
        """
        Missão 4
        O drone deve abaixar e pegar o pacote da base com a garra e voltar a posição original
        """
        # Sobe de novo
        drone.move(
            drone.get_postion()[0],
            drone.get_postion()[1] + 1,
            drone.get_postion()[2]
        )

    def drop_package(self):
        """
        Missão 4
        O drone vai descer até a plataforma e soltar o pacote e então voltar a posição original
        Deve também trocar o status do pacote para entregue
        """

