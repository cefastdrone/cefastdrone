
class Base:
    def __init__(self, position, tipo):
        # posição deverá ser uma lista que terá 3 valores, [x, y, z]
        self.position = position

        # Tipo deve determinar se a base é terrestre ou se é maritima, que estará sujeita ao arrasto.
        self.tipo = tipo

        # Usada na fase 4 para determinar qual pacote está em qual base
        self.pacote = pacote


def takeoff():
    """
    Inicializa o drone e o mantem no lugar até receber o próximo comando
    """


def hover():
    """
    cancela o último comando e fica no lugar parado
    """


def land():
    """
    Pousa o drone
    """


def move(x, y, z):
    """
    O drone se move até a localidade marcada como sendo x, y, z
    :param x:
    :param y:
    :param z:
    :return:
    """


def turn_by(x, y, z):
    """
    Muda a direção do drone de acordo com os parâmetros
    :param x: roll
    :param y: pitch
    :param z: yaw
    """


def get_postion():
    """
    :return: posição do drone em relação ao ponto on ele começou como um dicionário
    """


def get_orientation():
    """
    :return: Orientação do drone em relação a posição em que ele começou como um dicionário
    'roll':  , 'pitch':  , 'yaw':
    """
