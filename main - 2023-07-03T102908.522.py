import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Sample data for available trailers and freight
available_trailers_data = {
    'Trailer ID': ['TR001', 'TR002', 'TR003', 'TR004'],
    'Location': ['Warehouse A', 'Warehouse B', 'Warehouse C', 'Warehouse D'],
    'Status': ['Available', 'Available', 'In Use', 'Available']
}

freight_data = {
    'Freight ID': ['F001', 'F002', 'F003'],
    'Source': ['Warehouse A', 'Warehouse B', 'Warehouse D'],
    'Destination': ['Warehouse B', 'Warehouse C', 'Warehouse A']
}

# Create DataFrames from the sample data
df_available_trailers = pd.DataFrame(available_trailers_data)
df_freight = pd.DataFrame(freight_data)

# Create the Dash application
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1('Tractor Trailers Dashboard'),
    
    html.Div([
        html.H2('Available Trailers'),
        html.Table(
            # Generate table rows dynamically from the available trailers data
            [html.Tr([html.Th(col) for col in df_available_trailers.columns])] +
            [html.Tr([
                html.Td(df_available_trailers.iloc[i][col]) 
                for col in df_available_trailers.columns
            ]) for i in range(len(df_available_trailers))]
        )
    ]),
    
    html.Div([
        html.H2('Freight to be Moved'),
        html.Table(
            # Generate table rows dynamically from the freight data
            [html.Tr([html.Th(col) for col in df_freight.columns])] +
            [html.Tr([
                html.Td(df_freight.iloc[i][col]) 
                for col in df_freight.columns
            ]) for i in range(len(df_freight))]
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
