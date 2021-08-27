# Task 4
# You have a text file. Add a line consisting of twelve asterisks (************) after the last line among the lines that have no comma. If there are no such lines in the file, the asterisks should be added after all lines of the existing file. Write the result to another file.

with open("task4.txt") as f1, open("task4a.txt", "w", encoding="utf-8") as f2:
    my_list1 = [line.rstrip("\n") for line in f1]
    my_list2 = []
    for i in my_list1:
        if i[-1] == ",":
            my_list2.append("************")
        my_list2.append(i)
    if my_list2[-1][-1] != ",":
        my_list2.append("************")
    for i in my_list2:
        f2.write(i + "\n")