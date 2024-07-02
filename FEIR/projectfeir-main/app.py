import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Create a sample DataFrame
df = pd.DataFrame({
    "Tariff": ["Current", "AGILE-BB-24-04-03", "COOP-FIX-12M-24-06-28", "COOP-PP-VAR-20-04-01"],
    "Amount": [430, 420, 380, 390]
})

appliance_df = pd.DataFrame({
    "Name": ["CoolTech Supreme", "FrostGuard Elite", "ChillMaster Pro", "IceFlow Ultra", "Microwave", "Batterry", "SolarPanel"],
    "Consumption": [230, 165, 210, 200, 430, 430, 430],
    "Type": ["Fridge", "Fridge", "Fridge", "Fridge", "Microwave", "Battery", "SolarPanel"]
})


# Create a Dash app instance
external_stylesheets = [
    "https://cdn.jsdelivr.net/npm/@picocss/pico@2.0.6/css/pico.min.css"
]


# Sample data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

fridge_0_kwh_usage = [600, 560, 280, 620, 660, 700, 740, 720, 680, 640, 600, 620]
cumulative_fridge_0 = [sum(fridge_0_kwh_usage[:i+1]) for i in range(len(fridge_0_kwh_usage))]

fridge_1_kwh_usage = [28, 26, 29, 32, 34, 35, 38, 28, 22, 23, 20, 19]
cumulative_fridge_1 = [sum(fridge_1_kwh_usage[:i+1]) for i in range(len(fridge_1_kwh_usage))]

fridge_2_kwh_usage = [15, 14, 14, 15, 12, 13, 14, 15, 14, 12, 11, 10]
cumulative_fridge_2 = [sum(fridge_2_kwh_usage[:i+1]) for i in range(len(fridge_2_kwh_usage))]

fridge_3_kwh_usage = [11, 12, 9.8, 8.7, 7.8, 8, 9, 10, 7, 6, 5, 4]
cumulative_fridge_3 = [sum(fridge_3_kwh_usage[:i+1]) for i in range(len(fridge_3_kwh_usage))]

fridge_4_kwh_usage = [6, 5.4, 6.6, 7, 6.5, 5.4, 6, 5.8, 4.2, 4.5, 4.3, 4]
cumulative_fridge_4 = [sum(fridge_4_kwh_usage[:i+1]) for i in range(len(fridge_4_kwh_usage))]

# Create traces
fig = go.Figure()

fig.add_trace(go.Scatter(x=months, y=cumulative_fridge_0, mode='lines+markers', name="Current Fridge"))
fig.add_trace(go.Scatter(x=months, y=cumulative_fridge_1, mode='lines+markers', name="CoolTech Supreme"))
fig.add_trace(go.Scatter(x=months, y=cumulative_fridge_2, mode='lines+markers', name="FrostGuard Elite"))
fig.add_trace(go.Scatter(x=months, y=cumulative_fridge_3, mode='lines+markers', name="ChillMaster Pro"))
fig.add_trace(go.Scatter(x=months, y=cumulative_fridge_4, mode='lines+markers', name="IceFlow Ultra"))


cost_saving = df['Amount'][0] - min(df['Amount'])

# Layout
fig.update_layout(
    title='Monthly Cumulative Consumption of Different Fridges',
    xaxis_title='Month',
    yaxis_title='Consumption (kWh)',
    legend_title='Fridges'
)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# Define the layout of the app
app.layout = html.Main(className='container', children=[
    html.H1("EARN - Energy Appliance ROI Navigator"),
    dcc.Dropdown(
        id='tariff-dropdown',
        options=[
            {'label': 'Current', 'value': 'Current'},
            {'label': 'AGILE-BB-24-04-03', 'value': 'AGILE-BB-24-04-03'},
            {'label': 'COOP-FIX-12M-24-06-28', 'value': 'COOP-FIX-12M-24-06-28'},
            {'label': 'COOP-PP-VAR-20-04-01', 'value': 'COOP-PP-VAR-20-04-01'}
        ],
        value='Current',
        searchable = False,
        clearable= False
    ),
    dcc.Dropdown(
        id='appliance-type-dropdown',
        options=[
            {'label': 'Fridge', 'value': 'Fridge'},
            {'label': 'Microwave', 'value': 'Microwave'},
            {'label': 'Battery', 'value': 'Battery'},
            {'label': 'SolarPanel', 'value': 'SolarPanel'}
        ],
        value='Fridge',
        searchable = False,
        clearable= False
    ),
    dcc.Dropdown(
        id='appliance-dropdown',
        options=[
            {'label': 'CoolTech Supreme', 'value': 'CoolTech Supreme'},
            {'label': 'Microwave', 'value': 'Microwave'},
            {'label': 'Battery', 'value': 'Battery'},
            {'label': 'SolarPanel', 'value': 'SolarPanel'}
        ],
        value='Fridge',
        searchable = False,
        clearable= False
    ),
    dcc.Graph(id='bar-chart'),
    html.Div(id='tariff-saving', children=f"On your current tariff you are spending 430 GBP/year, just by switching to the best tariff you can save a total of {cost_saving} GBP/year"),
    # dcc.Graph(id='line-chart'),
    dcc.Graph(
        id='fridge-consumption-linechart',
        figure=fig
    ),
    html.Div(id='cost-saving'),
    # dcc.Graph(id='payment-plan-chart')
])

