from time import perf_counter

def execution_time(fn):
    def wrapper(*args, **kwargs):
        before = perf_counter()
        result = fn(*args, **kwargs)
        after = perf_counter() - before
        print(f"""\nExecution Time\nSeconds: {after}\nMinutes: {after / 60}\n""")
        #return (result, after)
        return result
    return wrapper