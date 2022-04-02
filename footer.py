from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Navbar([
    dbc.Container(
        children=[
            #Logo and brand name
            html.A(
                [
                    dbc.Row(
                        [dbc.Col([dbc.NavbarBrand("Dr. Kay",className="ms-2,")])],
                        align="center",
                        className="g-0, font-weight-bold"
                    )
                ],
            #style={"textDecoration":"none"},
            ),
        ],
    fluid=False,
    style={"padding-top":"60px"}
    )
],
color="light",
dark=False,
className="shadow-sm p-3 mb-3 bg-white rounded",

)
