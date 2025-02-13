#!/bin/bash

boilerplatepy="def main():


if __name__ == \"__main__\":
    main()"

if [ "$#" -lt 1 ]; then
    echo "usage: "$0" problem_name"
    exit
fi

dir=$(echo "$*" | tr -s '. ' '_' | tr "[:upper:]" "[:lower:]")

if [ -d "$dir" ]; then
    echo "Directory $dir already exists."
else
    mkdir "$dir"
    cd "$dir"
    echo "$boilerplatepy" > "solve.py"
fi