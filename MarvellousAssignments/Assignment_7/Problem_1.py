

class BookStore:
    no_Of_Books = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.no_Of_Books +=1

    def diplay(self):
        print(self.Name , end=' ')
        print("By ", self.Author)
        print("No Of Books In Store: ",self.no_Of_Books)


obj = BookStore("Python","Robert")
obj.diplay()

obj1 = BookStore("C Programming","Dennis Ritchie")
obj1.diplay()