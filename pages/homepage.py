from dash import html, Input, Output, callback
import dash_bootstrap_components as dbc 

layout = dbc.Container([
    html.Div(children=[
        dbc.Row([
            
            #Image
            dbc.Col([
                dbc.CardImg(src="/static/img/kahin.jpg", top=True, className="rounded-circle center", style={"width": "20rem"})
            ],xs=12,sm=12, md=5, align="center"),
            
            #Bio
            dbc.Col([
                dbc.CardBody(children=[
                    html.H1("Kahin Akram, Ph.D.", className="display-4 font-weight-bold"),
                    html.Hr(),
                    html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt", className="lead"),
                    html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt", className="lead"),
                    html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt", className="lead"),
                    html.Hr()
                ])
            ],xs=12,sm=12,md=7)
        ],justify="evenly"),
    ]),
 
],
fluid=False,
className="shadow-sm p-3 mb-3 bg-white rounded",
                     
)
