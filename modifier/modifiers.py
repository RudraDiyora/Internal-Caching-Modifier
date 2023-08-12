import time
import json

global JSON_FILE 
JSON_FILE = "file.JSON"

def timed(inner_func):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        result = inner_func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Time: {duration:.9f} secs")
        return result
    return wrapped_func
def internal_cache(inner_func):
    class CALLS:
        calls = {"":""}
    def wrapped_func(*args, **kwargs):
        arguments = str(args)
        if not(arguments in CALLS.calls):
            CALLS.calls[arguments] = inner_func(*args, **kwargs)
        return CALLS.calls[arguments]
      #  with open(str(JSON_FILE),'r') as file:
      #      database = json.load(file)
      #  if not(arguments in database):
            #database[arguments] = inner_func(*args, **kwargs)
          #  DONOT USE: database.append({f"{arguments}":inner_func(*args, **kwargs)})
            #with open("file.JSON", "w") as file:
               # json.dump(database, file, indent=4)
      #  return database[arguments]    
    return wrapped_func