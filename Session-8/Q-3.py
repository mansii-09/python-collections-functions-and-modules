def book_movie_ticket(movie_name, seat_type ="Regular" , snacks = None):
    print("Movie: ", movie_name)
    print("Seat Type: ", seat_type)
    print("Snacks: ", snacks)
    print()

#positional argument
book_movie_ticket("Jawan", "VIP", "Popcorn")


#keyword argument
book_movie_ticket(
    movie_name="Pathaan",
    seat_type="Premium",
    snacks="Cold Drink"
)

#Mix of positinal and keyword arguments
book_movie_ticket("Jawan", snacks="Popcorn", seat_type="VIP")