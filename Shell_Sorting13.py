import sys

def shell_sort(array,length):
    length = len(array)
    gap = int(length)//2
    while (gap>0):
        for i in range(gap,length):
            temp = array[i]
            j =i
            while j >= gap and array[j-gap] > temp:
                array[j] =array[j-gap]
                j = j-gap
            array[j] =temp
        gap= int(gap//2)



def main():
    scores = [9,6,5,8,0,7,4,3,1,2]
    length = len(scores)
    shell_sort(scores,length)
    for i in range(0,length):
        print(scores[i],",",end="")


if __name__ == "__main__":
    main()