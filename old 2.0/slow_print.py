#slow printing func
#making gag staff with text, start looking like starwars opening 
def slow_print(text):
    import time
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
slow_print
