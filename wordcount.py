def count_words(filename):
    try:
        with open("wordsin.txt", "r") as file:
            content = file.read()
            words = content.split()
            print("File Contents:\n")
            print(content)
            print("\nTotal Words:", len(words))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)


count_words("wordsin.txt")
