# Create a class
class Shoes:

    # Constructor method with parameters
    def __init__(self, country, code, product, cost, quantity):

        # Create Attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Method to return self.cost
    def get_cost(self):
        return self.cost

    # Method to return self.quantity
    def get_quanty(self):
        return self.quantity

    # Representation of a class.
    def __str__(self):
        return self.country + ", " + self.code + ", "+self.product + ", " + str(self.cost) + ", "+ str(self.quantity)


# Variable will be used to store a list of shoes objects
shoes = []

# Method to read shoe data 
# Open inventory.txt and read the data f
# Append object into the shoes list
def read_shoes_data():
    file = "inventory.txt"
    try:
        lineNo = 0
        # Open file in read mode
        with open(file, 'r') as f:
            
            # Iterate
            for line in f:
                if lineNo != 0:
                    
                    # Store the data by spliting
                    (country, code, product, cost, quantity) = line.rstrip('\n').strip().split(',')
                    
                    # Add data to list
                    shoes.append(Shoes(country,code,product,int(cost),int(quantity)))
                lineNo += 1
        print("Read Data from inventory.txt files")
    except IOError:
        print("File ", file, " not accessible")

# Method for user to capture
# Append to the shoe list.
def capture_shoes():
    shoe_country = input("Enter country of the shoe: ")
    shoe_code = input("Enter the code of the shoe: ")
    shoe_product = input("Enter the product of the shoe: ")
    shoe_cost = int(input("Enter the cost of the shoe: "))
    shoe_quantity = int(input("Enter the quantity of the shoe: "))

    # Create shoe objects
    shoe = Shoes(shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity)
    
    # Add the shoe to the list
    shoes.append(shoe)
    
# Method to view all shows
# Print the details of the shoes
def view_all():
    for shoe in shoes:
        print(str(shoe))

# Method to restock shoes
def re_stock():
    lowest_quantity = shoes[0]
    
    # Iterate 
    for shoe in shoes:
        
        # Check the lowest quantity to restock
        if shoe.get_quanty() < lowest_quantity.get_quanty():
            lowest_quantity = shoe

    # Print the lowest quantity
    print("Lowest Quantity Details\n"+str(lowest_quantity))

    
    # Ask user if the what to add quantity
    # If yes update quantity
    restock = input("Do you want to add to quantity of shoes(yes/no)? ")
    if restock.lower() == "yes":
        update_quantity = int(input("Enter the quantity to update: "))
        lowest_quantity.quantity = lowest_quantity.get_quanty() + update_quantity
    else:
        print("You selected no need to restock")



# Method to search a shoe
def seach_shoe(code):
    
    # Iterate
    for shoe in shoes:
        
        # Check the code matches
        if shoe.code == code:
            return shoe

# Method to get value per intem
# Total value for each item
def value_per_item():
    value = 0
    
    # iterate
    for shoe in shoes:
        value = shoe.get_cost() * shoe.get_quanty()

        # Print Value
        print(str(shoe) +"\tValue: " + str(value))

    # Return the value
    return value

# Method to check highest quantity
def highest_qty():
    highest_quantity_shoe = shoes[0]

    # iterate through the list
    for shoe in shoes:
        
        # check if quantity is highest
        if shoe.get_quanty() > highest_quantity_shoe.get_quanty():
            highest_quantity_shoe = shoe

    print(f"Sale Sale , shoe is on sale \n {str(highest_quantity_shoe)}\n")


# Menu to choose from
if __name__ == '__main__':
    choice = 0
    while True:
        print("1. Read shoe data")
        print("2. Capture data for a shoe")
        print("3. View all the Shoes")
        print("4. Find shoe that needs to be re-stocked")
        print("5. Search for a Shoe")
        print("6. Total value of shoes")
        print("7. Product on sale")
        print("8. Exit")

        # Choice from user
        choice = int(input("Enter choice: "))

        # Functions for menu
        if choice == 1:
            read_shoes_data()
        elif choice == 2:
            capture_shoes()
        elif choice == 3:
            view_all()
        elif choice == 4:
            re_stock()
        elif choice == 5:
            code = input("Enter code to search? ")
            print(str(seach_shoe(code)))
        elif choice == 6:
            value_per_item()
        elif choice == 7:
               highest_qty()
        elif choice == 8:
            print("Thank you for using the program,Have a great day!")
            break
        else:
            print("The choice you selected is invalid!")

            #Note for code reviewer
            # Read shoe data 1st in order to view shoes

