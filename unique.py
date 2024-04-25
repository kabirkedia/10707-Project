def count_unique_words(file_path):
    unique_words = set()

    with open(file_path, 'r') as file:
        for line in file:
            line = line.replace("'", "").replace("-", "")
            words = line.split()
            unique_words.update(words)

    return len(unique_words)

# Example usage
file_path = 'ghazals.txt'
num_unique_words = count_unique_words(file_path)
print("Number of unique words:", num_unique_words)
