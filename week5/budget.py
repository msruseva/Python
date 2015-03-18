def on_budget(books, budget):
    books = sorted(books)
    result = {
        "books_on_budget": 0,
        "loan": 0
        }
    
    for book in books:
        if budget >= book:
            result["books_on_budget"] += 1
            budget -= book
        else:
            result["loan"] += book - budget
            budget = 0
            
    return result
