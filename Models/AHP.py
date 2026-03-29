import numpy as np

def norm_avg(matrix):
    """
    Calculate the weights from the pairwise comparison matrix.
        input: matrix of shape (n, n) where n is the number of criteria
        output: vector of shape (n,) where n is the number of criteria
    """
    column_sums = np.sum(matrix, axis=0)
    normalized_matrix = matrix / column_sums
    avg = np.mean(normalized_matrix, axis=1)
    return avg

class AHP_normalization:
    def __init__(self, matrix1, matrix2):
        # define the pairwise comparison matrix for criteria and alternatives
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def weight_vector(self):
        """Calculate the weights from the pairwise comparison matrix.
        input: matrix of shape (n, n) where n is the number of criteria
        output: vector of shape (n,) where n is the number of criteria
        """
        return norm_avg(self.matrix1)
    
    def score_matrix(self):
        """Calculate the scores from the multiple pairwise comparison matrixs.
        input: matrix of shape (n, n, m) where n is the number of criteria and m is the number of alternatives
        output: matrix of shape (n, m) where n is the number of criteria and m is the number of alternatives
        """
        m = len(self.matrix2)
        n = np.size(self.matrix2[0], 0)
        mtx = np.zeros((n, m))
        for i in range(m):
            mtx[i, :] = norm_avg(self.matrix2[i])
        return mtx
    
    def CI(self):
        """Calculate the consistency index of the pairwise comparison matrix.
        input: matrix of shape (n, n) where n is the number of criteria
        output: consistency index
        """
        n = self.matrix1.shape[0]
        Aw = np.dot(self.matrix1, self.weight_vector())
        lambda_max = np.sum(Aw / self.weight_vector()) / n # the principal eigenvalue of the pairwise comparison matrix
        CI = (lambda_max - n) / (n - 1)
        return CI

    def global_score(self):
        """Calculate the weighted sum of scores given the weights.
        input: weights of shape (n,) where n is the number of criteria
            scores of shape (n, m) where n is the number of criteria and m is the number of alternatives
        output: vector of shape (m,) where m is the number of alternatives
        """
        return np.dot(self.weight_vector(), self.score_matrix())
   