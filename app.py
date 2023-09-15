import psutil

def get_disk_usage(path):
    """Returns the disk usage of the given path in bytes."""
    disk_usage = psutil.disk_usage(path)
    return disk_usage.used

# Get the disk usage of the directory /var/lib/data.
disk_usage = get_disk_usage("/var/lib/data")

# Print the disk usage to the console.
print(f"Disk usage: {disk_usage}")

