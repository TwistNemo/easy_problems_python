def bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(len(seq)-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
my_list = [1, 2, 10, 5, 7, 20]
print(my_list)
bubble_sort(my_list)
print(my_list)