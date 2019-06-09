# Read from the file file.txt and output the tenth line to stdout.
# 法一
awk 'NR==10' file.txt
# 法二
# sed -n '10p' file.txt