import sys

def reverse(arrays):
    length = len(arrays)
    middle = int(length/2)
    for i in range(0,middle):
        temp = arrays[i]
        arrays[i] = arrays[length-i-1]
        arrays[length-i-1] = temp

def main():
    scores = [50,90,70,80,60,100]
    reverse(scores)
    for score in scores:
        print(score,",",end="")

if __name__ == "__main__":
    main()