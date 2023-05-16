def slow_print(text):
    import time
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
slow_print