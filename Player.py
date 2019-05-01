class Player:
    """
    プレイヤー(インスタンス)にインスタンス変数として勝ち回数、持つカード、名前を与える
    """
    def __init__(self,name):
        self.win=0
        self.card=None
        self.name=name
