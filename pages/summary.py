from dash import html
import dash_bootstrap_components as dbc 

layout = html.Div(
    dbc.Container(
        [
            html.H1("Summary", className="display-5"),
            html.P(
                "Visualization expert with a passion for data science. "+ 
                "Seeking to tackle new data challenges. Achievements include Ph.D. in information visualization "+
                "from Linköping University, data scientist for a logistics company, "+
                "and leading UX/UI related projects. Highly skilled in data visualization "+
                "and creative research thinking.", className='font-weight-light' 
            ),
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