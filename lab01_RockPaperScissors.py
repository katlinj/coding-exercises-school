"""
Leonard and Sheldon are playing a modified version of Rock Paper Scissors that includes two additional
choices namely Lizard and Spock.

Rules:
Pick          | Can defeat
ROCK(R)       | SCISSORS, LIZARD
SCISSORS(s)   | PAPER, LIZARD
PAPER(P)      | ROCK, SPOCK
SPOCK(S)      | SCISSORS, ROCK
LIZARD(L)     | SPOCK, PAPER

This program outputs the score of Sheldon and Leonard after a given number of matches.
 
Input Format
First line of input: integer M that indicates the number of rounds/matches
M lines follow, each containing two characters (R, P, s, L, or S) separated by a space. First
character is Leonard's pick, second character is Sheldon's.


"""




def isWinner(player, opponent):
    #returns 1 if players wins, otherwise, returns 0
    if opponent in winAgainst.get(player):
        return 1
    else:
        return 0



winAgainst = {"s":["P", "L"], "P":["R","S"], "R":["s", "L"], "S":["s", "R"], "L":["S", "P"]}
#keys win against the elements in the list
rounds = int(input())
leonardScore = 0
sheldonScore = 0
draw = 0
for k in range(rounds):
    leonard, sheldon = input().rstrip().rsplit()
    if isWinner(leonard, sheldon) > isWinner(sheldon, leonard):
        leonardScore += 1
    elif isWinner(leonard, sheldon) < isWinner(sheldon, leonard):
        sheldonScore += 1
    else:
        draw += 1
print("Leonard:" + str(leonardScore) + " Sheldon:" + str(sheldonScore) + " Draw:" + str(draw))


