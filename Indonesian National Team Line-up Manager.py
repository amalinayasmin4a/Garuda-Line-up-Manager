from tabulate import tabulate

# Indonesian National Team Line-up Manager
# Capstone Project Module 1

squad = []    # all players in database
lineup = []   # starting 11
bench = []    # substitutes


def show_players(list_data):
    # display function to take a list of player dictionaries and shows them in a table
    
    if len(list_data) == 0:  # if the list is empty
        print("No players in this list.")
    else:  # else (if the list has players)
        headers = ["ID", "Jersey", "Name", "Position", "Club", "Age",
                   "Injury", "Minutes", "Notes"]
        table = [
            [p['id'], p['jersey'], p['name'], p['position'], p['club'],
             p['age'], p['injury'], p['minutes'], p['Notes']]
            for p in list_data
        ]
        print(tabulate(table, headers=headers, tablefmt="grid"))

#helper 
def find_player(pid):#--> used to search for a player in  squad list by their Player ID
    for p in squad:
        if p["id"] == pid:
            return p
    return None


def get_int_input(prompt): #--> to ensure that certain inputs are exclusively for integer only
    while True:
        val = input(prompt)
        if val.isdigit():
            return int(val)
        print("Please enter a number.")


def add_player(): #--> to add player 
    pid = input("Enter Player ID: ")
    if find_player(pid):
        print("Player ID already exists.")
        return
#input data area 
    jersey = get_int_input("Enter Jersey Number: ")
    name = input("Enter Name: ")
    position = input("Enter Position (GK/DF/MF/FW): ")
    club = input("Enter Club: ")
    age = get_int_input("Enter Age: ")
    minutes = get_int_input("Enter Minutes Played: ")
    injury = input("Injury Status (Yes/No): ")
    Notes = input("Enter Notes: ")

    player = {
        "id": pid,
        "jersey": jersey,
        "name": name,
        "position": position,
        "club": club,
        "age": age,
        "injury": injury,
        "minutes": minutes,
        "Notes": Notes
    }

    # Add to main database (squad)
    squad.append(player)
    print(f"\nPlayer {name} has been added to the Squad.")

    # Ask where to assign them
    print("\nAssign this player to: 1) Line-Up  2) Bench  3) Stay only in Squad")
    choice = input("Choose: ")
    if choice == "1":
        if len(lineup) >= 11: #--> criteria for a line up is 11 players max
            print("Line-Up is full (11 players). Adding to Bench instead.")
            bench.append(player)
        else:
            lineup.append(player)
            print(f"Player {name} added to Line-Up.")
    elif choice == "2":
        bench.append(player)
        print(f"Player {name} added to Bench.")
    else:
        print(f"Player {name} stays in Squad only for now.")

#to view all the appended players
def view_players():
    print("\n--- Squad (All Players) ---")
    show_players(squad)
    print("\n--- Line-Up (Starting 11) ---")
    show_players(lineup)
    print("\n--- Bench (Substitutes) ---")
    show_players(bench)

#to view the current players resided at the line up list
def view_lineup():
    print("\n===== Current Starting Line-Up =====")
    if len(lineup) == 0:
        print("No players in Line-Up yet.")
    else:
        print(f"Total Players: {len(lineup)}/11")
        show_players(lineup)


def update_player():
    pid = input("Enter Player ID to update: ")
    player = find_player(pid)
    if not player:
        print("Player not found.")
        return

    # --- Update fields ---
    name = input("New Name (leave blank if no change): ")
    club = input("New Club (leave blank if no change): ")
    injury = input("New Injury Status (leave blank if no change): ")
    Notes = input("New Notes (leave blank if no change): ")

    if name:
        player["name"] = name
    if club:
        player["club"] = club
    if injury:
        player["injury"] = injury
    if Notes:
        player["Notes"] = Notes

    print(f"Player {pid} info updated.")

    # --- Move player to a different list ---
    print("\nDo you want to move this player?")
    print("1) Stay where they are")
    print("2) Move to Line-Up")
    print("3) Move to Bench")
    print("4) Move to Squad only")

    move_choice = input("Choose: ")

    # First, remove them from wherever they are
    if player in lineup:
        lineup.remove(player)
    if player in bench:
        bench.remove(player)
    if player in squad:
        squad.remove(player)

    if move_choice == "1":
        # Figure out where they originally were and put them back
        squad.append(player)  # default if "stay" is chosen
    elif move_choice == "2":
        if len(lineup) >= 11:
            print("Line-Up is full (11 players). Adding back to Squad.")
            squad.append(player)
        else:
            lineup.append(player)
            print(f"Player {player['name']} moved to Line-Up.")
    elif move_choice == "3":
        bench.append(player)
        print(f"Player {player['name']} moved to Bench.")
    elif move_choice == "4":
        squad.append(player)
        print(f"Player {player['name']} moved to Squad.")
    else:
        # default fallback
        squad.append(player)

    print("Player update complete.")



def delete_player():
    pid = input("Enter Player ID to delete: ")
    player = find_player(pid)
    if not player:
        print("Player not found.")
        return

    # remove from all lists
    if player in squad:
        squad.remove(player)
    if player in lineup:
        lineup.remove(player)
    if player in bench:
        bench.remove(player)
    print(f"Player {pid} deleted from system.")


def menu():
    # Welcome message at start
    print("============================================")
    print("  Welcome Officials of Timnas Indonesia! 🇮🇩")
    print("============================================")

    while True:
        print("\n===== Indonesian National Team Line-up Manager =====")
        print("1. Add Player")
        print("2. View All Players")
        print("3. View Line-Up Only")
        print("4. Update Player")
        print("5. Delete Player")
        print("6. Exit")

        choice = input("Choose option: ")
        if choice == "1":
            add_player()
        elif choice == "2":
            view_players()
        elif choice == "3":
            view_lineup()
        elif choice == "4":
            update_player()
        elif choice == "5":
            delete_player()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

menu()
