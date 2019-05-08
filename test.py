'''
Test functions for my nba_scraper module
'''
import pandas as pd
import nba_scraper.nba_scraper as ns

def test_scrape_return():
    dataframe = ns.scrape_game([21800001])
    assert isinstance(dataframe, pd.DataFrame)

def test_scrape_playoffs_return():
    dataframe = ns.scrape_game([41700151])
    assert isinstance(dataframe, pd.DataFrame)

def test_scrape_date_range():
    dataframe = ns.scrape_date_range('2018-01-01', '2018-01-03')
    assert isinstance(dataframe, pd.DataFrame)


