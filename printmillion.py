import itertools as it


def print_million():
    """Print numbers from 0 to 10^6 using itertools"""
    a = it.starmap((lambda x,y: 1000*x+y), it.product(range(0,1000,1), range(1,1001,1)))
    while True:
        try:
            print(next(a))
        except:
            print("Done.")
            break
    
    
if __name__ == "__main__":
    print_million()

