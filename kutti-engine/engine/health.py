import psutil


class HealthMonitor:
    """
    Collects system health information.
    """

    def get_cpu(self):
        return psutil.cpu_percent(interval=0.5)

    def get_memory(self):
        return psutil.virtual_memory().percent

    def get_disk(self):
        return psutil.disk_usage("/").percent

    def get_summary(self):
        return {
            "cpu": self.get_cpu(),
            "memory": self.get_memory(),
            "disk": self.get_disk(),
        }