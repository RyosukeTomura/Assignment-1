#file open
file = open("movies.csv", "r")
movies = []

count = 0
for line in file.readlines():
    line = line.strip()
    movies.append(line.split(","))
    count = count + 1
print("Movies To Watch 1.0 by- Ryosuke Tomura")
print(count,"movies loaded")
file.close()
#Display Menu
while True:
    print("Menu:")
    print("L - List movies")
    print("A - Add new movie")
    print("W - Watch  movie")
    print("Q - Quit")
    choice = input(">>>")
    choice = choice.lower()
#L - List movies
    if choice == "l":
        remain = 0
        watched = 0
        for i, movie in enumerate(movies):
            title = movie[0]
            year = movie[1]
            category = movie[2]
            print(str(i)+"." + "  " + title + "    " + "-" + year + " " + "(" + category + ")")
            if movie[-1] == "w":
                watched = watched + 1
            else:# "w"
                remain = remain + 1
        print(watched, "movies watched,", remain, "movies still to watch")
#A - Add new movie
    elif choice == "a":
        title = ""
        while True:
            title = input("Title:")
            if title != "":
                break
            print("Input can not be blank")
        old = ""
        while True:
            old = input("Year:")
            try:
                old = int(old)
            except:
                print("Invalid input; enter a valid number")
                continue
            if old < 0:
                print("Number must be >=0")
            else:
                break
        category = ""
        while True:
            category = input("Category:")
            if category != "":
                break
            print("Input can not be blank")
        new_movie = ["*", title, old, "(", category, ")"]
        for movie in movies:
            print(title, "(", category, "from", old, ")added to movie list")
#W - Watch a movie
    elif choice == "w":
        remain = 0
        for movie in movies:
            if movie[-1] == "u":
                remain = remain + 1
        if remain == 0:
            print("No more movies to watch!")
            continue
        print("Enter the number of a movie to mark as watched")
        while True:
            number = input(">>>")
            try:
                number = int(number)
            except:
                print("Invalid input; enter a valid number")
                continue
            if number < 0:
                print("Number must be >= 0")
            elif number > len(movies):
                print("Invalid movie number")
            elif movie[-1] == "w":
                print("you have already watched", movie[0])
            else:
                print(movie[0], "from", movie[1], "watched")
                movies[-1] = ""
                break
#Q - Quit
    elif choice == "q":
        for movie in movies:
            print(len(movies), "movies saved to movies.csv")
            print("Have a nice day:)")
            break
    else:
        print("Invalid menu choice")


























