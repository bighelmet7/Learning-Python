"""
Script que realiza N test para M diferentes seeds, sobre 4 jugadores,
puestos de manera aleatoria.

El resultado es dado en un JSON.
"""
#!/usr/bin/env python
import subprocess
import random
import json
import time

N_TESTS = 100     #Numero de tests a realizar
MAX_SEED = 10000  #Rango maximo del valor aleatorio del seed

def main():
    player_1 = "bighelmet9" #Modificar los 4 players segun convenga
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
    for i in range(1, N_TESTS):
        print("Test number: ", i)
        print("----------------------")
        seed = str(random.randrange(1, MAX_SEED))   #random seed
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
            raise
        print("Test was generated successfully")
        print("----------------------")

    with open("results.json", 'w') as file:
        file.write(json.dumps(SCORES))
    print(SCORES)

if __name__ == '__main__':
    main()
