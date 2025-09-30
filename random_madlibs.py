from sample_madlibs import code, hp, hunger_games
import random

if __name__ == "__main__":
    m = random.choice([code, hp, hunger_games])
    m.madlib()
