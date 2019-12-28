from RandomWalk import RandomWalk
import pandas as pd
import numpy as np
import random

randomwalk=RandomWalk(10000,20)
# rn=randomwalk.choise_random_numbers_q1()

# randomwalk.draw_plot(randomwalk.choise_list)

# randomwalk.draw_walk()

rn=randomwalk.choise_random_numbers_q2()

randomwalk.draw_plot(randomwalk.choise_list)

randomwalk.draw_walk()