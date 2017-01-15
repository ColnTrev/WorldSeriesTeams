import pandas as reader
import warnings

# to suppress copy warning from pandas
warnings.filterwarnings('ignore')

def printer(ws_data, team_data, func):
    df = reader.DataFrame()
    for index, row in ws_data.iterrows():
        for windex, wrow in team_data.iterrows():
            if wrow['year'] == row['year']:
                if func(wrow, row):
                    if wrow['ws_win'] == 'Y':
                        wrow['ws_win'] = 0
                    else:
                        wrow['ws_win'] = 1
                    df = df.append(wrow)
    return df

def winner(wrow, row):
    return (wrow['franchise_id'] == row['team_id_winner']) or (wrow['team_id'] == row['team_id_winner'])
def loser(wrow, row):
    return (wrow['franchise_id'] == row['team_id_loser']) or (wrow['team_id'] == row['team_id_loser'])

teams = reader.read_csv('team.csv')
postseason = reader.read_csv('postseason.csv')

team_data = teams[['year', 'team_id', 'franchise_id','w', 'g','ws_win', 'r', 'ab', 'h','double', 'triple', 'hr', 'bb', 'so', 'ra', 'er', 'era', 'ha', 'hra', 'soa', 'e', 'fp', 'name']]
ws_data = postseason[postseason['round'] == 'WS']
ws_data = ws_data[ws_data['year'] >= 1903]

'''
I read on 
https://www.kaggle.com/cm1291/d/seanlahman/the-history-of-baseball/worst-world-series-winners-since-1900/discussion 
that we can normalize some of the data by calculating win percentage and adjusted run differential.
What this allows us to do is visualize all teams in terms of a percentage of wins and run differential out of a 162 game (1983 onward) season. 
This is beneficial because there were some seasons where the number of games and/or the number of strikes were different.
''' 
# calculating win percentage and adjusted run differential
wp = team_data['w'] / team_data['g'] * 100
ard = (team_data['r'] / team_data['g'] * 162) - (team_data['ra']/team_data['g'] * 162)

team_data['win_percent'] = reader.Series(wp, index=team_data.index)
team_data['run_diff'] = reader.Series(ard, index=team_data.index)
win_frame = printer(ws_data, team_data, winner)
lose_frame = printer(ws_data, team_data, loser)

reader.concat([win_frame, lose_frame], axis = 0).sort_values(['year', 'ws_win']).to_csv('data_combiner.csv')
