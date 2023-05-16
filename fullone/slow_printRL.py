def slow_printRL(text):
    import time
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.001)