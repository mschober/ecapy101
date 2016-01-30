#!/bin/bash

curr_koans=${1:-$(ls python_koans-*)}
echo "Current koans is: " $curr_koans

zip -r python_koans.zip python_koans

next_koans="python_koans-$(md5 python_koans.zip | awk -F " = " '{ print $2 }' | cut -c 1-8)".zip
echo "Next koans is: " $next_koans

echo "Moving current to next"
mv $curr_koans $next_koans

echo "Replacing current with next in wiki"
sed -i -e "s/$curr_koans/$next_koans/" ../ecapy101.wiki/setup_python_koans.rest

echo "Verifying grep"
grep -q $next_koans ../ecapy101.wiki/setup_python_koans.rest || echo "failed"

echo "Removing new zip temp file"
rm python_koans.zip

