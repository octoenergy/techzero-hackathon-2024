import pandas as pd
class amex:
    categories = {
        "Entertainment-Bars & Cafés": "Entertainment/Recreation",
        "General Purchases-Fuel": "General",
        "General Purchases-Groceries": "Grocery/Supermarket",
        "Entertainment-Restaurants": "Dining/Restaurants",
        "General Purchases-General Retail": "Clothing/Retail",
        "General Purchases-Wholesale Stores": "General",
        "General Purchases-Hardware Supplies": "General",
        "General Purchases-Clothing Stores": "Clothing/Retail",
        "Business Services-Mailing & Shipping": "General",
        "General Purchases-Online Purchases": "General",
        "Travel-Lodging": "Travel",
        "General Purchases-Department Stores": "Clothing/Retail",
        "Travel-Rail Services": "Travel",
        "General Purchases-Sporting Goods Stores": "Entertainment/Recreation",
        "Business Services-Advertising Services": "Business Services",
        "Travel-Other Travel": "Travel",
        "General Purchases-Florists & Gardening": "General",
        "General Purchases-Furnishing": "General",
        "Business Services-Professional Services": "Business Services",
        "General Purchases-Pharmacies": "General",
        "Business Services-Other Services": "Business Services",
        "General Purchases-Book Stores": "General",
        "General Purchases-Computer Supplies": "General",
        "Entertainment-Clubs": "Entertainment/Recreation",
        "Travel-Airline": "Travel",
        "Travel-Travel Agencies": "Travel",
        "Travel-Auto Services": "Travel",
        "Business Services-Health Care Services": "Business Services"
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

    tbl_nm = 'amex_raw'
    def __init__(self, file):
        self.file = self.map_category(file)
        self.calc_co2()



    @staticmethod
    def table_def():
        str = f"""
            CREATE TABLE IF NOT EXISTS {amex.tbl_nm} (
                id SERIAL PRIMARY KEY,
                date DATE NOT NULL,
                description TEXT NOT NULL,
                amount DECIMAL(10,2) NOT NULL,
                counterparty TEXT NOT NULL,
                reference TEXT,
                category TEXT NOT NULL,
                eco_cat TEXT NOT NULL,
                co2_est DECIMAL(10,2) NOT NULL
            )
        """
        return str

    def map_category(self, file):
        file['eco_cat'] = file['Category'].map(amex.categories)
        file['Date'] = pd.to_datetime(file['Date'], format='%d/%m/%Y')
        return file

    def calc_co2(self):
        self.file["co2_est"] = self.file.apply(
            lambda row: (amex.category_carbon_values.get(row["eco_cat"], (0, 0))[0] +
                         amex.category_carbon_values.get(row["eco_cat"], (0, 0))[1]) / 2 * (row["Amount"] / 100),
            axis=1
        ).abs()


