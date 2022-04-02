from dash import html
import dash_bootstrap_components as dbc 

layout = html.Div(
    dbc.Container(
        [
            html.H1("Experience", className="display-5"),
            html.P("LIST OF JOBS GOES HERE"),
            html.Hr(className="my-2"),
            html.P(
                dbc.Button("Learn more", color="info"), className="lead"
            ),
        ],
        fluid=False,
        className="py-3",
    ),
    className="shadow-sm p-3 mb-3 bg-light rounded-3",
    #xs=12,sm=12,md=12
)