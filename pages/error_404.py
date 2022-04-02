from dash import html
import dash_bootstrap_components as dbc 

layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H1("404: Page not found", className="text-danger alert alert-danger"),
                    html.Hr(),
                    html.P(f"The pathname was not recognised..."),
                ]) 
            ])
        ],md=12)
    ])
])