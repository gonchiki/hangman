from class_Deck_War import Deck
from class_Player_War import Player


class Game:

    def __init__(self):
        name1 = input("プレイヤー１の名前")
        name2 = input("プレイヤー２の名前")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        w = "このラウンドは{}が勝ちました".format(winner)
        print(w)
        print("現在 "+ self.p1 + " は" + p1.wins + "勝")

    def draw(self,p1n,p1c,p2n,p2c):
        d = "{}は{}、{}は{}を引きました".format(p1n,p1c,p2n,p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます")
        while len(cards) >= 2:
            response = input("qで終了、それ以外のキーでplay:")

            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1,self.p2)
        print("ゲーム終了、{}の勝ちです！".format(win))

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け！"
        
                
