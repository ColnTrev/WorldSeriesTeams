import pandas as reader
attr_list = ['win_percent','ab','bb','e','er','era','fp','h','ha','hr','hra','run_diff','so','soa','double','triple']
data = reader.read_csv('data_ordered.csv')

features = data[attr_list]
labels = data[['ws_win']]
features.to_csv('features.csv')
labels.to_csv('labels.csv')
