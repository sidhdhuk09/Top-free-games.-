import plotly.express as px 
from dash import html, dcc
from dash.dependencies import Input, Output
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
    top_50_free_games = free_games_df.nlargest(50, 'recommendations')

    @app.callback(
        Output("bar_chart","figure"),
        Input("recommendation-dropdown","value")  # the dropdown id should match the id of your dropdown in the other file
    )
    def update_bar_chart(selected_game):
        if isinstance(selected_game, str):
            selected_game = [selected_game]

        filtered_data = top_50_free_games[top_50_free_games['name'].isin(selected_game)]

        fig = px.bar(filtered_data,
                    x='name',
                    y='recommendations',
                    title= "Top 50 Free Games by Recommendations",
                    hover_data=['recommendations','name'],
                    color='name'
        )
        fig.update_xaxes(tickangle=45)
        fig.update_yaxes(type="log")
        return fig

    return dcc.Graph(id="bar_chart")





# import plotly.express as px 
# from dash import html, dcc
# from dash import html,dcc,Input,Output
# import pandas as pd
# import ast
# from .ids import *


# def render(app, data):
#     @app.callback(
#             Output("bar_chart","children"),
#             Input("recommendation-dropdown","value")
#     )
#     def parse_recommendations(rec):
#         try:
#             unpack_dict = ast.literal_eval(rec)
#             return unpack_dict.get('total', None) if isinstance(unpack_dict, dict) else None
#         except (ValueError, SyntaxError):
#             return None

#     data['recommendations'] = data['recommendations'].apply(parse_recommendations)
#     data['recommendations'] = pd.to_numeric(data['recommendations'], errors='coerce')

#     data['recommendations'].fillna(0, inplace=True)

#     free_games_df = data[data['is_free'] == True]
#     top_50_free_games = free_games_df.nlargest(50, 'recommendations')


#     # Print the 'name' and 'recommendations' columns of the top 50 free games
#     # print(top_50_free_games[['name', 'recommendations']])
#     # print("Unique games in the top 50: ", top_50_free_games['name'].nunique())

#     def update_bar_chart(dropdown):
#         filtered_data= data.query('Name in @dropdown')
#         if filtered_data.shape[0] == 0:
#             return 
#         fig = px.bar(top_50_free_games,
#                      x='name',
#                      y='recommendations',
#                      title= "Top 50 Free Games by Recommendations",
#                      hover_data=['recommendations','name'],
#                      color='recommendations'
#         )
#         fig.update_xaxes(tickangle=45)  
#         fig.update_yaxes(type="log")
#         return html.Div(dcc.Graph(figure=fig), id=BAR_CHART)

        
        


    # fig = px.bar(top_50_free_games,
    #             x='name',
    #             y='recommendations',
    #             title= "Top 50 Free Games by Recommendations",
    #             hover_data=['recommendations','name'],
    #             color='recommendations'
    #         )
    # fig.update_xaxes(tickangle=45)  
    # fig.update_yaxes(type="log")  #to show data
    # return html.Div(dcc.Graph(figure=fig), id=BAR_CHART)