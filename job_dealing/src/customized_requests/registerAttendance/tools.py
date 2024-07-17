

content = ""
for i in range(1, 1752):
    with open(f"~/Desktop/Space1/Files/temp.pptx{i}.txt", "r") as fi:
        content += fi.read()

with open("temp.txt", "w") as out:
    out.write(content)
