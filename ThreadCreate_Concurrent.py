import concurrent.futures

def ThreadFunction(ThreadIndex:int):
    print("Thread start")

    print(f"Thread number : {ThreadIndex}")

    return ThreadIndex

if __name__=="__main__":

    ThreadCount=10
    ThreadExec=concurrent.futures.ThreadPoolExecutor(ThreadCount)

    for Result in ThreadExec.map(ThreadFunction,range(ThreadCount)):
        print(f"{Result} Thread Done")

    print(f"Thread work has been done")