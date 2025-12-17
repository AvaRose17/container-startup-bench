$RUNTIME = "docker"
$RUNS = 20
$outfile = "results.csv"

"runtime,run,startup_ms,mem_mb,rss_kb" | Out-File $outfile

for ($i = 1; $i -le $RUNS; $i++) {
    $start = Get-Date

    $output = docker run --rm bench

    $end = Get-Date
    $ms = ($end - $start).TotalMilliseconds

    $lines = $output -split "`n" | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" }
    $data = $lines[-1] -split ","

    $mem = $data[0]
    $rss = $data[1]

    "$RUNTIME,$i,$ms,$mem,$rss" | Out-File $outfile -Append
}
