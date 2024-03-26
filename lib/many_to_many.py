class Book:
    _all_books = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book._all_books.append(self)

    @classmethod
    def all_books(cls):
        return cls._all_books

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Author:
    _all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author._all_authors.append(self)

    @classmethod
    def all_authors(cls):
        return cls._all_authors

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract) 
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)




class Contract:
    _all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract._all_contracts.append(self)

    @classmethod
    def all_contracts(cls):
        return cls._all_contracts

    @classmethod
    def contracts_by_date(cls, date):
        return sorted([contract for contract in cls._all_contracts if contract.date == date], key=lambda x: x.date)




book1 = Book("Book 1")
book2 = Book("Book 2")

author1 = Author("Author 1")
author2 = Author("Author 2")

contract1 = author1.sign_contract(book1, "2024-03-25", 10)
contract2 = author1.sign_contract(book2, "2024-03-26", 15)
contract3 = author2.sign_contract(book1, "2024-03-26", 12)

print("Contracts by Author 1:", [contract.book.title for contract in author1.contracts()])
print("Books by Author 1:", [book.title for book in author1.books()])
print("Total royalties for Author 1:", author1.total_royalties())

print("Contracts signed on 2024-03-26:", [contract.book.title for contract in Contract.contracts_by_date("2024-03-26")])
