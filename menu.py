from dash import html, Output, Input, State, callback
import dash_bootstrap_components as dbc

dropdown_items = [
    dbc.DropdownMenuItem("Dash Plotly", header=True),
    dbc.DropdownMenuItem("Dash template", href="/dash-template"),
    dbc.DropdownMenuItem("This portfolio", href="/portfolio"),
    dbc.DropdownMenuItem("D3.js", header=True),
    dbc.DropdownMenuItem("Radial", href="/d3-projects"),
    dbc.DropdownMenuItem("Python", header=True),
    dbc.DropdownMenuItem("Project 1", href="/python"),
]

links = dbc.Row(
    [
        dbc.Col(dbc.NavLink("Cv", href="/cv", active="exact")),
        dbc.Col(dbc.NavLink("Research", href="/research", active="exact")),
        dbc.Col(
            dbc.DropdownMenu(
            label="Projects",
            children=dropdown_items,
            #align_end=True, 
            nav=True,
            in_navbar=True,
            ),
        ),
        dbc.Col(dbc.NavLink("Books", href="/books", active="exact")),
        dbc.Col(dbc.NavLink("Contact", href="/contact", active="exact")),
    ],
    className="navbar-nav ",
)


layout = dbc.Navbar([
    dbc.Container(
        children=[
            #Logo and brand name
            html.A(
                [
                    dbc.Row(
                        [dbc.Col([dbc.NavbarBrand("Dr. Kay", href="/", className="ms-2,")])],
                        align="center",
                        className="g-0, font-weight-bold"
                    )
                ],
            #style={"textDecoration":"none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler",n_clicks=0),
            dbc.Collapse(
                links,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
                className="justify-content-end"
            )
        ],
    fluid=False
    )
],
color="light",
dark=False,
className="shadow-sm p-3 mb-3 bg-white rounded"
)

# add callback for toggling the collapse on small screens
@callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
