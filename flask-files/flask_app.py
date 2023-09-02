import pandas as pd
from flask import Flask, request
data = pd.read_csv('/home/boardgames/mysite/bgg_dataset.csv', delimiter=';')

app = Flask(__name__)
@app.route('/search', methods=['GET'])
def ReturnBoardGames():
    print('Category not checked yet.')
    category = request.args.get('category')
    print(category)
    players = int(request.args.get('playerCount'))
    age = int(request.args.get('age'))
    minrate = float(request.args.get('rating'))
    if(category == "ALL"):
        games = data[
                    (data["MinAge"] <= age) &
                    (data['MinPlayers'] <= players) &
                    (data['MaxPlayers'] >= players) &
                    (data['YearPublished'] >= 1) &
                    (data['Name'] != 'Any dummy text')
        ] # I know this part is completely against DRY principles but it kept giving weird errors
        print("Category is ALL")
    else:
        print('Category is different')
        games = data[
                    (data["MinAge"] <= age) &
                    (data['MinPlayers'] <= players) &
                    (data['Domains'].str.contains(category)) &
                    (data['MaxPlayers'] >= players) &
                    (data['YearPublished'] >= 1) &
                    (data['Name'] != 'Any dummy text')
        ] # I know this part is completely against DRY principles but it kept giving weird errors

    print(games)
    games_json = games.to_json(orient='records')
    return games_json
