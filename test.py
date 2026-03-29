import numpy as np
from Models.AHP import AHP_normalization

preferences = np.array([[1, 1/5, 1/3, 1/2],
                        [5, 1, 2, 4],
                        [3, 1/2, 1, 3],
                        [2, 1/4, 1/3, 1]])

evaluation1 = np.array([[1, 1/2, 1/3, 5],
                       [2, 1, 1/2, 7],
                       [3, 2, 1, 9],
                       [1/5, 1/7, 1/9, 1]])
evaluation2 = np.array([[1, 1/2, 3, 5],
                       [2, 1, 1/2, 7],
                       [1/3, 2, 1, 9],
                       [1/5, 1/7, 1/9, 1]])
evaluation3 = np.array([[1, 1/2, 1/3, 1/5],
                       [2, 1, 1/2, 7],
                       [3, 2, 1, 9],
                       [5, 1/7, 1/9, 1]])
evaluation4 = np.array([[1, 1/2, 1/3, 5],
                       [2, 1, 1/2, 7],
                       [3, 2, 1, 1/9],
                       [1/5, 1/7, 9, 1]])

scores = np.array([[0.174, 0.293, 0.489, 0.044],
                  [0.050, 0.444, 0.312, 0.194],
                  [0.210, 0.038, 0.354, 0.398],
                  [0.510, 0.012, 0.290, 0.188]])

ahp = AHP_normalization(preferences, [evaluation1, evaluation2, evaluation3, evaluation4])
weigts = ahp.weight_vector()
scores = ahp.score_matrix()
global_score = ahp.global_score()
CI = ahp.CI()
# print("Weights:", weigts)
# print("Scores:", scores)
print("CI:", CI)