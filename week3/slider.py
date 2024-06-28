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
    html.H4('Analysis of Iris Dataset using Scatter Matrix'),
    dcc.Dropdown(
        id="dropdown-y",
        options=[
            {'label': 'Humidity', 'value': 'Humidity'},
            {'label': 'Windy', 'value': 'Windy'}
        ],
        value=['Humidity', 'Windy'],  # Initial value, can be a list of default options
        multi=True,  # Allow multiple selections
        clearable=False
    ),
    dcc.Graph(id="graph"),
    dcc.RangeSlider(
        id='day-slider',
        min=df['day'].min(),
        max=df['day'].max(),
        value=[df['day'].min(), df['day'].max()],
        marks={str(day): str(day) for day in df['day']},
        step=None
    ),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("day-slider", "value"), Input("dropdown-y", "value")]
)
def update_scatter_plot(selected_days, y_dims):
    filtered_df = df[(df['day'] >= selected_days[0]) & (df['day'] <= selected_days[1])]
    
    fig = px.scatter(filtered_df, x='Temperature', y=y_dims[0], color='Play',
                     labels={'Temperature': 'Temperature (°F)', y_dims[0]: y_dims[0]})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
