from mergeSort import merge_sort
from medirMerge import medir_busqueda, medir_merge_sort

arr = [5, 2, 4, 7, 1]
merge_sort(arr, 0, len(arr)-1)
print(arr)  
medir_merge_sort(arr)
medir_busqueda(arr, 4)

