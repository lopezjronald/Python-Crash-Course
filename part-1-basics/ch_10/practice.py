def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, {filename} doesn't exist in your directory.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


books = ['alice.txt', 'die_mutter.txt', 'great_diamond.syndicate.txt', 'siddhartha.txt']

for book in books:
    count_words(book)