# Project 3
I completed this assignment for my Cloud Computing Course at the University of Cincinnati. See below for the assignment instructions.

## Requirements
Do the following:
1. Start a docker container from any image of your choice.
2. Install python so that the code written in python can be executed.
3. Write a python script to read 2 text files (IF.txt & Limerick-1.txt) from location:
/home/data (inside your container)
4. Python script should be able to do following:
   1. List name of all the text file at location: /home/data.
   2. Read the two text files and count total number of words in each text files.
   3. Add all the number of words to find the grand total (total number of words in
both files).
   4. List the top 3 words with maximum number of counts in IF.txt. Include the word
counts for the top 3 words.
   5. Find the IP address of your machine.
   6. Write all the output to a text file at location: /home/output/result.txt (inside
your container).
   7. Upon running your container, it should do all the above stated steps and print
the information on console from result.txt file and exit.
5. Make your container image as small as possible.
6. Submit your image for evaluation.

## Running a Container
To build the image, I ran `docker build -t project3 .` from within this project directory. Then, to start a container from the image, I ran `docker run -v [path-on-my-computer]:/home/data project3`, where `[path-on-my-computer]` was replaced with the path to the directory containing the text files on my computer.

## Results
When I ran the container, I received the following output. It is added to home/output/result.txt within the container and is also printed to the console.
```
All text file names:
IF.txt
Limerick-1.txt
something.txt

Total words in IF.txt: 292
Total words in Limerick-1.txt: 32
Grand total: 324

Top 3 words in IF.txt:
'and' appears 19 times.
'you' appears 18 times.
'if' appears 14 times.

IP address of your machine: 172.17.0.2
```
