# File to variable

file2var is made with python3. It has no dependency other than python 3.2
or higher.

## For example

Generate c files, Convert text files to cstring or binary files to c
`unsigned char[]`.

```
Example usage

$ ./file2var txt2cstr -p c -o ../src/programs *.glsl

output files are programs.h and programs.c

```


```
Javascript Example usage

$ ./file2var txt2cstr -p js -o ../src/programs.js *.glsl

output file is js file containing all .glsl files named with their filename

```
