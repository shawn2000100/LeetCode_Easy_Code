# Read from the file file.txt and output the tenth line to stdout.
# �k�@
awk 'NR==10' file.txt
# �k�G
# sed -n '10p' file.txt