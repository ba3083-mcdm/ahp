import numpy as np

class TOPSIS:
    def __init__(self, decision_matrix, weight_vector, flag=None):
        self.decision_matrix = np.array(decision_matrix, dtype=float)
        self.weight_vector = np.array(weight_vector, dtype=float)

        assert self.decision_matrix.shape[1] == self.weight_vector.shape[0]

        if flag is None:
            flag = [True] * self.decision_matrix.shape[1]
        self.flag = flag

        self.standardized_matrix = self.func_StandardizeDecisionMatrix(self.decision_matrix)
        self.weighted_standardized_matrix = self.func_WeightedStandardizedDecisionMatrix(
            self.standardized_matrix,
            self.weight_vector
        )
        self.positive_ideal_solution = self.func_PositiveIdealSolution(
            self.weighted_standardized_matrix,
            self.flag
        )
        self.negative_ideal_solution = self.func_NegativeIdealSolution(
            self.weighted_standardized_matrix,
            self.flag
        )
        self.relative_closeness = self.func_IdealSolutionRelativeCloseness(
            positive_matrix = self.positive_ideal_solution,
            negative_matrix = self.negative_ideal_solution
        )

    @classmethod
    def func_StandardizeDecisionMatrix(cls, input_matrix):
        output_matrix = np.zeros(input_matrix.shape)
        for i in range(input_matrix.shape[1]):
            denom = np.sqrt(np.sum(input_matrix[:, i] ** 2))
            output_matrix[:, i] = input_matrix[:, i] / denom
        return output_matrix

    @classmethod
    def func_WeightedStandardizedDecisionMatrix(cls, standardized_matrix, weight_vector):
        weighted_standardized_matrix = np.zeros(standardized_matrix.shape)
        for i in range(weight_vector.shape[0]):
            weighted_standardized_matrix[:, i] = standardized_matrix[:, i] * weight_vector[i]
        return weighted_standardized_matrix

    @classmethod
    def func_PositiveIdealSolution(cls, input_matrix, flag=None):
        if flag is None:
            flag = [True] * input_matrix.shape[1]

        output_matrix = np.zeros(input_matrix.shape)
        for i in range(input_matrix.shape[1]):
            if flag[i]:
                output_matrix[:, i] = (input_matrix[:, i] - np.max(input_matrix[:, i])) ** 2
            else:
                output_matrix[:, i] = (input_matrix[:, i] - np.min(input_matrix[:, i])) ** 2
        return output_matrix

    @classmethod
    def func_NegativeIdealSolution(cls, input_matrix, flag=None):
        if flag is None:
            flag = [True] * input_matrix.shape[1]

        output_matrix = np.zeros(input_matrix.shape)
        for i in range(input_matrix.shape[1]):
            if flag[i]:
                output_matrix[:, i] = (input_matrix[:, i] - np.min(input_matrix[:, i])) ** 2
            else:
                output_matrix[:, i] = (input_matrix[:, i] - np.max(input_matrix[:, i])) ** 2
        return output_matrix

    @classmethod
    def func_IdealSolutionRelativeCloseness(cls, positive_matrix, negative_matrix):
        d_plus = np.zeros(positive_matrix.shape[0])
        d_minus = np.zeros(positive_matrix.shape[0])
        R = np.zeros(positive_matrix.shape[0])
    
        for i in range(positive_matrix.shape[0]):
            d_plus[i] = np.sqrt(np.sum(positive_matrix[i, :]))
            d_minus[i] = np.sqrt(np.sum(negative_matrix[i, :]))
            R[i] = d_minus[i] / (d_plus[i] + d_minus[i])
        return R
