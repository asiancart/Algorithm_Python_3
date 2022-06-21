import sys

def sort(arrays):
    length = len(arrays)
    for i in range(0,length-1):
        insert_element=arrays[i]
        insert_position = i
        for j in range(insert_position-1,-1,-1):
            if insert_element < arrays[j]:
                arrays[j+1] = arrays[j]
                insert_position-=1
                arrays[insert_position] = insert_element


def main():
    scores=[80,70,60,50,95]
    sort(scores)
    for score in scores:
        print(score,",",end="")


if __name__ == "__main__":
    main()

