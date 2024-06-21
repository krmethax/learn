from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Sample DataFrame creation for demonstration
data = pd.DataFrame({
    'Temperature': [25, 22, 28],
    'Humidity': [50, 60, 55],
    'Play': ['Yes', 'No', 'Yes']  # Example categorical variable for color coding
})

# Create a scatter plot using Plotly Express
fig = px.scatter(data, x='Temperature', y='Humidity', color='Play', title='Weather Forecast')

# Create a Dash application
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1('Weather Forecast'),
    dcc.Graph(
        id='scatter-plot',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
