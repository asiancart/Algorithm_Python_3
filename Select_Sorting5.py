import sys

def sort(arrays):
    length = len(arrays)-1
    min_index = 0

    for i in range(0,length):
        min_index =i
        min_value = arrays[min_index]
        for j in range(i,length):
            if min_value > arrays[j+1]:
                min_value = arrays[j+1]
                min_index = j+1
                if i != min_index:
                    temp= arrays[i]
                    arrays[i] = arrays[min_index]
                    arrays[min_index] = temp

def main():
    scores = [60,80,95,50,70]
    sort(scores)
    for score in scores:
        print(score,",",end="")

if __name__ == "__main__":
    main()