Array = [99,21,19,22,28,11,14,18]

def merge(left, right, Array):
  i = 0
  j = 0
  k = 0

  while (i<len(left) and j<len(right)):
    if(left[i]<right[j]):
      Array[k] = left[i]
      i = i+1
    else:
      Array[k] = right[j]
      j = j+1

    k = k+1

  while(i<len(left)):
    Array[k] = left[i]
    i = i+1
    k = k+1

  while(j<len(right)):
    Array[k] = right[j]
    j = j+1
    k = k+1

def mergesort(Array):
  n = len(Array)
  if(n<2):
    return

  mid = n/2
  left = []
  right = []


  for i in range(int(round(mid))):
    number = Array[i]
    left.append(number)

  for i in range(int(round(mid)),int((round(n)))):
    number = Array[i]
    right.append(number)

  mergesort(left)
  mergesort(right)

  merge(left,right,Array)

#calling mergesort
mergesort(Array)
print(Array)
