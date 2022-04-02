from turtle import width
from dash import html, Input, Output, callback
import dash_bootstrap_components as dbc 

layout = dbc.Col(
    html.Div(
        [
            html.H2("Change the background", className="display-3"),
            html.Hr(className="my-2"),
            html.P(
                "Swap the background-color utility and add a `.text-*` color "
                "utility to mix up the look."
            ),
            dbc.Button("Example Button", color="light", outline=True),
        ],
        className="h-100 p-5 text-white bg-dark rounded-3",
    ),
    md=12,
)