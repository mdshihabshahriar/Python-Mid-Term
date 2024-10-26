class Start_cinema:
    _hall_list = []
    
    def entry_hall(self, hall):
        self._hall_list.append(hall)
        
class Hall(Start_cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)
        
    def entry_show(self, id, movie_name, time):
        showInfo = (id, movie_name, time)
        self.__show_list.append(showInfo)
        seat_matrix = []
        for _ in range(self.rows):
            row = [0] * self.cols 
            seat_matrix.append(row)
        self.__seats[id] = seat_matrix
    
    def available_seats(self, id):
        flag = False
        for show in self.__show_list:
            if show[0] == id:
                flag = True
                print(f"\n<------- Available seats for show -> {id} ------->")
                for row in self.__seats[id]:
                    for seat in row:
                        if seat == 0:
                            print("0", end=" ")
                        else:
                            print("1", end=" ")
                    print()
                break
        if not flag:
            print("Show ID not found.")
                
    def book_seats(self, id, seat_list):
        flag = False
        for show in self.__show_list:
            if show[0] == id:
                flag = True
                for row, col in seat_list:
                    if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                        print(f"Invalid seat [{row}, {col}].")
                    elif self.__seats[id][row][col] == 0:
                        self.__seats[id][row][col] = 1
                        print(f"Seat [{row}, {col}] booked successfully.")
                    else:
                        print(f"Seat [{row}, {col}] is already booked.")
                break
            
        if not flag:
            print("Show ID not found.")
    
    def view_show_list(self):
        print(f"<-------- Show list for Hall :{self.hall_no} --------->")
        for show in self.__show_list:
            print(f"\n SHOW ID: {show[0]}, MOVIE NAME: {show[1]}, TIME: {show[2]}")
            print()

hall = None

while True:
    print("""
            <---------- Movie Booking System ----------->
                1. Add Show Information
                2. View all shows today
                3. View available seats for a show
                4. Book seat for a show
                5. Exit
            """)
    
    choice = input("Choose Option: ")
    
    if choice == "1":
        showId = input("Enter show id: ")
        mv_name = input("Enter movie name: ")
        time = input("Enter the show time: ")
        row_col_input = input("Enter Row And Col (format: row col): ").split()
        row = int(row_col_input[0])
        col = int(row_col_input[1])
        hall_no = int(input("Enter hall no: "))
        
        hall = Hall(row, col, hall_no)
        hall.entry_show(showId, mv_name, time)
        print("\nInformation added successfully!!!\n")
    
    elif choice == "2":
        print("\n<-------- View show information --------->\n")
        for show in Start_cinema._hall_list:
            show.view_show_list()
            
    elif choice == "3":
        print("\n<-------- View available seats -------->")
        show_id = input("Enter the show id: ")
        if hall:  
            hall.available_seats(show_id)
        else:
            print("No hall information available. Please add a show first.")
        
    elif choice == "4":
        print("\n<------- Book seat for a movie ------->")
        show_id = input("Enter the id of the show: ")
        seat = int(input("Enter the number of seats: "))
        seatBook = []
        for _ in range(seat):
            row = int(input("Enter the row of the seat: "))
            col = int(input("Enter the column of the seat: "))
            seatBook.append((row, col))
        if hall:  
            hall.book_seats(show_id, seatBook)
        else:
            print("No hall information available. Please add a show first.")
    
    elif choice == "5":
        print("Exiting the system. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
