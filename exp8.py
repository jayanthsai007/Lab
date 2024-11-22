import pandas as bear
# outline
ser = bear.Series()
print(f'panda series:{ser}')
# series data structure
name = bear.Series(['J', 'A', 'Y', 'A', 'N', 'T', 'H'])
print(f'panda series:\n{name}')
# data frame data structure
# list
group = bear.DataFrame(['welcome', 'to', 'python'])
print(f'list data frame is:\n{group}')
# dictionaries
list = bear.DataFrame({'name': ['arjun', 'varun'], 'class': ['cse7', 'cse6']})
print(f'Dictionary data frame is:\n{list}')
