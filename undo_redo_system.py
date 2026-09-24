# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        """ Creates a new node using the provided value and places it on top of the stack """

        new_node = Node(value)

        #Point to the old top
        new_node.next = self.top

        #Move top to the new node
        self.top = new_node

    def pop(self):
        """ Removes a node from the top of the stack """

        #Can't remove a node if it's not on the top of the stack
        if not self.top:
            return None

        removed_node = self.top

        #Move the top to the next node
        self.top = self.top.next

        return removed_node.value

    def peek(self):
        """ Returns the value of the node on top of the stack """

        #Check if self.top exists & return its value
        if self.top:
            return self.top.value
        else:
            return None

    def print_stack(self):
        """ Prints the contents of the stack """

        #Check if the stack is empty
        if not self.top:
            print("The stack is empty.")
            return
        else:

            #Keep track of current place in the stack
            current_node = self.top

            #Iterate through the stack and print each node's value
            while current_node:
                print(current_node.value)

                current_node = current_node.next


def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack

            undo_stack.push(action)

            redo_stack = Stack()


            print(f"Action performed: {action}")
        
        
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            value = undo_stack.pop()
            
            if value == None:
                print("No actions to undo.")
            else:
                redo_stack.push(value)

        
        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            value = redo_stack.pop()

            if value == None:
                print("No actions to redo.")
            else:
                undo_stack.push(value)


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()
            
            
        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()

            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()