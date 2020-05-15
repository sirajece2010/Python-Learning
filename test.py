import re
with open("file.txt", 'r') as fh:
    data = fh.readline()

data = re.sub(r"bytes", 'strings', data)

with open("new_file.txt", 'w+') as f:
    f.write(data)