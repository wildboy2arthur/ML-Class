param_grid = {
    'svc__kernel': ['linear', 'rbf'],
    'svc__C':[0.1, 0.5, 0.8, 1, 5],
    'svc__gamma':np.arange(0.2, 1, 0.2)
}
print(param_grid)