import psutil

def getCPUStats():
    cpu_stats = psutil.cpu_stats()
    return cpu_stats

if __name__ == "__main__":
    print(getCPUStats())