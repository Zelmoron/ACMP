n = int(input())

bus_height = 437

data = [int(i) for i in input().split()]




def main():
    for i in  range(len(data)):
        if data[i] >bus_height:
            continue
        else:
            print(f"Crash {i+1}")
            return
    print("No crash")

main()