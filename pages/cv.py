from dash import html
import dash_bootstrap_components as dbc 

bio = html.Div(
    dbc.Container(
        [
            dbc.Row([

                #Image
                dbc.Col([
                    dbc.CardImg(
                        src="/static/img/kahin.jpg", 
                        top=True, 
                        className="mt-1 pt-3", 
                        style={
                            'border': 'none',
                            'border-radius':'50% 20% / 10% 40%',
                            'width':'18em',
                            'display': 'block',
                            'margin': 'auto'
                        }
                    )
                ],xs=12,sm=12, md=12, lg=4),
                #Bio
                dbc.Col([

                    html.H1("Kahin Akram, Ph.D.", className="display-4 font-weight-bold"),
                    html.Hr(className="my-2"),
                    html.P(
                        "Visualization expert with a passion for data science. "+ 
                        "Seeking to tackle new data challenges. Achievements include Ph.D. in information visualization "+
                        "from Linköping University, data scientist for a logistics company, "+
                        "and leading UX/UI related projects. Highly skilled in data visualization "+
                        "and creative research thinking." , className="lead"
                    ),
                    html.Hr(),
                    html.P(
                        dbc.Button("Learn more", color="info"), className="lead align-left"
                    ),

                ],
                xs=12,sm=12,md=12, lg=8,
                style={
                    'display': 'block',
                    'margin': 'auto'
                }),


            ])
        ],
        fluid=False,
        className="",
    ),
    className="shadow-sm p-3 mb-3 bg-light rounded-3"

)

#Experience
experience = html.Div(
    dbc.Container(
        dbc.Col([
            html.H1("Experience", className="display-5"),
            html.P("LIST OF JOBS GOES HERE"),
            html.Hr(className="my-2"),
            html.P(
                dbc.Button("Learn more", color="info"), className="lead"
            ),
        ]),
        className="py-3",
    ),
    className="shadow-sm p-3 mb-3 bg-light rounded-3",
)

#Education
education = html.Div(
    dbc.Container(
        children=[
            html.H1("Education", className="display-5"),
            html.P("Education Goes here"),
            html.Hr(className="my-2"),
            html.P(
                dbc.Button("Learn more", color="info"), className="lead"
            ),
        ],
        className="py-3",
    ),
    className="shadow-sm p-3 mb-3 bg-light rounded-3",
)

#Skills
skills = html.Div(
    dbc.Container(
        children=[
            html.H1("Skills", className="display-5"),
            html.P("Skills Goes here"),
            html.Hr(className="my-2"),
            html.P(
                dbc.Button("Learn more", color="info"), className="lead"
            ),
        ],
        className="py-3",
    ),
    className="shadow-sm p-3 mb-3 bg-light rounded-3",
)

#Extracurricular
extra = html.Div(
    dbc.Container(
        children=[
            html.H1("Extracurricular", className="display-5"),
            html.P("Extracurricular Goes here"),
            html.Hr(className="my-2"),
            html.P(
                dbc.Button("Learn more", color="info"), className="lead"
            ),
        ],
        className="py-3",
    ),
    className="shadow-sm p-3 mb-3 bg-light rounded-3",
)

#Certificates
certificates = html.Div(
    dbc.Container(
        children=[
            dbc.Col([
                html.H1("Certificates", className="display-5"),
                html.P("Certificates Goes here"),
                html.Hr(className="my-2"),
            ],)

        ],
        className="py-3",
    ),
    className="shadow-sm p-3 mb-3 bg-light rounded-3",
)

#Final Layout
layout = html.Div(
    dbc.Container(
        children=[
            dbc.Row([bio]),
            dbc.Row([dbc.Col([experience])]),
            dbc.Row([dbc.Col([education])]),
            dbc.Row([dbc.Col([skills])]),
            dbc.Row([dbc.Col([extra])]),
            dbc.Row([dbc.Col([certificates])]),
        ],
        fluid=False,
    )
)

