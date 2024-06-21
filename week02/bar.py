from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Sample DataFrame creation for demonstration
data = pd.DataFrame({
    'Outlook': ['overcast', 'rainy', 'sunny'],
    'Temperature': [70, 85, 45],
    'Play': ['Yes', 'No', 'Yes']
})

# Create a bar chart using Plotly Express
fig = px.bar(data, x='Outlook', y='Temperature',color='Play', title='Temperature by Outlook')

# Create a Dash application
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    style={'backgroundColor': '#f9f9f9', 'padding': '20px'},  # Background color and padding for the entire layout
    children=[
        html.H1('Weather Forecast', style={'textAlign': 'center'}),  # Center align the heading

        dcc.Graph(
            id='bar-chart',
            figure=fig
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
