import pandas as pd
import numpy as np

def aggregate_and_analyze(data_dir):
    """Aggregate and analyze data from multiple sources."""
    # Load data from various sources
    df1 = pd.read_csv(f'{data_dir}/source1.csv')
    df2 = pd.read_excel(f'{data_dir}/source2.xlsx')
    df3 = pd.read_json(f'{data_dir}/source3.json')

    # Concatenate dataframes
    df = pd.concat([df1, df2, df3], ignore_index=True)

    # Perform data cleaning and preprocessing
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date')

    # Calculate aggregated metrics
    df['total_value'] = df['value1'] + df['value2'] + df['value3']
    df['average_value'] = df['total_value'] / 3
    df['std_dev'] = df['total_value'].std()

    # Perform advanced analysis
    trends = df.groupby('category')['total_value'].mean().sort_values(ascending=False)
    anomalies = df[df['total_value'] > df['average_value'] + 2 * df['std_dev']]

    return {
        'trends': trends,
        'anomalies': anomalies
    }

if __name__ == '__main__':
    results = aggregate_and_analyze('data/')
    print('Top Trends:')
    print(results['trends'])
    print('\
Anomalies:')
    print(results['anomalies'])
