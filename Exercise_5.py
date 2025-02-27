# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):

  #write your code here
  pivot = arr[h]
  i = l - 1
  for j in range(l, h):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[h]) = (arr[h], arr[i + 1])
  return i + 1

def quickSortIterative(arr, l, h):

  #write your code here
  n = h - l + 1
  stack = [0] * (n)
  top = -1
  top += 1
  stack[top] = l
  top += 1
  stack[top] = h
 
  while top >= 0:
    h = stack[top]
    top = top - 1
    l = stack[top]
    top = top - 1
 
    pivot = partition( arr, l, h )

    if pivot-1 > l:
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = pivot - 1

    if pivot+1 < h:
      top = top + 1
      stack[top] = pivot + 1
      top = top + 1
      stack[top] = h




arr = [22, 12, 89, 34, 9, 0, 15, 45, 54]
size = len(arr)
print("Original Array:")
for i in range(size):
  print(arr[i])
quickSortIterative(arr, 0, size-1)
print("Sorted Array:")
for i in range(size):
  print ( arr[i])