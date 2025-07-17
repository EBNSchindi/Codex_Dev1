import time


def main():
    print("Press Ctrl+C to stop the stopwatch.")
    start_time = time.time()
    try:
        while True:
            elapsed = time.time() - start_time
            print(f"\rElapsed time: {elapsed:.2f} seconds", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\nStopped at {time.time() - start_time:.2f} seconds.")


if __name__ == "__main__":
    main()

