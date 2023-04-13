""""

STATEMENT

Professional boxers maintain a career record based on the outcomes of their fights. Fighters can win by knockout (KO), 
either by an actual knockout (falling unconscious, or if a fighter fails to stand up after a 10-second count after falling), 
or via technical knock out (TKO), when the referee stops the fight. The fight could also go to a decision at the end of the fight,
where a boxer could win by unanimous decision (UD) or split decision (SD), based on the scores from a panel of three judges. Lastly,
fights could end in a draw (D), based on the scorecards.

Given a list of boxing fights, boxer information, and their outcomes, your task is to determine the highest ranking boxer, both for the orthodox stance and the southpaw stance. The orthodox stance is usually used by right-handed boxers, and the southpaw stance is used by left-handed fighters.

The boxers will be ranked according to:
    number of wins (most wins first)
    number of losses (least losses first)
    number of draws (least number of draws first)
    number of wins via knockout (most number of knockouts)
    number of fights (increasing order)
    label of boxer (increasing order)


INPUT

Input starts with two integers Nand F on one line, separated by a space. 
N denotes the number of boxers to be considered. The boxers are labelled from 0 to N-1
F denotes the number of fights to consider.
Then F lines follow, which are of the following format:
    <boxer1> <O,S> <UD,SD,KO,TKO,D> <boxer2> <O,S>

<boxer1> and <boxer2> are the integer labels for the boxers in this fight. <O,S> indicates the stance of each boxer,
O for orthodox, and S for southpaw. <UD,SD,KO,TKO,D> shows the result of the fight. For this input format, if the result
is UD, SD, KO, or TKO, <boxer1> is interpreted to be the winner, and <boxer2>, the loser. KO and TKOs are both counted as
knockouts. If the result is D (draw), then both boxers get a draw in their record.

You may assume that the values for <boxer1> and <boxer2> are not equal. There will always be at least one orthodox boxer and 
one southpaw boxer in the fight records.


OUTPUT

Output the record of the top orthodox and top southpaw boxer. Refer to the sample output for exact formatting.


Sample input
4 2
2 O UD 0 S
3 S KO 1 O

Sample output
Orthodox: Boxer 2 (1W 0L 0D 0KO)
Southpaw: Boxer 3 (1W 0L 0D 1KO)


"""




def boxerSort(record, orth):
    top = [0, 0, 0, 0, 0, 0]        #[win, loss, draw, KO, fights, boxernumber]  
    topSouth = [0, 0, 0 ,0 ,0 ,0]
    for i in orth:
        if record[i][0] > top[0]:   #if more wins
            top = record[i]
            top.append(i)
        elif record[i][0] == top[0]:    #if same number of wins
            if record[i][1] < top[1]:   #if less number of losses
                top = record[i]
                top.append(i)
            elif record[i][1] == top[1]:    #if same number of losses
                if record[i][2] < top[2]:   #if less number of draws
                    top = record[i]
                    top.append(i)
                elif record[i][2] == top[2]: #if equal draws
                    if record[i][3] > top[3]:   #if more KO
                        top = record[i]
                        top.append(i)
                    elif record[i][3] == top[3]: #if equal KO
                        if record[i][4] > top[4]:   #if more fights
                            top = record[i]
                            top.append(i)
    return top

    
if __name__ == '__main__':   
    boxers, matches = input().rsplit()
    boxers, matches = int(boxers), int(matches)
    record = []
    orth = []
    south = []

    for i in range(boxers):
        record.append([0, 0, 0, 0, 0, 0])     #[wins, losses, draws, KO, fights, stance]
    for k in range(matches):
        boxer_a, stance_a, result, boxer_b, stance_b = input().rsplit()
        boxer_a, boxer_b = int(boxer_a), int(boxer_b)
        record[boxer_a][-1] = stance_a
        record[boxer_b][-1] = stance_b
        if result in ["UD", "SD", "KO", "TKO"]:
            record[boxer_a][0] += 1         #update win record of boxer_a
            record[boxer_a][-2] += 1        #update number of fights o boxer_a
            record[boxer_b][1] += 1         #update lose record of boxer_b
            record[boxer_b][-2] += 1        #update number of fights of boxer-b
            if result in ["TKO", "KO"]:
                record[boxer_a][-3] += 1    #update KO record of boxer_a
        else:                               #the result is draw, update draw and number of fights of both boxer
            record[boxer_a][2] += 1
            record[boxer_a][-2] += 1
            record[boxer_b][2] += 1
            record[boxer_b][-2] += 1
    for boxers in record:                   #getting the list of orthodox and southpaw boxers
        if boxers[-1] == "O":
            orth.append(record.index(boxers))
        else:
            south.append(record.index(boxers))
    
    TO = list(map(str, boxerSort(record, orth)))
    TS = list(map(str, boxerSort(record, south)))

    print("Orthodox: Boxer " + TO[-1] + " (" + TO[0] + "W " + TO[1] + "L " + TO[2] + "D " + TO[3] + "KO)")
    print("Southpaw: Boxer " + TS[-1] + " (" + TS[0] + "W " + TS[1] + "L " + TS[2] + "D " + TS[3] + "KO)")
     
    



    

