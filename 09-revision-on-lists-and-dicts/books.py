# A library needs to keep track of their books. 
# Each book is represented by the ISBN,
# title, author(s), and a category.
# What data structure fits best?
# Write a program to load book data from a 
# CSV file and then give options to search by ISBN, 
# keyword in title, or category.

import csv 

file = open("books.csv")
reader = csv.DictReader(file)

books = {}
for row in reader:
    books[row['isbn']] = row

print(books)

