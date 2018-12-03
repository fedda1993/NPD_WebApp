# -*- coding: utf-8 -*-
"""
Data processing for NPD web app
"""
import os
import pandas as pd

project_root = os.path.abspath(os.path.join(os.getcwd(), os.pardir, os.pardir))
data_folder = os.path.join(project_root, 'data')
data_folder_raw = os.path.join(data_folder, 'raw')
fp = os.path.join(data_folder_raw, 'field_production_yearly.csv')

def get_data():
        url = "http://hotell.difi.no/download/npd/field/production-yearly-by-field"
        df = pd.read_csv(url, delimiter=";")
        return df


def process_data(df):
    """
    Melt the dataset to put all columns into a variables column
    """
    df2 = df.melt(
        id_vars=['prfInformationCarrier', 'prfYear', 'prfNpdidInformationCarrier'],
        value_vars=['prfPrdOilNetMillSm3', 'prfPrdGasNetBillSm3', 'prfPrdNGLNetMillSm3', 'prfPrdCondensateNetMillSm3', 'prfPrdOeNetMillSm3', 'prfPrdProducedWaterInFieldMillSm3']
        )

    return df2
