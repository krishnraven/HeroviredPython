import psutil
import time

THRESHOLD = 80  # Set CPU usage threshold

def monitor_cpu():
    print("Monitoring CPU usage...\nPress Ctrl+C to stop.")
    try:
        while True:
            usage = psutil.cpu_percent(interval=1)
            if usage > THRESHOLD:
                print(f"⚠️  Alert! CPU usage exceeds threshold: {usage}%")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu()

