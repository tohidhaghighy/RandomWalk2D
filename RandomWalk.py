import random 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class RandomWalk:
    def __init__(self,total_move,per_move):
        self.total_move=total_move
        self.per_move=per_move
        self.walk_array=[]
        self.choise_list=[]
        self.choise_list_squres=[]
        self.choise_list_squres_mean=[]

    def choise_random_numbers_q1(self):
        numbers=[1,-1]
        for move in range(self.total_move):
            sumation=0
            for i in range(self.per_move):
                rn=random.choice(numbers)
                sumation+=rn
            self.choise_list.append(sumation)
            self.choise_list_squres.append(sumation ** 2)
            self.choise_list_squres_mean.append(np.mean(np.array(self.choise_list_squres)))
        
        
        return self.choise_list

    def choise_random_numbers_q2(self):
        numbers=[1,-1]
        for move in range(self.total_move):
            sumation=0
            for i in range(self.per_move):
                rn=random.choice(numbers)
                sumation+=rn
                if sumation ==-1 :
                    sumation=0
            self.choise_list.append(sumation)
            self.choise_list_squres.append(sumation ** 2)
            self.choise_list_squres_mean.append(np.mean(np.array(self.choise_list_squres)))
        
        return self.choise_list

    def draw_plot(self,walk_number):
        plt.plot(walk_number) 
        plt.show()

    def draw_walk(self):
         # diffusion coefficient is equal to the last transition square mean we computed
        diffusion_coefficient = self.choise_list_squres_mean[-1]
        print('Diffusion Coefficient: {0}'.format(diffusion_coefficient))

        # draw transition square means
        tsm_data = pd.DataFrame(data={'move': range(self.total_move), 'tsm': self.choise_list_squres_mean,
                                      'diff_co': [diffusion_coefficient] * self.total_move})
        sns.lineplot(x='move', y='tsm', data=tsm_data)
        sns.lineplot(x='move', y='diff_co', data=tsm_data)
        plt.show()

        # draw distribution
        sns.distplot(self.choise_list, rug=True)
        plt.show()
    