# Define callback to update the bar chart based on the dropdown selection
@app.callback(
    Output('bar-chart', 'figure'),
    Input('tariff-dropdown', 'value')
)
def update_bar_chart(selected_tariff):
    fig = px.bar(df, x='Tariff', y='Amount', title=f'Energy Cost Per Tariff')
    fig.update_traces(marker_color=['purple'] + ['#636EFA'] * (len(df) - 1))
    
    min_value = min(df['Amount'])
    max_value = max(df['Amount'])
    fig.update_yaxes(range=[min_value * 0.9, max_value * 1.1]) 
    return fig


# Define callback to update the line chart based on the dropdown selection
# @app.callback(
#     Output('line-chart', 'figure'),
#     Input('tariff-dropdown', 'value')
# )
# def update_line_chart(selected_tariff):
#     fig = px.line(df, x='Tariff', y='Amount', title=f'Energy Cost Per Tariff', markers=True)
#     return fig

# Callback to update the item dropdown based on category selection
@app.callback(
    Output('appliance-dropdown', 'options'),
    Output('appliance-dropdown', 'value'),
    Input('appliance-type-dropdown', 'value')
)
def set_item_options(selected_category):
    
    
    filtered_df = appliance_df[appliance_df.Type == selected_category]
    options = [{'label': item, 'value': item} for item in filtered_df['Name']]
    value = options[0]['value'] if options else None
    return options, value

# Callback to calculate and display cost-saving
@app.callback(
    Output('cost-saving', 'children'),
    Input('tariff-dropdown', 'value'),
    Input('appliance-dropdown', 'value')
)
def update_cost_saving(selected_tariff, selected_appliance):
    selected_appliance = 'FrostGuard Elite'
    if selected_tariff and selected_appliance:
        # tariff_amount = df.loc[df['Tariff'] == selected_tariff, 'Amount'].values[0]
        # appliance_consumption = appliance_df.loc[appliance_df['Name'] == selected_appliance, 'Consumption'].values[0]
        
        current_consumption = cumulative_fridge_0[len(cumulative_fridge_0) - 1]
        best_consumption = cumulative_fridge_4[len(cumulative_fridge_4) - 1]
        cost_saving = int((current_consumption * 17.2 - best_consumption * 8.2) / 1000)
        
        return f"Cost Saving for {selected_appliance} utilising {selected_tariff} tariff: {cost_saving} GBP"
    return "Select both a tariff and an appliance to see cost saving."


# @app.callback(
#     Output('payment-plan-chart', 'figure'),
#     Input('tariff-dropdown', 'value'),
#     Input('appliance-dropdown', 'value')
# )
# def update_payment_plan_chart(selected_tariff, selected_appliance):
#     if selected_tariff and selected_appliance:
#         # Example parameters
#         investment_cost = 1000  # Cost of the appliance investment
#         monthly_payment = 50    # Monthly payment
#         months = 24             # Duration in months
        
#         tariff_amount = df.loc[df['Tariff'] == selected_tariff, 'Amount'].values[0]
#         appliance_consumption = appliance_df.loc[appliance_df['Name'] == selected_appliance, 'Consumption'].values[0]
#         monthly_cost_saving = tariff_amount - appliance_consumption
        
#         months_range = list(range(1, months + 1))
#         payments = [monthly_payment] * months
#         cost_savings = [monthly_cost_saving * month for month in months_range]

#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=months_range, y=payments, mode='lines', name='Monthly Payment'))
#         fig.add_trace(go.Scatter(x=months_range, y=cost_savings, mode='lines', name='Cost Saving'))
        
#         fig.update_layout(title='Monthly Payment Plan vs Cost Saving',
#                           xaxis_title='Month',
#                           yaxis_title='Amount')
        
#         return fig
    
#     return go.Figure()

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)