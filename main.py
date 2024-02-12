import os, socket
from collections import Counter

# Writes the provided results to result.txt
def write_to_results(results):
    # Create the path if it doesn't exist
    if (not os.path.exists("/home/output")): os.mkdir("/home/output")

    # Write the results to the file
    file = open("/home/output/result.txt", "a+")
    for line in results:
        file.write(line + "\n")

    # Add space between this result and the next
    file.write("\n")

    file.close()

# Writes the text file names to result.txt
def list_file_names():
    # Get all the text files in /home/data
    all_files = [file for file in os.listdir("/home/data/") if file.endswith(".txt")]

    # Add a heading for the output
    all_files.insert(0, "All text file names:")

    # Write the heading and file names to the result file
    write_to_results(all_files)

# Returns the word lowercased and only including letters
def format_word(word):
    word = word.lower()
    word = ''.join([letter for letter in word if letter.isalpha()])
    return word

# Returns the words in the provided file
def get_words(file_name):
    file = open(f"/home/data/{file_name}", "r")

    # Get the words from the file content
    words = file.read().split()
    file.close()

    # Remove special characters and split words connected by —
    formatted_words = []
    for word in words:
        split_words = word.split("—")
        for split_word in split_words:
            formatted_words.append(format_word(split_word))

    return formatted_words

# Writes the top 3 words in IF.txt to result.txt
def get_top_3_words(words):
    # Get the 3 most common words
    top_3 = Counter(words).most_common(3)

    # Add to the results
    results = ["Top 3 words in IF.txt:"]
    for top in top_3:
        results.append(f"'{top[0]}' appears {top[1]} times.")
    
    write_to_results(results)

if __name__ == "__main__":
    # List all text files within /home/data
    list_file_names()

    # Get the words from IF.txt and Limerick-1.txt
    if_words = get_words("IF.txt")
    limerick_words = get_words("Limerick-1.txt")

    # Write the individual and grand total word counts
    write_to_results([f"Total words in IF.txt: {len(if_words)}",
                      f"Total words in Limerick-1.txt: {len(limerick_words)}",
                      f"Grand total: {len(if_words) + len(limerick_words)}"])

    # Write the top 3 words and their counts in IF.txt
    get_top_3_words(if_words)

    # Write the IP address of the machine
    write_to_results([f"IP address of your machine: {socket.gethostbyname(socket.gethostname())}"])

    # Write the contents of result.txt to the console
    print(open("/home/output/result.txt", "r").read())
