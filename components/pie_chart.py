import plotly.express as px 
from dash import html, dcc
    
import pandas as pd
import ast
from .ids import *


def render(app, data):
    def parse_recommendations(rec):
        try:
            unpack_dict = ast.literal_eval(rec)
            return unpack_dict.get('total', None) if isinstance(unpack_dict, dict) else None
        except (ValueError, SyntaxError):
            return None

    data['recommendations'] = data['recommendations'].apply(parse_recommendations)
    data['recommendations'] = pd.to_numeric(data['recommendations'], errors='coerce')

    data['recommendations'].fillna(0, inplace=True)

    free_games_df = data[data['is_free'] == True]
    top_50_free_games = free_games_df.nlargest(100, 'recommendations')

    # print(top_50_free_games[['name', 'recommendations']])
    # print("Unique games in the top 50: ", top_50_free_games['name'].nunique())

    fig = px.pie(top_50_free_games,
                values='recommendations',
                names='name',
                title= "Top 50 Free Games by Recommendations"
            )
    
    return html.Div(dcc.Graph(figure=fig), id=PIE_CHART)
