from Player import Player
from Deck import Deck
from Card import Card

class Game:
    def __init__(self):
        name1=input("プレイヤー1の名前を入力:")
        name2=input("プレイヤー2の名前を入力:")
        self.deck = Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)

    def print_wins(self,winner):
        """
        買ったやつを出力
        """
        print("\n")
        print("このラウンドは{}が勝ち".format(winner))

    def print_draw(self,p1name,p1card,p2name,p2card):
        """
        誰が何を引いたかを出力
        """
        print("\n")
        print("{}は{}を引き、{}は{}を引きました".format(p1name,p1card,p2name,p2card))

    def result(self,p1,p2):
        """
        play_gameメソッドで使う
        """
        if p1.win > p2.win:
            return p1.name
        if p1.win < p2.win:
            return p2.name
        else:
            return "引き分け"
    def play_game(self):
        """
        ここで前の3つのメソッドを使う
        """
        cards=self.deck.cards #これはリスト,単にwhileの条件で使う
        print("戦争を始めます")
        while len(cards) >= 2:
            response = input("qで終了、それ以外でplay")
            if response == "q":
                break
            p1_draw = self.deck.draw_card()
            p2_draw = self.deck.draw_card()
            self.print_draw(self.p1.name,p1_draw,self.p2.name,p2_draw)
            if p1_draw > p2_draw:
                self.p1.win += 1
                self.print_wins(self.p1.name)
            else:
                self.p2.win += 1
                self.print_wins(self.p2.name)

        r=self.result(self.p1,self.p2)

        print("ゲーム終了、{}の勝ち!".format(r))
