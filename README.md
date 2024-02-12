# Project 3
I completed this assignment for my Cloud Computing Course at the University of Cincinnati. See below for the assignment instructions.

## Requirements
Do the following (Python is mentioned but you can use any language of your choice to
complete the task):
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
