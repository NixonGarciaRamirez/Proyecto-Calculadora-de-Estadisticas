import os
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def ruta_rel(ruta):
    d = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(d, ruta)


def load_data(csv_file):
    data = pd.read_csv(ruta_rel(csv_file))
    return data

def anova_analysis(data, dependent_var, independent_var):
    formula = f'{dependent_var} ~ C({independent_var})'
    model = ols(formula, data=data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    return anova_table


def tukey(data, Colm_D = 'Valor', Colm_g = 'Grupo'):
    t = pairwise_tukeyhsd(endog=data[Colm_D], groups=data[Colm_g], alpha=0.05)
    return t


def hypothesis_testing(data, group1, group2, variable, Colm_D = 'Valor'):
    group1_data = data[data[variable] == group1][Colm_D]
    group2_data = data[data[variable] == group2][Colm_D]
    t_stat, p_value = stats.ttest_ind(group1_data, group2_data)
    return t_stat, p_value

