"""Project Two starter for the student's text-based adventure game."""

# Dylan Galvin


def show_instructions():
    """Display the game objective and available commands."""
    # TODO: Print instructions that match your game and commands.
    print("Cyber Siege Text Adventure Game")
    print("Collect all 6 items before encountering the villain!")
    print("Move commands: go North, go South, go East, go West")
    print("Collect items: get 'item name'")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    # TODO: Show the current room.
    # TODO: Show the current inventory.
    # TODO: Show the current-room item when one is available.
    print("\nYou are in the", current_room)
    print("Inventory:", inventory)

if 'item' in rooms[current_room]:
    print("You see a", rooms[current_room]['item'])

print("---------------------------")


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.
    
    rooms = {
        'Security Operations Center': {
            'east': 'Server Room',
            'south': 'IT Help Desk'
        },
        'Server Room': {
            'west': 'Security Operations Center',
            'east': 'Network Operations Center',
            'south': 'Firewall Control Room',
            'item': 'Encryption Key'
        },
        'Network Operations Center': {
            'west': 'Server Room',
            'east': 'Data Center',
            'south': 'Backup Server Room',
            'item': 'Network Scanner'
        },
        'Data Center': {
            'west': 'Network Operations Center',
            'item': 'Security Token'
        },
        'IT Help Desk': {
            'north': 'Security Operations Center',
            'east': 'Firewall Control Room',
            'item': 'Antivirus Software'
        },
        'Firewall Control Room': {
            'north': 'Server Room',
            'west': 'IT Help Desk',
            'east': 'Backup Server Room',
            'item': 'Firewall Patch'
        },
        'Backup Server Room': {
            'north': 'Network Operations Center',
            'west': 'Firewall Control Room',
            'east': "Hacker's Command Center",
            'item': 'Backup Drive'
        },
        "Hacker's Command Center": {
            'west': 'Backup Server Room',
            'villain': 'GhostByte'
        }
    }

    # TODO: Set the player's starting room.
    current_room = 'Security Operations Center'
    # TODO: Create the player's inventory.
    inventory = []
    # TODO: Call the instruction function at the appropriate time.
    show_instructions()
    # TODO: Create the gameplay loop.
    while True:
        show_status(current_room, inventory, rooms)

        command = input("\nEnter your command: ").lower().strip()
            
        if command.startswith('go '):
            direction = command[3:]

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print("You moved to the", current_room)
                
                if 'villain' in rooms[current_room]:
                    if len(inventory) == 6:
                        print("Congratulations! You collected all 6 items!")
                        print("You defeated GhostByte and saved the network!")
                    else:
                        print("GhostByte has defeated you!")
                        print("You did not collect all 6 items.")
                        print("Game Over!")

                    break

            else:
                print("You cannot go that way.")

        elif command.startswith('get '):
            item_name = command[4:]

            
            if 'item' in rooms[current_room]:
                item = rooms[current_room]['item']

                if item_name == item.lower():
                    inventory.append(item)
                    del rooms[current_room]['item']
                    print("You collected the", item)
                else:
                    print("That item is not in this room.")
            else:
                print("There is no item to collect here.")

        else:
            print("Invalid command. Use 'go direction' or 'get item name'.")


    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    


if __name__ == "__main__":
    main()
