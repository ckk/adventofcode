# generic shell one-liner I used for part 1:
while read l; do egrep "${l}(,|$)" input-sues; done < input-analysis |sed -e 's/:.*//' | sort | uniq -c | sort -n | tail -1
