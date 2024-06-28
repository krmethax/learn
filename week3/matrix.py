from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Sample data
data = {
    'day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'Outlook': ['overcast', 'overcast', 'overcast', 'overcast', 'rainy', 'rainy', 'rainy', 'rainy', 'rainy', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny'],
    'Temperature': [83, 64, 72, 81, 70, 68, 65, 75, 71, 85, 80, 72, 69, 75],
    'Humidity': [86, 65, 90, 75, 96, 80, 70, 80, 91, 85, 90, 95, 70, 70],
    'Windy': [False, True, True, False, False, False, True, False, True, False, True, False, False, True],
    'Play': ['yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'no', 'yes', 'yes']
}

df = pd.DataFrame(data)

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Weather Data Analysis using Scatter Matrix'),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': 'Temperature', 'value': 'Temperature'},
            {'label': 'Humidity', 'value': 'Humidity'}
        ],
        value=['Temperature', 'Humidity'],
        multi=True
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def update_scatter_matrix(dims):
    fig = px.scatter_matrix(df, dimensions=dims, color="Play")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
