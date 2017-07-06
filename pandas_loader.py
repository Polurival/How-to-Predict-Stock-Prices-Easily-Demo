import pandas as pd


def load_stock_file(filename, column='Open'):
    '''
    Gain list of prices from defined column of csv file
    Csv source, for example - https://www.google.com/finance/historical?q=NASDAQ%3AGOOGL&ei=Xu6wWKnDAcS1jAGX6a-ACg
    :param filename: for example 'twtr.csv'
    :param column: for example 'Close'
    :return: list, for example [17.68, 17.940000000000001, 17.66, ....]
    '''
    prices = pd.read_csv(filename)
    open_prices_column = prices[column] #you can also use df['column_name']

    raw_open_data = []
    for price in open_prices_column:
        raw_open_data.append(str(price))
    raw_open_data.append('') # need for right structure

    return raw_open_data
