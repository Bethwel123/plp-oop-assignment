class Book:
    def __init__(self, title, author, genre, page_count, current_page=0, is_read=False):
        self.title = title
        self.author = author
        self.genre = genre
        self.page_count = page_count
        self.current_page = current_page
        self.is_read = is_read
    
    def read(self, pages):
        if self.is_read:
            print(f"You've already finished {self.title}!")
            return
        
        self.current_page += pages
        if self.current_page >= self.page_count:
            self.current_page = self.page_count
            self.is_read = True
            print(f"Congratulations! You've finished reading {self.title}!")
        else:
            print(f"You've read {pages} pages. Now on page {self.current_page}/{self.page_count}")
    
    def bookmark(self, page):
        if page > self.page_count:
            print(f"Page {page} doesn't exist in this book!")
        else:
            self.current_page = page
            print(f"Bookmarked page {page}")
    
    def get_status(self):
        if self.is_read:
            return f"Completed: {self.title} by {self.author}"
        else:
            return f"Reading: {self.title} ({self.current_page}/{self.page_count})"
    
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.genre}, {self.page_count} pages)"


# Inheritance example: Textbook class that inherits from Book
class Textbook(Book):
    def __init__(self, title, author, subject, page_count, edition, current_page=0, is_read=False):
        super().__init__(title, author, "Textbook", page_count, current_page, is_read)
        self.subject = subject
        self.edition = edition
    
    def do_homework(self, chapter):
        print(f"Working on {self.subject} homework from chapter {chapter}...")
    
    def __str__(self):
        return f"'{self.title}' ({self.subject} {self.edition} edition) by {self.author}"


# Demonstration
if __name__ == "__main__":
    print("=== Book Class Demo ===")
    novel = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 180)
    print(novel)
    novel.read(30)
    novel.read(50)
    novel.bookmark(100)
    novel.read(100)
    print(novel.get_status())
    
    print("\n=== Textbook Inheritance Demo ===")
    math_book = Textbook("Calculus", "James Stewart", "Mathematics", 1200, "8th")
    print(math_book)
    math_book.do_homework(5)
    math_book.read(50)
    print(math_book.get_status())