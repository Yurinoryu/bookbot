import stats
import sys




def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return


    # Get the file path
    path = sys.argv[1]
                
    # Read the file contents
    with open(path) as f:
        file_contents = f.read()
                                        
    # Get word count
    word_count = stats.word_count(file_contents)
                                                    
    # Get character count
    char_counts = stats.char_count(file_contents)
                                                                
    # Get sorted character list
    sorted_chars = stats.sort_letters(char_counts)
                                                                            
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
                                                                 
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    print("============= END ===============")



if __name__ == "__main__":
    main()
