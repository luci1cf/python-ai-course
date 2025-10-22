# Play Backpack Game To Practice Collection DataTypes
#
# dashes = '-'*50
#
# # Start Backpack Game
# #-----------------------------------------------
# pack = []
# print('0. Starting Journey with Empty Backpack.')
#
# print('Backpack: ', pack)
# print('-'*50)
#
# # Pick up StarterKit Items
# #-----------------------------------------------
# print('1. Picking up StarterKit (Armor, Shield, Sword, Potion).')
# pack.append('Sword')
# pack.append('Armor')
# pack.append('Shield')
# pack.append('Potion')
#
# print('Backpack: ', pack)
# print(dashes)
#
# # Loot a Treasure Chest
# #-----------------------------------------------
# chest = ['Map', 'Potion', 'Compass', 'Potion']
# pack.extend(chest)
#
# print('2. Looting a Treasure Chest!')
# print(f'Chest: {chest}')
#
#
# print('Backpack: ', pack)
# print(dashes)
#
# # Visit Merchant
# print('3. Visiting Merchant')
# print('- Selling the Shield.')
# print('- Upgrading Sword -> Magic GreatSword')
#
# pack.remove('Shield')
# inx         = pack.index('Sword')
# pack[inx] = 'Magic GreatSword'
#
# print('Backpack: ', pack)
# print('-'*50)
#
# # Check Inventory
# #---------------------------------------------------
# print('4. Checking Backpack: ')
# print(pack)
#
# total_count = len(pack)
# unique_items = set(pack)
# unique_count = len(set(unique_items))
# potion_count = pack.count('Potion')
#
# print(f'There are {total_count} items in total.')
# print(f'There are {unique_count} unique items.')
# print(f'There are {potion_count} potions.')
# print('-'*50)
#
# # Dropped the Backpack
# #----------------------------------------------------
# print('5. Dropped the Backpack Upside-Down...')
# pack.reverse()
#
# print('Backpack: ', pack)
# print('-'*50)
#
# # Sorting Items
# #----------------------------------------------------
# print('6. Sorting Items: ')
# pack.sort(key=len)
#
# print('Backpack: ', pack)
# print('-'*50)
#
# # 3 Items Stolen During Sleep
# print('7. Sleeping')
#
# a      = pack.pop()
# b      = pack.pop(2)
# c      = pack.pop()
# stolen = [a, b, c]
#
# print(f'Stolen Items: {stolen}')
# print('Backpack: ', pack)
# print('-'*50)
#
# # Found Magic-Ring
# print('8. Found Magic Ring And Coin Pouch.')
# ring = 'Magic Ring'
# coin_pouch = ['Gold Coin', 'Silver Coin']
#
# pack.insert(0, ring)
# pack.append(coin_pouch)
#
# print('Backpack: ', pack)
# print('-'*50)
#
# # Half of the Backpack Items Have Teleported
# #---------------------------------------------------
# print('9. Half Items Magically Disappeared. Damn You Magic Ring...')
#
# count    = len(pack)
# half     = count // 2
# pack = pack[half:]
#
# print('Backpack: ', pack)
# print('-'*50)
#
# # Bandits Stole Empty Backpack
# #--------------------------------------------------
# print('10. Bandits Attacked.')
# print('Backpack Stolen...')
#
# pack.clear()
#
# print('Backpack: ', pack)
# print('-'*50)

# Dictionaries
# phonebook = {
#     'Ricky' : '+43 4111 5111',
#     'Tommy' : '+43 4222 6222',
#     'Klaus' : '+43 4333 7333' }          # Name : 'Number'
#
# # Add More Items
# phonebook['Erik']       = '+372 5555 5555'
# phonebook['Kristina']   = '+372 5656 5656'
# phonebook['Theo']       = '+372 5757 5757'
#
# print(phonebook)
#
# number = phonebook['Erik']
# print(f'Calling Erik... ({number})')
#
# number = phonebook['Theo']
# print(f'Calling Theo... ({number})')
#
# number = phonebook['Kristina']
# print(f'Calling Kristina... ({number})')

# LEVEL TWO DICTIONARY (Advanced)
player = {
    'Name'      : 'Erik',
    'Class'     : 'Warrior',
    'Health'    : 100,
    'Level'     : 1,
    'Backpack'  : []
}

# Modify Stats
player['Health'] += 1

# Add Items
player['Backpack'].append('Item-A')
player['Backpack'].append('Item-B')
player['Backpack'].append('Item-C')
player['Backpack'].append([10,20,30])

for k,v in player.items():
    print(k, v)
