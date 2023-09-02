import pandas as pd
from flask import Flask, request
import numpy as np
data = pd.read_csv('/bgg_dataset.csv', delimiter=';')
domains = data['Domains'].unique()
print(domains)
app = Flask(__name__)
@app.route('/search', methods=['GET'])
def ReturnBoardGames():
    category = request.args.get('category')
    players = int(request.args.get('playerCount'))
    age = int(request.args.get('age'))
    minrate = float(request.args.get('rating'))
    if(category == "ALL"):
        categoryFilter = True
    else:
        categoryFilter = data['category'].isin(category)
    games = data[
                (data["MinAge"] >= age) &
                (categoryFilter) &
                (data['MinPlayers'] <= players) &
                (data['MaxPlayers'] >= players) &
                data['RatingAverage'] >= minrate
    ]
    games_json = games.to_json(orient='records')
    return games_json
    
