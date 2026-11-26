# File Objects // File I/O:


# THIS BLOCK READS THE FILE:
file = open('Notes.txt', 'r')
print(file.name)
file.close()


# READS THE CONTENTS OF THE FILE:
with open('C:/Users/Md. Nahid Reza/Desktop/Modules/Notes.txt', 'r') as file:
    file_contents = file.read()
print(file_contents)

file_contents = file.readline()
print(file_contents, end='')

file_contents = file.readlines()
print(file_contents, end='')

for line in file:
    # >>>This for loop prints each elements (as line) at a time<<<
    print(line, end='')

size_to_read = 10

file_contents = file.read(size_to_read)
print(file_contents, end='*\n\n')
# This iterates throught the lines of the file every 10 characters and at the end of each iteration it puts an asterisk.
file_contents = file.read(size_to_read)
while len(file_contents) > 0:
    print(file_contents, end='*')
    file_contents = file.read(size_to_read)

with open('C:/Users/Md. Nahid Reza/Desktop/Modules/Notes.txt', 'r') as file:
    size_to_read = 10
    file_contents = file.read(size_to_read)
    print(file.tell())  # >>>Tells the current position that it read in the file<<<

file_contents = file.read(size_to_read)
print(file_contents, end='')
file.seek(0)
file_contents = file.read(size_to_read)
print(file_contents)


with open('Notes2.txt', 'w') as file:
    file.write('This is the 2nd Text File')
    file.write('\n2nd Line')
    file.seek(30)
    file.write('\n3rd Line')

with open('Notes.txt', 'r') as rf:
    with open('Notes_Copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('cat.jpg', 'rb') as rf:
    with open('cat_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

with open('cat.jpg', 'rb') as rf:
    with open('cat_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
