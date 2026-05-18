#!/bin/bash

echo "Enter filename:"
read file

sha256sum "$file" > hash.txt

echo "Hash stored in hash.txt"
echo "Checking integrity..."

sha256sum -c hash.txt
