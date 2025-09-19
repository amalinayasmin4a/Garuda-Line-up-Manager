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


# helper
def find_player(pid):  # search by player ID
    for p in squad + lineup + bench:  # search across all lists
        if p["id"] == pid:
            return p
    return None


def get_int_input(prompt):  # ensure integer input only
    while True:
        val = input(prompt)
        if val.isdigit():
            return int(val)
        print("Please enter a number.")


def add_player():  # add player
    pid = input("Enter Player ID: ")
    if find_player(pid):
        print("Player ID already exists.")
        return

    # input data
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
        if len(lineup) >= 11:  # max 11 in line-up
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
#Sort Player Sub Menu
def sort_players(list_data):
    if len(list_data) == 0:
        return list_data

    print("\nSort by: 1) Position  2) Minutes Played  3) No Sorting")
    choice = input("Choose: ")

    def get_position(player):
        return player['position']

    def get_minutes(player):
        return player['minutes']

    if choice == "1":
        list_data.sort(key=get_position)
    elif choice == "2":
        list_data.sort(key=get_minutes, reverse=True)
    

    return list_data

def view_players():
    print("\n--- Squad (All Players) ---")
    show_players(sort_players(squad))
    print("\n--- Line-Up (Starting 11) ---")
    show_players(sort_players(lineup))
    print("\n--- Bench (Substitutes) ---")
    show_players(sort_players(bench))


def view_lineup():
    print("\n===== Current Starting Line-Up =====")
    if len(lineup) == 0:
        print("No players in Line-Up yet.")
    else:
        print(f"Total Players: {len(lineup)}/11") #to ensure that the total players only contain of 11 people for the final line up
        show_players(sort_players(lineup))


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

    # --- Move player ---
    print("\nDo you want to move this player?")
    print("1) Stay where they are")
    print("2) Move to Line-Up")
    print("3) Move to Bench")
    print("4) Move to Squad only")

    move_choice = input("Choose: ")

    # Remove from current list
    if player in lineup:
        lineup.remove(player)
    if player in bench:
        bench.remove(player)
    if player in squad:
        squad.remove(player)

    if move_choice == "1":
        squad.append(player)  # default "stay"
    elif move_choice == "2":
        if len(lineup) >= 11:
            print("Line-Up is full (11 players). Adding to Squad.")
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
        squad.append(player)

    print("Player update complete.")


def delete_player():
    pid = input("Enter Player ID to delete: ")
    player = find_player(pid)
    if not player:
        print("Player not found.")
        return

    if player in squad:
        squad.remove(player)
    if player in lineup:
        lineup.remove(player)
    if player in bench:
        bench.remove(player)
    print(f"Player {pid} deleted from system.")


def menu():
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
