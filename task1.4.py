import random
class ChessPlayer:
    def __init__(self, name, age, elo, tenacity, is_boring):
        self.name=name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.is_boring = is_boring
        self.tournament_score = 0
    def simulateMatch(self,opp):
        elo_difference=abs(self.elo-opp.elo)
        if elo_difference>100:
            if self.elo>opp.elo:
                self.tournament_score+=1
            else:
                opp.tournament_score+=1
        elif elo_difference>50 and elo_difference<=100:
            r=random.randint(1,10)
            if self.elo<opp.elo:
                if (r*self.tenacity) > opp.elo:
                    self.tournament_score+=1
                else:
                    opp.tournament_score+=1
            elif opp.elo<self.elo:
                if (r*opp.tenacity) > self.elo:
                    opp.tournament_score+=1
                else:
                    self.tournament_score+=1
        elif elo_difference<=50:
            if self.tenacity > opp.tenacity:
                self.tournament_score += 1
            else:
                opp.tournament_score += 1
        if self.is_boring==True or opp.is_boring==True:
            if elo_difference<=100:
                self.tournament_score+=0.5
                opp.tournament_score+=0.5
            
arr=[
    ChessPlayer("Courage the Cowardly Dog",25, 1000.39, 1000 ,False),
    ChessPlayer("Princess Peach", 23, 945.65, 50, True),
    ChessPlayer("Walter White", 50, 1650.73, 750, False),
    ChessPlayer("Rory Gilmore",16 ,1700.87 ,500 ,False),
    ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True),
    ChessPlayer("Beth Harmon" ,20 ,2500.34 ,150 ,False)
    ]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        arr[i].simulateMatch(arr[j])
        arr[j].simulateMatch(arr[i])
arr.sort(key=lambda player:player.tournament_score)
print(f"Name{' ':<36}Tournament_score")
for i in range(len(arr)):
    print(f"{arr[i].name:<40}{arr[i].tournament_score}")