import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# def

# def chart_before_after_improvements():

#     before_after_improvements_df['Baseline (gCO2)'] = before_after_improvements_df['Baseline (kWh)']*before_after_improvements_df['carbon_intensity (gCO2/kWh)']
# before_after_improvements_df['After project (gCO2)'] = before_after_improvements_df['After project (kWh)']*before_after_improvements_df['carbon_intensity (gCO2/kWh)']


def add_carbon_intensity_to_df(hh_dataf: pd.DataFrame) -> pd.DataFrame:
    org_col = hh_dataf.columns[0]
    carbon_intensity = pd.read_csv('../data/carbon_intensity.csv', index_col=0)
    carbon_intensity.index = pd.to_datetime(carbon_intensity.index, utc=True)
    carbon_intensity.dropna(inplace=True)
    carbon_emission_profile = pd.merge(hh_dataf,
                                       carbon_intensity,
                                       left_index=True,
                                       right_index=True,
                                       how='left')
    carbon_emission_profile[
        'Total carbon emissions (gCO2)'] = carbon_emission_profile[
            org_col] * carbon_emission_profile['carbon_intensity (gCO2/kWh)']
    return carbon_emission_profile


def create_avg_consumption_and_carbon_intensity_chart(
        hh_dataf: pd.DataFrame) -> str:
    carbon_emission_profile = add_carbon_intensity_to_df(hh_dataf)

    avg_day = carbon_emission_profile.groupby(
        [carbon_emission_profile.index.hour]).mean()
    # avg_day.columns = avg_day.columns.droplevel(0)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(x=avg_day.index,
                             y=avg_day['Electricity consumption (kWh)'],
                             mode='lines',
                             name='Electricity consumption (kWh)'),
                  secondary_y=False)
    fig.add_trace(go.Scatter(x=avg_day.index,
                             y=avg_day['carbon_intensity (gCO2/kWh)'],
                             mode='lines',
                             name='Carbon intensity (gCO2/kWh)'),
                  secondary_y=True)

    # Set y-axes titles
    fig.update_yaxes(title_text="Consumption (kWh)", secondary_y=False)
    fig.update_yaxes(title_text="Carbon intensity (gCO2/kWh)",
                     secondary_y=True)

    fig.update_layout(
        title=f'Average Carbon Emissions and Consumption',
        xaxis_title='Hour of Day',
        yaxis_title='Carbon Emissions (gCO2)',
        width=500,
        height=500,
        margin=go.layout.Margin(
            l=0,  #left margin
            r=0,  #right margin
            b=0,  #bottom margin
            t=30,  #top margin
        ),
        legend=dict(orientation="h", y=-0.2),
    )
    return fig.to_html(full_html=False)


def create_avg_daily_consumption_chart(hh_dataf: pd.DataFrame) -> str:
    daily_avg_hh_consumption_before_improvements = hh_dataf.groupby(
        [hh_dataf.index.hour]).agg({'Electricity consumption (kWh)': 'mean'})
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=daily_avg_hh_consumption_before_improvements.index,
                   y=daily_avg_hh_consumption_before_improvements[
                       'Electricity consumption (kWh)'],
                   mode='lines',
                   name='Before Improvements'))

    fig.update_layout(
        title='Average Hourly Consumption',
        xaxis_title='Hour of Day',
        yaxis_title='Consumption (kWh)',
        width=500,
        height=500,
        margin=go.layout.Margin(
            l=0,  #left margin
            r=0,  #right margin
            b=0,  #bottom margin
            t=30,  #top margin
        ),
    )
    return fig.to_html(full_html=False)


def create_overall_chart(dataf: pd.DataFrame) -> str:
    # Resample data
    daily_consumption = dataf['Electricity consumption (kWh)'].resample(
        'd').mean()
    weekly_consumption = dataf['Electricity consumption (kWh)'].resample(
        'W').mean()
    monthly_consumption = dataf['Electricity consumption (kWh)'].resample(
        'ME').mean()

    # Create traces
    trace_daily = go.Scatter(x=daily_consumption.index,
                             y=daily_consumption,
                             mode='lines',
                             name='Daily Consumption')
    trace_weekly = go.Scatter(x=weekly_consumption.index,
                              y=weekly_consumption,
                              mode='lines',
                              name='Weekly Consumption')
    trace_monthly = go.Scatter(x=monthly_consumption.index,
                               y=monthly_consumption,
                               mode='lines',
                               name='Monthly Consumption')

    # Create figure
    fig = go.Figure()

    # Add traces to figure
    fig.add_trace(trace_daily)
    fig.add_trace(trace_weekly)
    fig.add_trace(trace_monthly)

    # Update layout
    fig.update_layout(title='Electricity Consumption Over Time',
                      xaxis_title='Date',
                      yaxis_title='Electricity consumption (kWh)',
                      legend_title='Resample Frequency',
                      template='plotly')
    return fig.to_html(full_html=False)


def get_peak_electricity_import(hh_dataf: pd.DataFrame) -> float:
    return hh_dataf['Electricity import (kWh)'].max()
