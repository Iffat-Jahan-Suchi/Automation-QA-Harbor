class movie:
    def __init__(self):
        self.title="Dham"
        self.genre="Action"
        self.rating=7.5
    def show_movie(self):
        print("movie showing....")
        print(f"title is {self.title},genre is {self.genre},Rating {self.rating} ")
    def movieRating(self,updateRating):
        self.rating=updateRating
        print(f"Your rating is {self.rating}")


myMovie=movie()

while True:
    print("1. show movie")
    print("2. Rating")
    print("3. Exit")

    option=int(input("select any option "))
    if option==1:
        myMovie.show_movie()
    elif option==2:
        updateRating=float(input("Are you enjoy it! enter your rating "))
        myMovie.movieRating(updateRating)
    elif option==3:
        print("stop program")
        break
    else:
        print("invalid option")



