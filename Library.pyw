import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 
import customtkinter as CTK 
class Library:
    def __init__(self, root):
        self.all_books = ["To Kill a Mockingbird", "Pride and Prejudice", "Harry Potter", "The Alchemist", "Demon Slayer", "Game of Thrones", "End Game"]
        self.available_books = self.all_books.copy()
        self.borrowed_books = []
        self.returned_books = []
        self.root = root
        self.setup_ui()
        self.book_summaries = {
            "To Kill a Mockingbird": "A classic novel by Harper Lee. that explores themes of racism, morality, and innocence. Set in the American South during the 1930s, it follows the story of young Scout Finch and her brother Jem as they witness their father, Atticus Finch, defend a black man falsely accused of raping a white woman. The novel sheds light on the deep-seated prejudices and injustices of the time.",
            "Pride and Prejudice": "Jane Austen's famous novel.'Pride and Prejudice' is a timeless novel that revolves around the romantic pursuits of the strong-willed Elizabeth Bennet and the proud Mr. Darcy. Set in the early 19th century, it is a story of love, class, and societal expectations, with Austen's keen social commentary and sharp wit.",
            "Harry Potter": "'Harry Potter' is a popular fantasy book series written by J.K. Rowling. The series follows the adventures of a young wizard, Harry Potter, as he discovers his magical abilities and attends Hogwarts School of Witchcraft and Wizardry. Throughout the series, Harry and his friends, Ron and Hermione, encounter various challenges and adversaries, including the dark wizard Voldemort, who seeks to conquer the wizarding world. The story explores themes of friendship, courage, and the battle between good and evil in a magical and captivating world.",
            "The Alchemist":"A philosophical novel written by Paulo Coelho that follows the journey of Santiago, a shepherd boy, as he embarks on a quest to find his personal legend and fulfill his dreams. Along the way, he learns about the importance of following one's heart and the pursuit of destiny.",
            "Demon Slayer":"'Demon Slayer' follows the adventures of Tanjiro Kamado, a young boy who becomes a demon slayer after his family is slaughtered by demons, and his sister turned into one. He seeks to avenge his family and find a cure for his sister while battling formidable demons.",
            "End Game":"David Baldacci's (A Will Robie series)'End Game' is a thriller novel in the Will Robie series, featuring a government assassin who uncovers dark secrets while trying to protect his home town. The book is full of suspense, action, and intrigue.",
            "Game of Thrones":"'Game of Thrones' by George R.R. Martin is the first book in the epic fantasy series. It is a tale of political intrigue, power struggles, and complex characters set in a medieval-like world. The story follows various noble families as they vie for control of the Iron Throne."
        }
    def setup_ui(self):
        self.root.title("Library Management System")

        # Load the background image using Pillow
        bg_image = Image.open("Library.jpeg").resize((600, 500))
        bg_image = ImageTk.PhotoImage(bg_image)

        # Set the transparency of the root window
        self.root.attributes("-transparentcolor", "white")

        # Create a canvas to display the background image
        canvas = CTK.CTkCanvas(self.root, width=700, height=600)
        canvas.pack(fill="both",ipadx=500,ipady=450)

        # Display the background image
        canvas.create_image(0,0, anchor=CTK.NW, image=bg_image)

        # Create custom buttons with transparent background
        CTK.CTkLabel(canvas, text='Library Management System',width=360 ,height=40,font=("New times Roman", 25), corner_radius=0 , text_color="lavender",fg_color="black").pack(pady=15)
        CTK.CTkButton(canvas, text="View All Books", command=self.Display_books, width=110, corner_radius=0,text_color="lavender",fg_color="black",bg_color="transparent").pack(pady=15)
        CTK.CTkButton(canvas, text="Available Books", command=self.Available_books,corner_radius=0, width=110,text_color="lavender",fg_color="black").pack(pady=15)
        CTK.CTkButton(canvas, text="Read Books", command=self.Read_books,  corner_radius=0, width=110,text_color="lavender",fg_color="black").pack(pady=15)
        CTK.CTkButton(canvas, text="Borrow a Book", command=self.Borrow_books,  corner_radius=0, width=110,text_color="lavender",fg_color="black").pack(pady=15)
        CTK.CTkButton(canvas, text="Return a Book", command=self.Return_books,  corner_radius=0, width=110,text_color="lavender",fg_color="black").pack(pady=15)
        CTK.CTkButton(canvas, text="Exit", command=self.root.quit, corner_radius=0, width=90,text_color="lavender",fg_color="black").pack(pady=15)

        canvas.bg_image=bg_image
    def Display_books(self):
        if self.all_books:
            book_list = "\n".join(f"{i + 1}: {book}" for i, book in enumerate(self.all_books))
            messagebox.showinfo("All books",book_list)


    def Available_books(self):
        if self.available_books:
            book_list = "\n".join(f"{i + 1}: {book}" for i, book in enumerate(self.available_books))
            messagebox.showinfo("Available books", book_list)
            choice = messagebox.askquestion("Question", "Want to borrow a book?")
            if choice == "yes":
                self.Borrow_books()
        else:
            messagebox.showinfo("All books have been issued", "Please wait until they are returned")

    def Read_books(self):
        if self.borrowed_books:
            book_list = "\n".join(f"{i + 1}: {book}" for i, book in enumerate(self.borrowed_books))
            returned_book_no = simpledialog.askinteger("Borrowed books", f"Enter the book number you want to read:\n{book_list}")
            if returned_book_no is not None and 1 <= returned_book_no <= len(self.borrowed_books):
                returned_book = self.borrowed_books[returned_book_no - 1]
                book_summary = self.book_summaries.get(returned_book, "No summary available.")
                messagebox.showinfo("Book Summary", f"Summary of '{returned_book}':\n{book_summary}")
            else:
                messagebox.showinfo("Invalid input", "Please enter a valid book number.")
        else:
            messagebox.showinfo("No borrowed books", "You have no borrowed books to read. Want to borrow one?")
            self.Borrow_books()

    def Borrow_books(self):
        if self.available_books:
            book_list = "\n".join(f"{i + 1}: {book}" for i, book in enumerate(self.available_books))
            book_number = simpledialog.askinteger("Library books", f"Enter the book number you want to borrow:\n{book_list}")
            if book_number is not None and 1 <= book_number <= len(self.available_books):
                book = self.available_books.pop(book_number - 1)
                self.borrowed_books.append(book)
                messagebox.showinfo("Book Borrowed", f"Book #{book_number}: {book} has been issued to you. Please keep it safe and return it on time.")
            else:
                messagebox.showinfo("Invalid input", "Please enter a valid book number.")
        else:
            choice = messagebox.askquestion("Sorry", "All books have been borrowed. Maybe you are looking to return.")
            if choice == "yes":
                self.Return_books()

    def Return_books(self):
        if self.borrowed_books:
            book_list = "\n".join(f"{i + 1}: {book}" for i, book in enumerate(self.borrowed_books))
            returned_book_no = simpledialog.askinteger("Borrowed books", f"Enter the book number you want to return:\n{book_list}")
            if returned_book_no is not None and 1 <= returned_book_no <= len(self.borrowed_books):
                returned_book = self.borrowed_books.pop(returned_book_no - 1)
                self.returned_books.append(returned_book)
                self.available_books.append(returned_book)
                messagebox.showinfo("Thanks", f"You have returned Book #{returned_book_no}: {returned_book}. Thank you for returning it on time.")
            else:
                messagebox.showinfo("Invalid input", "Please enter a valid book number.")
        else:
           
            choice = messagebox.askquestion("No borrowed books", "You have no borrowed books to return. Want to borrow one?")
            if choice.lower()=="yes":
                self.Return_books()
                
                
def main():
    root = tk.Tk()
    app = Library(root) 
    CTK.set_default_color_theme("dark-blue")
    root.geometry("500x450")
    root.resizable(width=False,height=False)
    root.mainloop()
if __name__ == "__main__":
    main()