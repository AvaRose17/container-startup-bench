import pandas as pd

df = pd.read_csv('results.csv')

summary = df.groupby('runtime').agg(
    startup_ms_mean=('startup_ms', 'mean'),
    startup_ms_std=('startup_ms', 'std'),
    startup_ms_p50=('startup_ms', lambda x: x.quantile(0.50)),
    startup_ms_p95=('startup_ms', lambda x: x.quantile(0.95)),
    rss_kb_mean=('rss_kb', 'mean'),
)

summary.to_csv('summary.csv')
print(summary)
