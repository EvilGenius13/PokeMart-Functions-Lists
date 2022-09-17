# variables/lists
pokemon = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur']
poke_visits = [5, 6, 8, 2]
cost_per_day = 100


#function to add new Pokemon by input
def addpokemon():
        pokemon_add = input(f"Enter the name of your pokemon :")
        pokemon.append(pokemon_add)


#test function
addpokemon()
print(pokemon)
# list to pull individual pokemon / visit #
# - pokeinvidivualvisit(num)
def pokeindividualvisit (num):
        print(f'{pokemon[num]} has visited {poke_visits[num]} times.')

#test function
pokeindividualvisit(3)

#function to show all of the dogs
# and the amount of visits - listvisit()
def listvisit ():
        for pokemo, poke_visit in zip(pokemon,poke_visits):
                print("{} has visited {} times".format(pokemo,poke_visit))

#test function
listvisit()


#function to show individual pokemon, total visits, and total cost.
def pokeindividualbill(num):
        result = poke_visits[num] * cost_per_day
        return (f'{pokemon[num]} has visited {poke_visits[num]} times for a total of {result}$')

#test functon
print(pokeindividualbill(2))


# TODO: Using the function you created in the previous 
# step print a billing message for each dog. Include the 
# dog's name, the number of visits, cost per visit, and 
# the total bill: 
# TODO: Print a billing message for each dog in your list: 


def poketotalbill():
        count = 0
        for count in range(len(poke_visits)):
                result = poke_visits[count] * cost_per_day
                print(f'{pokemon[count]} has visited {poke_visits[count]} times.')
                print(f'With a daily rate of {cost_per_day}, the total bill is {result}')
poketotalbill()