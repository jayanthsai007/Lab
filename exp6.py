from scipy.stats import pearsonr
py = [15, 16, 12, 10, 8]
ai = [18, 11, 10, 20, 17]
r, p_value = pearsonr(py, ai)
# corr,pval = sp
print(f'pearson correlation coefficient:{r}')
print(f'p value is {p_value}')
