
def read_file(filename):
    lines = []
    with open (filename, "r", encoding="utf-8-sig") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    t_count = 0
    b_count = 0
    t_s_count = 0
    b_s_count = 0
    for line in lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "Timothy":
            if s[3] == "貼圖":
                t_s_count += 1
            else:
                for m in s[3:]:
                    t_count += len(m)
        elif name == "ブン":
            if s[2] == "圖片":
                b_s_count += 1
            else:
                for m in s[2:]:
                    b_count += len(m)
    print("Timothy Huang說了" , t_count, "個字")
    print("ブン說了" , b_count, "個字")
    print("Timothy Huang傳了" , t_s_count, "個貼圖")
    print("ブン傳了", b_s_count, "個圖片")

def write_file(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + "\n")



def main():
    lines = read_file("[LINE]bun.txt")
    lines = convert(lines)
    # write_file("output.txt", lines)

main()