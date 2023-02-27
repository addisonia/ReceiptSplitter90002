class Item:
	def __init__(self, item_name, price, buyer_list):
		self.item_name = item_name
		self.price = price
		self.buyer_list = buyer_list

class Buyer:
	def __init__(self, buyer_name):
		self.buyer_name = buyer_name

def main():
	print("               RECEIPT SPLITTER 9001\n")
	buyers = {} # dictionary of all the buyers: key = name, value = Buyer object
	items = {} # dictionary of all the items: key = name, value = Item object

	# Determine who is in on the bill
	print("Enter buyers' names (enter \"done\" or \"d\" when finished):")
	print("--------------------------------------------------")
	buyer_count = 1 # buyer that is currently being entered
	while True:
		user_input  = input("Buyer " + str(buyer_count) + ": ").lower()
		if user_input  == "done" or user_input == "d": break

		buyer_name = user_input 

		buyers[buyer_name] = Buyer(buyer_name)

		buyer_count += 1
	print("") # print empty line
	
	# Determine what items are on the bill
	print("For each item, enter its name and price. Then enter everyone who is buying it. (enter \"done\" or \"d\" when all items are in):")
	print("--------------------------------------------------")
	item_count = 1
	while True:
		# Get name
		user_input  = input("Item " + str(item_count) + " name: ").lower()
		if user_input  == "done" or user_input == "d": break

		item_name = user_input 

		# Get price	
		item_price_is_float = False
		while not item_price_is_float:
			try:
				item_price = float(input("Item " + str(item_count) + " price: "))
				item_price_is_float = True
			except: pass

		# Get buyer list
		buyer_list = [] # the list of buyers for this item
		print("Enter every buyer for this item (enter either \"done\" or \"d\" when finished or \"everyone\" or \"e\" if its everyone):")
		item_buyer_count = 1
		while True:
			everyone = False # set to true if every buyer is in on this item
			user_input = input("Buyer " + str(item_buyer_count) + ": ").lower()
			if user_input  == "done" or user_input == "d": break
			elif user_input == "redo": 
				buyer_list.pop()
				item_buyer_count -= 1 
				continue
			elif user_input == "everyone" or user_input == "all" or user_input == "e": everyone = True

			if not everyone:
				# Check if the inputted name is valid
				while not user_input in buyers:
					user_input  = input("Enter a name that is in the buyers list: ").lower()
					if user_input == "everyone" or user_input == "all" or user_input == "e":
						everyone = True
						break
					elif user_input == "done" or user_input == "d": break
					elif user_input == "redo":
						buyer_list.pop()
						item_buyer_count -= 1 
						break
				if user_input == "done" or user_input == "d": break
				elif user_input == "redo": continue
			
			if everyone:
				# add every buyer to buyer list
				for name in buyers.keys():
					buyer_list.append(name)
					item_buyer_count += 1
				break
			else:
				item_buyer_name = user_input 

				buyer_list.append(item_buyer_name)

				item_buyer_count += 1
		print("")

		# Add this item to item list
		items[item_name] = Item(item_name, item_price, buyer_list)
		if len(items[item_name].buyer_list) != 0:
			items[item_name].price_per_buyer = items[item_name].price / (float)(len(items[item_name].buyer_list)) # determine price per buyer for this item
			item_count += 1
		else: del items[item_name]
			
	print("") # print empty line

	# Determine tax
	tax_is_float = False
	while not tax_is_float:
		try:
			tax = float(input("Enter the total tax or shipping: "))
			tax_is_float = True
		except: pass
	# tax_per_buyer = tax / (float)(len(buyers))


	# For every buyer, calculate total amount they owe (BEFORE tax)
	total = 0
	for buyer in buyers:
		price_before_tax = 0 # init to 0

		for item in items:
			if buyers[buyer].buyer_name in items[item].buyer_list: price_before_tax += items[item].price_per_buyer

		buyers[buyer].total_payment_due = price_before_tax

	# calculate total
	for buyer in buyers: total += buyers[buyer].total_payment_due

	#calculate total owed per buy (WITH tax)
	for buyer in buyers: buyers[buyer].total_payment_due_FINAL = buyers[buyer].total_payment_due + ((buyers[buyer].total_payment_due / total) * tax)

        
	print("") # print empty line

	# For every buyer, print the total amount they owe
	for buyer in buyers:
		output_name = buyer[0].upper() + buyer[1:] # capitalize first letter in name

		print(f'{output_name}\'s price is: ${round(buyers[buyer].total_payment_due_FINAL, 2)}')


if __name__ == "__main__":
	main()
