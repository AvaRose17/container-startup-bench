\# container-bench



Goal: run a tiny C program in a container and measure container \*\*startup time\*\* + \*\*RSS memory\*\*, outputting `results.csv` and `summary.csv`.



\## How to run (once finished)

1\) `docker build -t bench .`

2\) `.\\\\benchmark.ps1`

3\) `python .\\\\scripts\\\\aggregate.py`



Outputs:

\- `results.csv` (raw runs)

!\[Startup latency](figures/startup\_latency.png)

\- `summary.csv` (aggregated stats)

