#!/usr/bin/env python3
# Input and Output and Exceptions

3 data streams in Unix / Windows:
    STDIN (the standard input strea: default keyboard)
    STDOUT (standard output stream: default screen)
    STDERR (standard error output stream: default screen)

process: a running program
            - has a PID (process ID)
            - allocates memory with permissions of the OS
            - may writes to STDOUT and/or STDERR
            - may reads from STDIN
            - may read/write to files (the disk)
            - may make a network connection (over socket)

Definitions:
    ls -ltr (time order listing)
    ls > filename.ext (creates a new file)
    cat ()
    >> (appends to a file at the end)
    wc (word count)
    |   (whatever the STDOUT is move it into 'wc')

manipulating STDIN/STDOUT/STDERR/args to program
    === write STDOUT to a file with '>'===
        $ myprog > myfile.txt

    === append STDOUT to a file with '>>'===

    === pipe STDOUT to another program with '|' ===
        $ myprog | otherprog

    === read contents of a file to STDIN with '>' ===
        $ myprog < myfile.txt

Exceptions
    - different way to handle errors
    - form of flow control
    - 
