import random

# Configuration for rarities and colors
rarities = {
    "Rare/Mythic": 1,
    "Uncommon": 3,
    "Common": 11
}
colors = ["White", "Blue", "Black", "Red", "Green", "Artifact", "Multicolor"]

# Function to generate a random pack
def generate_pack(pack_number):
    pack = []
    
    # Generate cards based on rarity slots
    for rarity, count in rarities.items():
        for _ in range(count):
            color = random.choice(colors)  # Randomly pick a color
            pack.append({"rarity": rarity, "color": color})
    
    # Add random lands for fixing
    lands = random.choices(["Plains", "Island", "Swamp", "Mountain", "Forest"], k=random.randint(1, 2))
    for land in lands:
        pack.append({"rarity": "Land", "color": "N/A", "card": land})

    # Generate Markdown table
    print(f"### Pack {pack_number}")
    print("| Rarity        | Color         | Card Placeholder |")
    print("|---------------|---------------|------------------|")
    for card in pack:
        if card["rarity"] == "Land":
            print(f"| {card['rarity']} | {card['color']} | {card['card']} |")
        else:
            print(f"| {card['rarity']} | {card['color']} | [Assign a {card['color']} {card['rarity']}] |")
    print("\n")

# Generate packs
number_of_packs = 12  # Adjust for desired number of packs
for i in range(1, number_of_packs + 1):
    generate_pack(i)