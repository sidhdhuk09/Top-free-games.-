# from dash import html, dcc
# import pandas as pd
# import ast
# from .ids import *

# def parse_recommendations(rec):
#     try:
#         rec_dict = ast.literal_eval(rec)
#         return rec_dict.get('total', None) if isinstance(rec_dict, dict) else None
#     except (ValueError, SyntaxError):
#         return None

# def render(app, data):
#    
#     data['recommendations'] = data['recommendations'].apply(parse_recommendations)
#     data['recommendations'] = pd.to_numeric(data['recommendations'], errors='coerce')

#    
#     data['recommendations'].fillna(0, inplace=True)

#    
#     free_games_df = data[data['is_free'] == True]
#     top_50_free_games = free_games_df.nlargest(50, 'recommendations')

#     game_names = top_50_free_games["name"].unique()
#     first_value = game_names[0]
#     options = [{"label": i, "value": i} for i in game_names]

#     return html.Div(
#         [
#             dcc.Dropdown(
#                 options=options,
#                 placeholder="Choose a game",
#                 value=first_value,
#                 multi=False,
#                 className="mb-3",
#                 id=DROPDOWN
#             )
#         ]
#     )




# from dash import html, dcc, Input, Output

# def render(app,data):
#     get_recc = sorted(data['recommendations'].unique())
#     name_list= [{"label":l, "value":l} for l in get_recc]

#     @app.callback(
#         Output("Select-recommendations","value"),
#         Input("Select-allrecommendations","n-clicks"),
#     )
#     def select_all_recc(n):
#         return select_all_recc
    
#     dropdown=html.Div(
#         {
#             dcc.Dropdown(
#         options= get_recc,
#         placeholder="names",
#         multi=True,
#         className="mb-3",
#         id="recommendation-dropdown",
#         value="Name"
#             ),
#             html.Button(
#         children=["Select all recommendations"],
#         className="dropdown-button",
#         id="Select-allrecommendations-button",
#         n_clicks=0

#             )
#         }
#     )
#     return dropdown

# from dash import html, dcc, Input, Output

# def render(app, data):
#     get_recc = sorted(data['recommendations'].unique())
#     name_list = [{"label": l, "value": l} for l in get_recc]

#     dropdown=html.Div(
#         [
#             dcc.Dropdown(
#                 options= name_list,
#                 placeholder="Select a game",
#                 multi=True,
#                 className="mb-3",
#                 id="recommendation-dropdown",
#                 value=get_recc[0]
#             ),
#             html.Button(
#                 children=["Select all recommendations"],
#                 className="dropdown-button",
#                 id="Select-allrecommendations-button",
#                 n_clicks=0
#             )
#         ]
#     )
#     return dropdown

from dash import html, dcc, Input, Output,Dash
import ast
from dash import html, dcc
import pandas as pd
import ast
from .ids import *


def render(app, data):
    # Parse 'recommendations' column
    def parse_recommendations(rec):
        try:
            unpack_dict = ast.literal_eval(rec)
            return unpack_dict.get('total', None) if isinstance(unpack_dict, dict) else None
        except (ValueError, SyntaxError):
            return None

    data['recommendations'] = data['recommendations'].apply(parse_recommendations)
    data['recommendations'] = pd.to_numeric(data['recommendations'], errors='coerce')
    data['recommendations'].fillna(0, inplace=True)

    # Get the top 50 free games
    free_games_df = data[data['is_free'] == True]
    top_50_free_games = free_games_df.nlargest(50, 'recommendations')

    # Create a sorted list of game names
    get_names = sorted(top_50_free_games['name'].unique())
    name_list = [{"label": l, "value": l} for l in get_names]

    @app.callback(
        Output("recommendation-dropdown", "value"),
        Input("Select-allrecommendations-button", "n_clicks"),
        Input("clear-allrecommendations-button", "n_clicks")
    )
    def select_all_names(n_select, n_clear):
        if n_select and n_select > n_clear:  
            return get_names  
        elif n_clear and n_clear > n_select: 
            return []  

        return []  

    dropdown = html.Div([
        dcc.Dropdown(
            options=name_list,
            placeholder="names",
            multi=True,
            className="mb-3",
            id="recommendation-dropdown"
        ),
        html.Button(
            children=["Select all recommendations"],
            className="dropdown-button",
            id="Select-allrecommendations-button",
            n_clicks=0
        ),
        html.Button(
            children=["Clear all selections"],
            className="dropdown-button",
            id="clear-allrecommendations-button",
            n_clicks=0
        )
    ])

    return dropdown

