from os.path import join as pjoin, dirname

import numpy as np

import formula
from formula.parts import fromrec

DATA_PATH = pjoin(dirname(formula.__file__), 'data')

SALARY_DATA = np.recfromcsv(pjoin(DATA_PATH, 'salary.csv'))

terms = fromrec(SALARY_DATA)
x, E, P = terms['x'], terms['e'], terms['p']

f = E.formula + P.formula
X, con_mats = f.design(SALARY_DATA, contrasts=dict(E=E.main_effect, P=P.main_effect))

[e_B, e_M, e_P] = E.terms
[p_L, p_M] = P.terms


