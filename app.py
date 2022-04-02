from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

#import local files 
from pages import homepage, cv, error_404
import menu

#Initiate app
app = Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)
server = app.server 

bio = html.Div(id='page-content')
app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    menu.layout,
    bio,
],fluid=False)


@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return homepage.layout
    if pathname == '/cv':
        return cv.layout
    else:
        return error_404.layout

if __name__ == '__main__':
    app.run_server(debug=True)
