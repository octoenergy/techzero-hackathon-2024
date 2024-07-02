import pandas as pd

class star:
    category_mapping = {
        'GROCERIES': 'Grocery/Supermarket',
        'ENTERTAINMENT': 'Entertainment/Recreation',
        'EATING_OUT': 'Dining/Restaurants',
        'BILLS_AND_SERVICES': 'Utilities',
        'HOME': 'Utilities',
        'TRANSPORT': 'Travel',
        'HOLIDAYS': 'Travel',
        'SHOPPING': 'Clothing/Retail',
        'CLOTHES': 'Clothing/Retail',
        'INCOME': 'General',
        'PAYMENTS': 'General',
        'GENERAL': 'General',
        'EXPENSES': 'General',
        'LIFESTYLE': 'General',
        'DIY': 'General',
        'CHILDREN': 'General',
        'NONE': 'General',
        'CASH': 'General'
    }

    category_carbon_values = {
        "Grocery/Supermarket": (0.5, 1.5),
        "Dining/Restaurants": (1.0, 2.5),
        "Clothing/Retail": (2.0, 5.0),
        "Travel": (5.0, 15.0),
        "Entertainment/Recreation": (1.0, 3.0),
        "Utilities": (2.0, 5.0),
        "General": (1.0, 3.0)
    }

    tbl_nm = 'starling'
    def __init__(self, file):
        self.file = self.map_category(file)
        self.calc_co2()

    @staticmethod
    def table_def():
        str = f"""
            CREATE TABLE IF NOT EXISTS {star.tbl_nm} (
                id SERIAL PRIMARY KEY,
                date DATE,
                counterparty VARCHAR(255),
                reference VARCHAR(255),
                type VARCHAR(255),
                amount DECIMAL(10,2),
                balance DECIMAL(10,2),
                category VARCHAR(255),
                notes TEXT,
                eco_cat TEXT NOT NULL,
                co2_est DECIMAL(10,2) NOT NULL
            )
        """
        return str

    def map_category(self, file):
        file['eco_cat'] = file['Category'].map(star.category_mapping)
        file['Date'] = pd.to_datetime(file['Date'], format='%d/%m/%Y')
        return file

    def calc_co2(self):
        self.file["co2_est"] = self.file.apply(
            lambda row: (star.category_carbon_values.get(row["eco_cat"], (0, 0))[0] +
                         star.category_carbon_values.get(row["eco_cat"], (0, 0))[1]) / 2 * (row["Amount"] / 100),
            axis=1
        ).abs()

