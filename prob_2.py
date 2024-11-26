def library_book_analysis():
    records = input("Enter borrowed books (format: 'Book Title - Days Borrowed', separated by commas): ")
    records_list = [record.strip() for record in records.split(",")]
    books_dict = {}
    for record in records_list:
        title, days = record.rsplit(" - ", 1)
        days = int(days)
        books_dict[title] = books_dict.get(title, 0) + days

    unique_titles = set(books_dict.keys())
    
    most_borrowed = max(books_dict.items(), key=lambda x: x[1])
    least_borrowed = min(books_dict.items(), key=lambda x: x[1])

    total_days = sum(books_dict.values())
    total_books = len(books_dict)
    average_days = total_days / total_books

    sorted_books = sorted(books_dict.items(), key=lambda x: x[1], reverse=True)

    print("")
    print(f"Most Borrowed Book: '{most_borrowed[0]}' with {most_borrowed[1]} days")
    print(f"Least Borrowed Book: '{least_borrowed[0]}' with {least_borrowed[1]} days")
    print(f"Average Borrowing Time: {average_days:.2f} days")
    print(f"Unique Book Titles: {unique_titles}")
    print(f"Books Sorted by Borrowing Duration:")
    for title, days in sorted_books:
        print(f"  {title}: {days} days")
library_book_analysis()
