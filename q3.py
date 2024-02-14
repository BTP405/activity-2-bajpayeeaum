def wordCount(t):
    word_dict = {}

    # Open the text file in read mode
    with open(t, 'r') as file:
        # Read each line in the file
        for line_num, line in enumerate(file, start=1):
            # Split the line into words
            words = line.split()
            # Iterate through each word in the line
            for word in words:
                # Remove punctuation and convert to lowercase
                word = word.strip('.,!?;:').lower()
                # Check if the word is already in the dictionary
                if word in word_dict:
                    # Append the line number to the list of line numbers for the word
                    word_dict[word].append(line_num)
                else:
                    # Create a new list with the line number for the word
                    word_dict[word] = [line_num]

    return word_dict


# Test the function
if __name__ == "__main__":
    filename = input("Enter the filename: ")
    result = wordCount(filename)
    print("Word count result:")
    for key, value in result.items():
        print(f"{key}: {value}")
