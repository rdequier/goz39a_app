import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

# Chart
fig = make_subplots(rows=1, cols=1)
fig.add_trace(
    go.Scatter(x=np.arange(0,10,1),
               y=np.arange(0,10,1)*2 + np.random.randn(),
               name='Example'),
    row=1, col=1)
fig.update_layout(width=1500)

# Currency Options
dropdown = dcc.Dropdown(
    id='id_currency',
    options=[{"label":'CHF','value':'CHF'},
             {"label":'GBP','value':'GBP'},
             {"label":'SEK','value':'SEK'},
             ],
    value='CHF')

app.layout = dbc.Container(
    [
        html.Div(children=[html.H1(children='Gaussian Mixtures'),
                           html.H2(children='Data Source: ECB')],
                 style={'textAlign':'center','color':'black'}),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(dropdown, md=2),
                dbc.Col(dcc.Graph(id="id_graph",figure=fig), md=10),
            ],
            align="center",
        ),
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)