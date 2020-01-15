import pandas as pd

from scratch10.ex02 import peak_to_peak

if __name__ == '__main__':
    tip_df = pd.read_csv('tips.csv')
    print(tip_df.iloc[0:5])
    tip_df['tip_pct'] = tip_df['tip'] / tip_df['total_bill']
    print(tip_df.head())

    grouped = tip_df.groupby(['day', 'smoker'])
    grouped_tip_pct = grouped['tip_pct']
    print(grouped_tip_pct.mean())

    tip_pct_df = grouped_tip_pct.agg(mean='mean', std='std', range=lambda x: x.max() - x.min())
    print(tip_pct_df)

    grouped_tippct_totalbill = grouped[['tip_pct', 'total_bill']]
    print(grouped_tippct_totalbill)
    df = grouped_tippct_totalbill.agg([('mean','mean'), ('std', 'std'), ('range',peak_to_peak)])
    print(df)

    result = grouped.agg({'tip':'max', 'size':'sum'})
    print(result)

    functions = [('mu','mean'), ('sigma', 'std'), ('range', peak_to_peak)]
    result = grouped.agg({'tip_pct':functions, 'total_bill':functions})
    print(result)

    # grouping 컬럼들을 인덱스로 사용하지 않는 경우
    grouped = tip_df.groupby(['day', 'smoker'], as_index=False)