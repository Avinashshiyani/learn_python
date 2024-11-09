# Create a dictionary of book titles and authors
books = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "Pride and Prejudice": "Jane Austen"
}

# Print all book titles
print("Book Titles:")
for title in books.keys():
    print(title)

# Print all authors
print("\nAuthors:")
for author in books.values():
    print(author)

# Add a new book-title/author pair to the dictionary
new_title = input("\nEnter a new book title: ")
new_author = input("Enter the author of the book: ")
books[new_title] = new_author
print(f"Added: {new_title} by {new_author}")

# Accept 
remove_title = input("\nEnter the title of the book you want to remove: ")

if remove_title in books:
    del books[remove_title]
    print(f"Removed: {remove_title}")
else:
    print(f"Book titled '{remove_title}' not found in the dictionary.")

# Print updated 
print("\nUpdated Book Titles:")
for title in books.keys():
    print(title)

print("\nUpdated Authors:")
for author in books.values():
    print(author)
