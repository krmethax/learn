from dash import Dash, html, dcc
import dash_table
import pandas as pd

# Sample DataFrame creation for demonstration
data = pd.DataFrame({
    'Overcast': [64, 72, 81],
    'Rainy': ['70', '68', '65'],
    'Sunny': [80, 72, 69]
    
})

# Create a Dash application
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    style={'backgroundColor': '#f2f2f2', 'padding': '20px'},  # Background color and padding for the entire layout
    children=[
        html.H1('Weather Forecast', style={'textAlign': 'center'}),  # Center align the heading

        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in data.columns],
            data=data.to_dict('records'),
            style_table={
                'overflowX': 'auto',
                'backgroundColor': '#ffffff',  # Background color for the table
                'border': '1px solid #cccccc',  # Border color
                'borderRadius': '5px'  # Border radius to round corners
            },
            style_cell={
                'height': 'auto',
                'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                'whiteSpace': 'normal',
                'textAlign': 'center'  # Center align cell text
            },
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
