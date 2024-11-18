from DSALinkedlist import DSALinkedList
from DSAStack import *
from DSAQueue import *
import numpy as np
from DSAHash import DSAHashTable, DSAHashEntry

class Shop:
    def __init__(self, shop_number, shop_name, category, location, rating):
        self.adjacent_shops = DSALinkedList()
        self.shop_number = shop_number
        self.shop_name = shop_name
        self.category = category
        self.location = location
        self.rating = rating
        self.visited = False

    def reset_visited(self):
        self.visited = False

class GraphShop(DSAHashTable):
    def __init__(self, max_size, initial_size, loadFactorThreshold=0.7, shrinkFactorThreshold=0.3):
        super().__init__(max_size, initial_size, loadFactorThreshold=0.7, shrinkFactorThreshold=0.3)
        self.shopsList = DSALinkedList()
        self.hashShop = DSAHashTable(10)
        self.adj_shops = DSAQueue()
        self.queue = DSAQueue()
        self.path = DSALinkedList()
        self.breadthFirstSearch_path_length = 0
        self.depthFirstSearch_path_length = 0
    ################Add Shops to the graph############################
    def addShop(self, shopnumber, shopname, category, location, rating):
        try:
            existing_shop = self.findShop(shopnumber)
            if existing_shop is None:
                new_shop = Shop(shopnumber, shopname, category, location, rating)
                self.shopsList.insert_last(new_shop)
                self.put(category, new_shop)
            else:
                print(f'\nShop with shop number {shopnumber} already exists.\n')
        except Exception as e:
            print(f'\nAn error occurred while adding the shop: {str(e)}\n')
    ##############Find the shop with shop number###############################
    def findShop(self, shopnumber):
        try:
            current_shop = self.shopsList.head
            while current_shop is not None:
                if current_shop.get_value().shop_number == shopnumber:
                    return current_shop
                current_shop = current_shop.get_next()
        except Exception as e:
            print(f"An error occurred: {str(e)}")


    ############################Delete an existing shop#############################        
    def deleteShop(self, shop_number):
        try:
            current_shop = self.shopsList.head
            prev_shop = None

            if current_shop is None:
                print('\nNo shops to delete.\n')
                return

            while current_shop is not None:
                print(type(current_shop.get_value().shop_number),' -> ', current_shop.get_value().shop_number)
                print(type(shop_number),' -> ',shop_number)
                if current_shop.get_value().shop_number == shop_number:
                    shop_category = current_shop.get_value().category
                    self.remove_shop_from_hash(shop_number, shop_category)
                    self.deleteFromAdjacentlist(current_shop)
                    if prev_shop is None:
                        self.shopsList.head = current_shop.get_next()
                    else:
                        prev_shop.set_next(current_shop.get_next())
                    current_shop.set_next(None)
                    print(f'\nShop with shop number {shop_number} has been deleted from graph.\n')
                    return
                prev_shop = current_shop
                current_shop = current_shop.get_next()

            print(f'\nShop with shop number {shop_number} not found.\n')
        except Exception as e:
            print(f'\nAn error occurred while deleting the shop: {str(e)}\n')
    ####################Delete shop from adjacent list########################3
    def deleteFromAdjacentlist(self, shop_to_remove):
        try:
            current_shop = self.shopsList.head
            # shop1 = self.findShop(shop_to_remove)
            while current_shop is not None:
                self.removeAdjacentShops(shop_to_remove, current_shop)
                current_shop = current_shop.get_next()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    ##################Display all shops###############################
    def displayShopsList(self):
        try:
            current_shop = self.shopsList.head
            while current_shop is not None:
                print("Shop Number:", current_shop.get_value().shop_number, end=" ")
                print("\tShop Name:", current_shop.get_value().shop_name, end=" ")
                print("\tCategory:", current_shop.get_value().category, end=" ")
                print("\tLocation:", current_shop.get_value().location, end=" ")
                print("\tRating:", current_shop.get_value().rating, end=" ")
                print()
                current_shop = current_shop.get_next()
        except Exception as e:
            print(f'\nAn error occurred while displaying shops: {str(e)}\n')
    ###############Update the Shop##################################################
    def updateShop(self, shop_number, new_shop_name, new_category, new_location, new_rating):
        try:
            current_shop = self.shopsList.head
            found = False
            while current_shop is not None:
                if current_shop.get_value().shop_number == shop_number:
                    current_shop.get_value().shop_name = new_shop_name
                    current_shop.get_value().category = new_category
                    current_shop.get_value().location = new_location
                    current_shop.get_value().rating = new_rating
                    print(f'\nShop with shop number {shop_number} has been updated.\n')
                    found = True
                    break
                current_shop = current_shop.get_next()
            
            if not found:
                print(f'\nShop with shop number {shop_number} not found.\n')
        except Exception as e:
            print(f'\nAn error occurred while updating the shop: {str(e)}\n')
    #################Add edges/ coonection between two shops########################
    def addEdge(self, shop_number1, shop_number2):
        try:
            shop1 = self.findShop(shop_number1)
            shop2 = self.findShop(shop_number2)
            if shop1 and shop2:
                shop1.get_value().adjacent_shops.insert_sorted(shop2)
                shop2.get_value().adjacent_shops.insert_sorted(shop1)
            else:
                print('\nOne or both shops not found.\n')
        except Exception as e:
            print(f'\nAn error occurred while adding an edge: {str(e)}\n')
    ###############Remove edges between two shops####################
    def removeEdge(self, shop_number1, shop_number2):
        try:
            shop1 = self.findShop(shop_number1)
            shop2 = self.findShop(shop_number2)

            if shop1 and shop2:
                self.removeAdjacentShops(shop1, shop2)
                self.removeAdjacentShops(shop2, shop1)
                print(f'\nRemoved edge between Shop {shop_number1} and Shop {shop_number2}.\n')
            else:
                print('\nOne or both shops not found.\n')
        except Exception as e:
            print(f'\nAn error occurred while removing an edge: {str(e)}\n')
    ##############Remove Adjacent Shops############################
    def removeAdjacentShops(self, shop_to_remove, shop_to_check):
        try:
            current_shop = shop_to_check.get_value().adjacent_shops.head
            prev_shop = None

            while current_shop is not None:
                if current_shop.get_value() == shop_to_remove:
                    if prev_shop is None:
                        shop_to_check.get_value().adjacent_shops.head = current_shop.get_next()
                        if current_shop.get_next() is None:
                            shop_to_check.get_value().adjacent_shops.tail = None  # Remove tail reference if last node
                    else:
                        prev_shop.set_next(current_shop.get_next())
                        if current_shop.get_next() is not None:
                            current_shop.get_next().set_prev(prev_shop)
                        if current_shop.get_next() is None:
                            shop_to_check.get_value().adjacent_shops.tail = prev_shop  # Update tail if last node       
                    current_shop.set_next(None)
                    current_shop.set_prev(None)
                    return
                prev_shop = current_shop
                current_shop = current_shop.get_next()
        except Exception as e:
            print(f'\nAn error occurred while removing the shop from adjacent shops: {str(e)}\n')

    ############Find the Neighbour Shops######################
    def findAdjacentShops(self, shop_number):
        try:
            current_shop = self.shopsList.head
            while current_shop is not None:
                if current_shop.get_value().shop_number == shop_number:
                    return current_shop
                current_shop = current_shop.get_value().adjacency_list.head
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        return None
    #########Display Neighbour Shops######################
    def displayAdjacentShops(self):
        try:
            print('\n\nAdjacent Shop List \n')
            current_shop = self.shopsList.head
            while current_shop is not None:
                print(f"\n{current_shop.get_value().shop_number} : ", end =" ")
                current_adjacent_shop = current_shop.get_value().adjacent_shops.head
                while current_adjacent_shop is not None:
                    adjacent_shop = current_adjacent_shop.get_value()  
                    print(f"{adjacent_shop.get_value().shop_number} ->", end =" ")
                    current_adjacent_shop = current_adjacent_shop.get_next()
                current_shop = current_shop.get_next()
        except Exception as e:
            print(f'\nAn error occurred while displaying adjacent shops: {str(e)}\n')
    
    def checkShop(self, start, end):
        try:
            start_found = False
            end_found = False

            current_shop = self.shopsList.head
            while current_shop is not None:
                if current_shop.get_value().shop_number == start:
                    start_found = True
                if current_shop.get_value().shop_number == end:
                    end_found = True 
                current_shop = current_shop.get_next()
            if start_found and end_found:
                return True
            if not start_found:
                print('\n{} shop number not found in the graph'.format(start))
            if not end_found:
                print('\n{} shop number not found in the graph'.format(end))
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    ################Breadth First Search#######################
    def breadthFirstSearch(self, shop1, shop2):
        try:
            shop_found = False
            # Mark all vertices as new
            current_node = self.shopsList.head
            while current_node is not None:
                current_node.get_value().visited = False
                current_node = current_node.get_next()

            shop_exists = self.checkShop(shop1, shop2)
            if not shop_exists:
                return None

            # Initialize the queue for breadthFirstSearch
            queue = DSAQueue()
            path_queue = DSAQueue()
            queue.enqueue(shop1)  # Enqueue the start vertex
            path_queue.enqueue(shop1)

            while not queue.is_empty():
                v = queue.dequeue()

                # Find the shop with shop_number v
                current_node = self.shopsList.head
                current_shop = None
                while current_node is not None:
                    if current_node.get_value().shop_number == v:
                        current_shop = current_node.get_value()
                        break
                    current_node = current_node.get_next()

                if current_shop is not None:
                    current_shop.visited = True

                    # Iterate through adjacent shops
                    current_adjacent_node = current_shop.adjacent_shops.head
                    while current_adjacent_node is not None:
                        adjacent_shop = current_adjacent_node.get_value()
                        w = adjacent_shop.get_value().shop_number  # Access the shop number

                        if not adjacent_shop.get_value().visited:
                            path_queue.enqueue(w)
                            adjacent_shop.get_value().visited = True
                            queue.enqueue(w)

                        if v == shop2:
                            # Stop the traversal if shop2 is found
                            print("\nShop {} found.\n".format(shop2))
                            shop_found = True
                            print('\nbreadthFirstSearch Path\n')
                            while not path_queue.is_empty():
                                self.queue = path_queue
                                item = path_queue.dequeue()
                                self.breadthFirstSearch_path_length += 1
                                print('{} - > '.format(item), end='')
                                if item == shop2:
                                    break
                            print()
                            return True

                        current_adjacent_node = current_adjacent_node.get_next()

            # If you reach this point, it means shop2 was not found during the traversal.
            if not shop_found:
                print("\nShop {} not found in the graph.\n".format(shop2))
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def depthFirstSearch(self, shop1, shop2):
        try:
            shop_found = False

            # Mark all vertices as new
            current_node = self.shopsList.head
            while current_node is not None:
                current_node.get_value().visited = False
                current_node = current_node.get_next()

            shop_exists = self.checkShop(shop1, shop2)
            if not shop_exists:
                return None

            # Initialize the stack for depthFirstSearch
            stack = DSAStack()
            # to store the path traversal
            temp_queue = DSAQueue()
            stack.push(shop1)  # Push the start vertex

            while not stack.is_empty():
                v = stack.pop()
                temp_queue.enqueue(v)
                # Find the shop with shop_number v
                current_node = self.shopsList.head
                current_shop = None
                while current_node is not None:
                    if current_node.get_value().shop_number == v:
                        current_shop = current_node.get_value()
                        break
                    current_node = current_node.get_next()
                if current_shop is not None:
                    current_shop.visited = True

                    # Iterate through adjacent shops 
                    current_adjacent_node = current_shop.adjacent_shops.tail
                    while current_adjacent_node is not None:
                        adjacent_shop = current_adjacent_node.get_value()
                        w = adjacent_shop.get_value().shop_number  

                        if not adjacent_shop.get_value().visited:
                            stack.push(w)

                        if v == shop2:
                            print('\n\ndepthFirstSearch path\n')
                            while not temp_queue.is_empty():
                                self.depthFirstSearch_path_length += 1
                                print('{} - > '.format(temp_queue.dequeue()), end='')
                            return True

                        current_adjacent_node = current_adjacent_node.get_prev()

            # If you reach this point, it means shop2 was not found during the traversal.
            print("Shop {} not found in the graph.".format(shop2))
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def shortestPath(self, start, end):
        try:
            # Compare the lengths
            path_exists_breadthFirstSearch = self.breadthFirstSearch(start, end)
            path_exists_depthFirstSearch = self.depthFirstSearch(start, end)
            if path_exists_breadthFirstSearch and path_exists_depthFirstSearch:
                if self.breadthFirstSearch_path_length < self.depthFirstSearch_path_length:
                    print("\n\nbreadthFirstSearch path is shorter.\n")
                elif self.breadthFirstSearch_path_length > self.depthFirstSearch_path_length:
                    print("\n\ndepthFirstSearch path is shorter.\n")
                else:
                    print("\n\nBoth paths have the same length.\n")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def print_menu():
    print("\nShop Navigation System:\n")
    print("a. Add a shop")
    print("b. Add an edge")
    print("c. Remove a shop")
    print("d. Remove an edge")
    print("e. Update shop")
    print("f. Display all shops")
    print("g. Display all adjacent shops with neighbors")
    print("h. Display breadthFirstSearch path")
    print("i. Display depthFirstSearch path")
    print("j. Find Shortest path")
    print("k. Display shops based on category")
    print("l. Display shops based on rating")
    print("m. Adding shops")
    print("n. Adding shop edges")
    print("o. Exit from the menu")

