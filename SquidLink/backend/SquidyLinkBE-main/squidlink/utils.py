import pandas as pd
from squidlink.plots import viz_class


def load_facility_hh_data(facility_id: int) -> pd.DataFrame:
    """Load half-hourly data for a facility."""
    dummy_dataf = pd.read_csv(r"/app/csv/dummy_data.csv", index_col=0)
    dummy_dataf.index = pd.to_datetime(dummy_dataf.index)
    col_index = facility_id % len(dummy_dataf.columns)
    print(col_index, len(dummy_dataf.columns))
    temp_dataf = dummy_dataf.iloc[:, col_index].to_frame()
    temp_dataf.columns = ['Electricity consumption (kWh)']
    return temp_dataf


if __name__ == "__main__":
    facility = viz_class.Facility(1)
    print(facility.viz_avg_elec_data())
    # print(load_facility_hh_data(1))
