import sys

cookbook = {
            'Sandwich': {
                'ingredients': ['ham', 'bread', 'cheese', 'tomato'],
                'meal': 'lunch',
                'prep_time': 10},
            'Cake': {
                'ingredients': ['flour', 'sugar', 'eggs'],
                'meal': 'dessert',
                'prep_time': 60},
            'Salad': {
                'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
                'meal': 'lunch',
                'prep_time': 15}
}

def ft_print():
	print("Cookbook recipes:")
	for name in cookbook:
		print("\t", name)
	print()

def ft_details(recipe):
	if recipe in cookbook:
		print("Recipe: ", recipe)
		for detkey, detvalues in cookbook[recipe].items():
			print("\t", detkey, ": ", detvalues)
	else:
		print("The recipe isn't in cookbook")
	print()

def ft_del(recipe):
	if recipe in cookbook:
		del cookbook[recipe]
		print('The recipe {} was deleted'.format(recipe))
	else:
		print("The recipe isn't in cookbook")
	print()

def ft_add():
	ingr = []
	name = input("Enter a name:\n")
	while (1):
		ingredient = input("Enter ingredients:\n")
		while (ingredient != ''):
			ingr.append(ingredient)
			ingredient = input()
		if (len(ingr) > 0):
			break
	meal = input("Enter a meal type:\n")
	prep = int(input("Enter a preparation time:\n"))
	cookbook[name]={
		"ingredients": ingr,
		"meal": meal,
		"prep_time": prep}
		
	
if __name__ == "__main__":
	print("Welcome to the Python Cookbook!")
	while (1):
		print("List of available option:")
		case = int(input("\t1: Add a recipe\n\t2: Delete a recipe\n\t3: Print a recipe\n\t4: Print the cookbook\n\t5: Quit\n"))
		if case == 1:
			ft_add()
		elif case == 2:
			recipe = input("Please enter a recipe name to delete:\n")
			ft_del(recipe)
		elif case == 3:
			recipe = input("Please enter a recipe name to get its details:\n")
			ft_details(recipe)
		elif case == 4:
			ft_print()
		elif case == 5:
			print("Cookbook closed. Goodbye!")
			break
		else:
			print("Sorry, this option does not exist.")

