from pync import Notifier
import time

if __name__ == "__main__":
    while True:
        Notifier.notify(
            title="Rest App",
            message="Take some rest. Rest is essential for life and detox of the mind.",
            timeout=10
        )
        time.sleep(60*60)
