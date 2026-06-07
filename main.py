from stats import build_player

print("Welcome to my NBA stats project!")
while True:
    print("\n1. Search player stats \n2. Compare two players \n3. Quit")
    choice = input("\nType 1, 2, or 3 for which operation you would like to complete: ")
    if choice == '1':
        while True:
            player_name = input("\nProvide the name of an NBA player: ")
            player_result = build_player(player_name)

            if player_result == None:
                print("Player not found, try again please")
                continue
            elif player_result == "no_stats":
                print("No stats available for this player yet.")
                continue
            else:
                player_result.display_stats()
                break

    elif choice == '2':
        while True:
            player_name1 = input("\nProvide the name of an NBA player: ")
            player_result1 = build_player(player_name1)

            if player_result1 == None:
                print("Player1 not found, try again please")
                continue
            elif player_result1 == "no_stats":
                print("No stats available for this player yet.")
                continue
            else:
                player_result1.display_stats()
                break

        while True:
            player_name2 = input("\nProvide the name of another NBA player: ")
            player_result2 = build_player(player_name2)

            if player_result2 == None:
                print("Player2 not found, try again please")
                continue
            elif player_result2 == "no_stats":
                print("No stats available for this player yet.")
                continue
            else:
                player_result2.display_stats()
                break

    elif choice == '3':
        break
    
    else:
        print("Please enter a valid input. Try again.")
        continue

