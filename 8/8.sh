#!/bin/sh

before=`wc -c < input`
after=`sed -re 's/^"//; s/"$//; s/\\\"/Q/g; s/\\\{2}/B/g; s/\\\x[0123456789abcdef]{2}/X/g'< input | tee output | wc -c`
# the backslsh escaping here with shell and sed combo is pretty bad, did a workaround to get it right after guessing wrong...
after2=`sed -re 's/^"/QQQ/; s/"$/QQQ/; s/\\\x[0123456789abcdef]{2}/XXXXX/g; s/\\\/BBB/g; s/BBBBBB/BBBB/g'< input | tee output2 | wc -c`
echo $[$before - $after]
echo $[$after2 - $before]
