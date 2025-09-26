def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    def add_item(item):
        shopping_list.append(item)
        return f"'{item}' has been added to the shopping list."
    
    def remove_item(item):
        if item in shopping_list:
            shopping_list.remove(item)
            return f"'{item}' has been removed from the shopping list."
        else:
            return f"'{item}' not found in the shopping list."

    def view_list():
        if not shopping_list:
            print("Shopping list is empty.")
        else:
            print("Shopping List:")
            for item in shopping_list:
                print(f"- {item}")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            new_item = input("Enter the item you want to add: ")
            print(add_item(new_item))
        elif choice == '2':
            # Prompt for and remove an item
            remove_item_name = input("Enter the item you want to remove: ")
            print(remove_item(remove_item_name))
        elif choice == '3':
            # Display the shopping list
            view_list()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





