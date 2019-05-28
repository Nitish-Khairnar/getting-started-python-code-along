# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data=yaml.load(f)
f.close()
#print(data)
# Find data type of the file
print('type of file is',(type(data)))

# In which city, and at which venue the match was played and where was it played ?
#print(data.keys())
city=data['info']['city']
venue= data['info']['venue']
print('the match was played in', city, venue)

# Which are all the teams that played in the tournament ? How many teams participated in total?
#print('*_*'*20)
team1= data['info']['teams'][0]
team2= data['info']['teams'][1]
print('The match was played between', team1, 'and', team2)
# Which team won the toss and what was the decision of toss winner ?
toss_winner=data['info']['toss']['winner']
decision=data['info']['toss']['decision']
print('the toss was won by', toss_winner, 'and they decided to', decision)

# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler=(data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler'])
first_batsmen=(data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman'])
print('The first bowler was',first_bowler, 'and the first_batsmen was', first_batsmen)

# How many deliveries were delivered in first inning ?
deliveries_bowled=len(data['innings'][0]['1st innings']['deliveries'])
print('the number of delvcireis vowlwded weere', deliveries_bowled)

# How many deliveries were delivered in second inning ?
twodeliveries_bowled=len(data['innings'][1]['2nd innings']['deliveries'])
print(twodeliveries_bowled)

# Which team won and how ?
team_won=data['info']['outcome']['winner']
how=data['info']['outcome']['by']['runs']
print(team_won,'by',how,'runs')


