def merge_sort(unsortedList):
    if len(unsortedList) > 1:
        mid = len(unsortedList) // 2
        leftList = unsortedList[:mid]
        rightList = unsortedList[mid:]

        # Recursive call when we go two list (left and right) for sorting
        merge_sort(leftList)
        merge_sort(rightList)

        # Because we have two lists, so we need to iterators for iteration of each list
        m = 0
        n = 0
        # We need one common iterator which iterates to the main list
        z = 0

        while m < len(leftList) and n < len(rightList):
            if leftList[m] <= rightList[n]:
                # Here we are using the first left side elements
                unsortedList[z] = leftList[m]
                # Increment the main iterator
                m += 1
            else:
                unsortedList[z] = rightList[n]
                n += 1
            z += 1

        # If values are left in the list, then we process here
        while m < len(leftList):
            unsortedList[z] = leftList[m]
            m += 1
            z += 1

        while n < len(rightList):
            unsortedList[z] = rightList[n]
            n += 1
            z += 1


unsortedList1 = [23, 56, 0, 23, 85, 100, 200, 12, 32, 78, 90, 102]
merge_sort(unsortedList1)
print(unsortedList1)