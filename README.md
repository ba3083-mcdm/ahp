# Analytic Hierarchy Process (AHP)

This repository provides an implementation of the Analytic Hierarchy Process (AHP), a widely used multi-criteria decision-making method for ranking alternatives based on pairwise comparisons.

---

## Overview

The Analytic Hierarchy Process (AHP) is a structured technique for organizing and analyzing complex decisions. It allows decision-makers to model a problem in a hierarchy and derive priority weights using pairwise comparisons.

This project includes:
- Construction of pairwise comparison matrices
- Computation of priority weights
- Consistency analysis (CI)
- Examples provided by students

---

## Features

- Pairwise comparison matrix input  
- Weight calculation (eigenvector/normalization method)  
- Consistency Index (CI) calculation  
- Consistency Ratio (CR) check  
- Easy-to-use and modular code  

---

## Methodology

### 1. Pairwise Comparison Matrix

Given \( n \) criteria, construct a matrix:

$$A = (a_{ij}), \quad a_{ij} = \frac{1}{a_{ji}}, \quad a_{ii} = 1$$

---

### 2. Weight Calculation

Weights are computed using:
- **Row normalization method**

---

### 3. Consistency Check

Consistency Index:

$$CI = \frac{\lambda_{\max} - n}{n - 1}$$

- \( RI \): Random Index  
- Acceptable if: **CR < 0.1**

---

## Example

```python
import numpy as np
from MCDM import AHP

C = np.array([
    [1, 3, 5],
    [1/3, 1, 2],
    [1/5, 1/2, 1]
])

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

ahp = AHP(C, B)

weigts = ahp.weight_vector()
scores = ahp.score_matrix()
global_score = ahp.global_score()
CI = ahp.CI()

print("Weight vector:", weigts)
print("Score matrix:", scores)
print("Global scores:", global_score )
print("CI:", CI)
