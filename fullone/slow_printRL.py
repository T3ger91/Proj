#faster slow print
#in use by Ruleta.py were it prints whole table with nums
def slow_printRL(text):
    import time
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.00008)
