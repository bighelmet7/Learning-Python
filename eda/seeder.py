#!/usr/bin/env python
import subprocess
import random
import json
import time

def main():
    player_1 = "bighelmet9"
    player_2 = "__bighelmet7"
    player_3 = "Crimson"
    player_4 = "Dummy"
    players = [player_1, player_2, player_3, player_4]
    SCORES = {
        player_1: {"wins": {"total": 0, "seed_win": []}, "scores_per_round": []},
        player_2: {"wins": {"total": 0, "seed_win": []}, "scores_per_round": []},
        player_3: {"wins": {"total": 0, "seed_win": []}, "scores_per_round": []},
        player_4: {"wins": {"total": 0, "seed_win": []}, "scores_per_round": []},
    }
    for i in range(1, 100):
        print("Test numero: ", i)
        print("----------------------")
        seed = str(random.randrange(1, 1000))   #random seed
        random.shuffle(players)                 #random list of players
        command = "./Game %s %s %s %s -s %s -i default.cnf -o default.out 2>&1 | grep \"^info: player\\w*\"" % (players[0], players[1], players[2], players[3], seed)
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            out = str(output)
            lines = out.split('\\n')
            for line in lines:
                s = line.split() #getting the score
                if not "got top score" in line and not "loaded" in s:
                    if not "loaded" in s and len(s) > 2:
                        SCORES[s[2]]["scores_per_round"].append(int(s[-1]))
                else:
                    if not "loaded" in s and len(s) > 2:
                        SCORES[s[2]]["wins"]["total"] += 1 #counts the numbers of winns
                        SCORES[s[2]]["wins"]["seed_win"].append({"seed": seed, "round": i})
        except Exception as e:
            with open("error.txt", "a") as file:
                file.write("Error: " + str(e) + "\n")
            raise
        print("Realizado correctamente")
        print("----------------------")

    with open("datos_random.txt", 'w') as file:
        file.write(json.dumps(SCORES))
    print(SCORES)

if __name__ == '__main__':
    main()
