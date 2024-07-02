import psycopg2
import pandas as pd
from matplotlib import pyplot as plt
import io
import base64

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "myapp"
DB_USER = "myuser"
DB_PASSWORD = "mypassword"

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# Create a cursor object
cur = conn.cursor()



def calc_co2():
    cur.execute("SELECT * FROM amex_raw")
    st_amex = cur.fetchall()
    columns = [column[0] for column in cur.description]
    # Create a Pandas DataFrame from the fetched data
    df_amex = pd.DataFrame(st_amex, columns=columns)

    cur.execute("SELECT * FROM starling")
    st_star = cur.fetchall()
    columns = [column[0] for column in cur.description]
    # Create a Pandas DataFrame from the fetched data
    df_star = pd.DataFrame(st_star, columns=columns)
    df_total = pd.concat([df_star, df_amex], ignore_index=True)

    cur.execute("SELECT * FROM topups")
    st_star = cur.fetchall()
    columns = [column[0] for column in cur.description]
    # Create a Pandas DataFrame from the fetched data
    df_topup = pd.DataFrame(st_star, columns=columns)
    df_total['multi'] = df_total['counterparty'].map(df_topup.set_index('merchant')['multi'].to_dict()).fillna(1)
    df_total['eco_co2'] = (df_total['multi']) * df_total['co2_est']

    return df_total



def top10():
    df = calc_co2()
    df = df[df['eco_cat'].isin(["Grocery/Supermarket","Dining/Restaurants","Clothing/Retail","Travel","Entertainment/Recreation"])]
    df.loc[df['counterparty']=='Tesco','eco_co2'] = df.loc[df['counterparty']=='Tesco','eco_co2'] / 10

    top_10_a = df.sort_values('eco_co2', ascending=False).head(10)
    return top_10_a[['date', 'counterparty', 'eco_cat', 'co2_est', 'multi', 'eco_co2']]

def monthly_chart():
    df = calc_co2()
    df['month'] = pd.to_datetime(df['date']).dt.month

    # Create a bar chart with all 12 months
    co2_totals = df.groupby('month')['co2_est'].sum().reindex(range(1, 13), fill_value=0)
    eco_co2_totals = df.groupby('month')['eco_co2'].sum().reindex(range(1, 13), fill_value=0)

    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#F0F8FF')

    x = range(1, 13)
    width = 0.4

    ax.bar(x, co2_totals, width=width, label='co2_est')
    ax.bar([i + width for i in x], eco_co2_totals, width=width, label='eco_co2')

    ax.set_xlabel('Month')
    ax.set_ylabel('Total')
    ax.set_title('Monthly Total Estimated vs Real CO2')
    ax.set_xticks(x)
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.legend()

    # plt.show()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')

    return plot_url

def company_comp():
    df = calc_co2()
    df_comp = df[df['eco_cat'].isin(["Grocery/Supermarket"])]
    df_comp = df_comp[df_comp['counterparty'].isin(['Co-Op','Lidl','Tesco',"Sainsbury's",'Marks & Spencer','Asda'])]
    comp = df_comp[['counterparty', 'amount', 'eco_co2']].groupby('counterparty').sum()
    comp['eff'] = ((comp['amount']*100)/comp['eco_co2']).abs()
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#F0F8FF')

    ax.bar(comp.index, comp['eff'])

    ax.set_xlabel('Shop')
    ax.set_ylabel('KGs CO2 per £100k spend')
    ax.set_title('KGs of CO2 per £100k spend - Carbon Efficiency ')
    ax.set_xticklabels(comp.index, rotation=90)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')

    return plot_url




if __name__ == '__main__':
    company_comp()
    print()