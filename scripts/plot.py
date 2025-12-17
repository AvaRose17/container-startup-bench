import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv", encoding="utf-16")

# mean + std per runtime
g = df.groupby("runtime")["startup_ms"]
means = g.mean()
stds = g.std()

plt.figure()
plt.bar(means.index, means.values, yerr=stds.values)
plt.ylabel("Startup latency (ms)")
plt.title("Container startup latency (mean ± std)")

plt.tight_layout()
plt.savefig("figures/startup_latency.png", dpi=200)
print("Saved figures/startup_latency.png")
