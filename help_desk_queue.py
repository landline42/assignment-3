# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    # Delete the following line and implement your Queue class
    
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """ Creates a new node with the provided value, then adds it to the queue. """

        #Create a new Node object using the provided value
        new_node = Node(value)

        #Check if there are any nodes in the queue. If there are none, make the new node the front and back of the queue
        if not self.front:
            self.front = new_node
            self.rear = new_node
        
        #Otherwise, place the new node at the end of the queue
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """ Removes a node from the front of the queue. """

        #Check if the queue is empty
        if not self.front:
            return None

        #Always remove nodes from the front of the queue
        removed_node = self.front
        self.front = self.front.next

        #Change the front to the next node in the queue
        if not self.front:
            self.rear = None
        return removed_node.value

    def peek(self):
        """ Shows the value of the node currently at the front of the queue """
        
        #Check if there is a node at the front of the queue
        if self.front:
            return self.front.value
        
        #Otherwise, return None of the queue is empty
        else:
            return None

    def print_queue(self):
        """ Prints the value of each node in the queue"""

        #Start with the first node in the queue
        current_node = self.front

        #Check if the queue is empty
        if not current_node:
            print("The queue is empty.")
            return

        #iterate through the queue and print each node's value
        while current_node:
            print(f" - {current_node.value}")
            current_node = current_node.next


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            
            if len(name) > 0:
                queue.enqueue(name)
                print(f"{name} added to the queue.")
            else:
                print("Name cannot be blank.")

            
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            name = queue.dequeue()
            
            if name != None:
                print(name, " was helped. Removed from queue.")
            else:
                print("The queue is empty.")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            
            next_customer = queue.peek()
            if next_customer != None:
                print("Next customer in the queue:", queue.peek())
            else:
                print("The queue is empty.")


        elif choice == "4":
            print("\nWaiting customers:")
            # Print all customers in the queue
            queue.print_queue()

            
        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
