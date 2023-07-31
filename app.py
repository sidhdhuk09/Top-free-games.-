from dash import Dash
import dash_bootstrap_components as dbc
import os
from flask import Flask
from data.util import get_games
from layout import create_layout

PATH = os.path.join(os.getcwd(), "data\steam_app_data.csv")

data = get_games(PATH)

server = Flask(__name__)
app = Dash(__name__,server=server, external_stylesheets=[dbc.themes.COSMO])

app.title = "Top 50 free Computer Video Games of all time"
app.layout = create_layout(app, data)
server=app.server

if __name__ == "__main__":
    app.run_server(debug=True)
