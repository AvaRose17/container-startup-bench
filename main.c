#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MEM_MB 64
#define CPU_ITERS 100000000

long get_rss_kb() {
    FILE *f = fopen("/proc/self/statm", "r");
    if (!f) return -1;

    long pages;
    fscanf(f, "%*s %ld", &pages);
    fclose(f);

    return pages * sysconf(_SC_PAGESIZE) / 1024;
}

int main() {
    // Marker for startup timing
    printf("READY\n");
    fflush(stdout);

    // Allocate memory
    size_t bytes = MEM_MB * 1024 * 1024;
    char *buf = malloc(bytes);
    if (!buf) return 1;

    for (size_t i = 0; i < bytes; i += 4096)
        buf[i] = 1;

    // CPU loop
    volatile long x = 0;
    for (long i = 0; i < CPU_ITERS; i++)
        x += i;

    // Measure RSS
    long rss_kb = get_rss_kb();

    // Output CSV row
    printf("%d,%ld\n", MEM_MB, rss_kb);

    return 0;
}

