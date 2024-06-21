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
], style={'backgroundColor': 'pink'})  

if __name__ == '__main__':
    app.run(debug=True)
