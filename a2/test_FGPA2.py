from logging import exception
import pytest
import numpy as np

from FGPA2 import *

def test_read_df():
    assert isinstance(read_df('finanzas2020[1].csv'), pd.DataFrame)

def test_check_empty():
    df = read_df('finanzas2020[1].csv')
    assert len(check_empty(df).columns) == 12
    
def test_df_processing():
    df = read_df('finanzas2020[1].csv')
    df = check_empty(df)
    df = df_processing(df)
    calculos_df = calculos(df)
    assert (calculos_df['ingresos'] > 0).any().any()


def test_df_processing_1():
    df = read_df('finanzas2020[1].csv')
    df = check_empty(df)
    df = df_processing(df)
    calculos_df = calculos(df)
    assert (calculos_df['gastos'] < 0).any().any()

def test_df_processing_2():
    df = read_df('finanzas2020[1].csv')
    df = check_empty(df)
    df = df_processing(df)
    calculos_df = calculos(df)
    assert (calculos_df['ahorros'] != 0).any().any()