if __name__ == "__main__":
    #creatting shop_graphect
    shop_graph = GraphShop(20, 10, loadFactorThreshold=0.7, shrinkFactorThreshold=0.3)
    while True:
        try:
            print_menu()
            choice = input("\nEnter your choice : ")
            if choice == "a":
                 # Input validation for shop number
                while True:
                  try:
                      shop_number = int(input("Enter shop number: "))
                      break
                  except ValueError:
                    print("Invalid input. Please enter a numeric value for shop number.")
                shop_name = input("Enter shop name: ")
                category = input("Enter shop category: ")
                location = input("Enter shop location: ")

                # Input validation-rating
                while True:
                    try:
                        rating = int(input("Enter shop rating (0 to 5): "))
                        if 0 <= rating <= 5:
                            shop_graph.addShop(shop_number,shop_name,category,location,rating)
                            break  
                        else:
                            print("Rating must be between 0 and 5.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for rating.")
                    
            elif choice == "b":
                shop1 = input('Enter shop 1 : ')
                shop2 = input('Enter shop 2 : ')
                #addEdge method
                shop_graph.addEdge(shop1,shop2)
                
            elif choice == "c":
                shop = input('Enter shop number you want to delete : ')
                #deleteShop method
                shop_graph.deleteShop(shop)
                
            elif choice == "d":
                shop1 = input('Enter shop number of shop 1 : ')
                shop2 = input('Enter shop number of shop 2 : ')
                #removeEdge method
                shop_graph.removeEdge(shop1, shop2)
                
            elif choice == "e":
                shop_number = int(input("Enter shop number of shop you want to update: ")) 
                shop_name = input("Enter new shop name : ") 
                category = input("Enter new shop category : ")  
                location = input("Enter new shop location : ") 
                # Input validation for rating
                while True:
                    try:
                        rating = int(input("Enter shop rating (0 to 5): "))
                        if 0 <= rating <= 5:
                            # Call the updateShop method to update shop details
                            shop_graph.updateShopShop(shop_number, shop_name, category, location, rating)
                            break  # Rating is valid, exit the loop
                        else:
                            print("Rating must be between 0 and 5.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value for rating.")
                    
    

               
            elif choice == "f":
                # Display shops
                shop_graph.displayShopsList()

            elif choice == "g":
                # display adjacent shops
                shop_graph.displayAdjacentShops()
                
            elif choice == "h":
                start = input('Enter starting shop : ')
                end = input('Enter last shop : ')
                # breadthFirstSearch method to find breadthFirstSearch path
                shop_graph.breadthFirstSearch(start, end)
                
            elif choice == "i":
                start = input('Enter starting shop : ')
                end = input('Enter last shop : ')
                #  depthFirstSearch method to find depthFirstSearch path
                shop_graph.depthFirstSearch(start, end)

            elif choice == "j":
                start = input('Enter starting shop : ')
                end = input('Enter last shop : ')
                # shortestPath method to find shortest path between breadthFirstSearch and depthFirstSearch
                shop_graph.shortestPath(start, end)
                
            elif choice == "k":
                category = input('Enter the category of shop you want to display : ')
                #  display_shops_in_category to display shops based on category method
                shop_graph.display_hash_table(category)

            elif choice == "l":
                category = input('Enter the category of shop you want to display : ')
                # display_shops_in_heap to display shops based on rating method
                shop_graph.get_shops_in_category(category)
                shop_graph.display_shops_in_heap()

            elif choice == "m":
                # add shops sample data into graph
                print('\nAdding shops \n')
                shop_graph.addShop('1100','Best and Less','Clothing','Floor 2 ',5)
                shop_graph.addShop('2200','Target Electronics','Electronics','Floor 1 ',4)
                shop_graph.addShop('3300','JB hi-fi','Electronics','Floor 2 ',2)
                shop_graph.addShop('4400', 'Kmart', 'Clothing', 'Floor 3 ', 1)
                shop_graph.addShop('5500','Cindrella', 'Books', 'Floor 1 ', 3)
                shop_graph.addShop('6600','Hush and Puppies', 'Gifts', 'Floor 2 ', 5)
                shop_graph.addShop('7700','Kinder Joy', "Toys", 'Floor 3 ', 4)
                
                
            elif choice == "n":
                # sample data-creating edges
                print('\nAdding edges into the graph to connect shops \n')
                shop_graph.addEdge('1100','2200')
                shop_graph.addEdge('1100','3300')
                shop_graph.addEdge('2200','4400')
                shop_graph.addEdge('3300','5500')
                shop_graph.addEdge('4400','6600')
                shop_graph.addEdge('7700','6600')
                shop_graph.addEdge('5500','7700')

            elif choice == "0":
                print("\nExiting the Shop Navigation System.\n")
                break
            else:
                print("\nInvalid choice. Please select a valid option.\n")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

