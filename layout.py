from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
from components import bar_chart, dropdown, pie_chart

def create_layout(app, data):
    return dbc.Container(
        [
            dbc.Row([
                dbc.Col(bar_chart.render(app, data), md=12),
            ]),
            dbc.Row([
                dbc.Col([
                    html.H1("Individual Game Ratings"),
                    html.P("Dataset is based on positive user ratings and recommendations"),
                    dropdown.render(app, data)
                ])
            ]),
            dbc.Row([
                dbc.Col(pie_chart.render(app, data), lg=9),
            ])
        ]
    )
