import numpy as np
from Models.AHP import AHP_normalization

C = np.array([[1, 3, 5],
              [1/3, 1, 3],
              [1/5, 1/3, 1]])

B1 = np.array([[1, 3, 7],
              [1/3, 1, 5],
              [1/7, 1/5, 1]])

B2 = np.array([[1, 1/5, 1],
              [5, 1, 5],
              [1, 1/5, 1]])

B3 = np.array([[1, 5, 9],
              [1/5, 1, 3],
              [1/9, 1/3, 1]])
B = [B1, B2, B3]

ahp = AHP_normalization(C, B)

weigts = ahp.weight_vector()
scores = ahp.score_matrix()
global_score = ahp.global_score()
CI = ahp.CI()

print("Weights:", weigts)
print("Scores:", scores)
print("Global Score:", global_score)
print("CI:", CI)