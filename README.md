## learn

# input
from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the values in the text boxes to see callbacks in action!"),
    html.Div([
        "Input 1: ",
        dcc.Input(id='my-input-1', value='initial value 1', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output-1'),
    html.Br(),
    html.Div([
        "Input 2: ",
        dcc.Input(id='my-input-2', value='initial value 2', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output-2'),
])


@callback(
    Output(component_id='my-output-1', component_property='children'),
    Input(component_id='my-input-1', component_property='value')
)
def update_output_div1(input_value1):
    return f'Output 1: {input_value1}'


@callback(
    Output(component_id='my-output-2', component_property='children'),
    Input(component_id='my-input-2', component_property='value')
)
def update_output_div2(input_value2):
    return f'Output 2: {input_value2}'


if __name__ == '__main__':
    app.run(debug=True)


# Graph
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5, 20, 15, 12],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal", "Lavel", "Lavel", "Lavel"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash', style={'color': 'red', 'text-align': 'right'}),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''', style={'color': 'red', 'text-align': 'right'}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
], style={'backgroundColor': 'pink'})  # Set the background color here

if __name__ == '__main__':
    app.run(debug=True)

