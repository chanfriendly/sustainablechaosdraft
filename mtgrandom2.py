import random

# Card pool configuration
card_pool = {
    "common": {
        "White": ["Card1", "Card2", "Card3"],
        "Blue": ["Card4", "Card5", "Card6"],
        "Black": ["Card7", "Card8", "Card9"],
        "Red": ["Card10", "Card11", "Card12"],
        "Green": ["Card13", "Card14", "Card15"],
        "Artifact": ["Card16", "Card17", "Card18"],
        "Multicolor": ["Card19", "Card20", "Card21"]
    },
    "uncommon": {
        "White": ["Card22", "Card23"],
        "Blue": ["Card24", "Card25"],
        "Black": ["Card26", "Card27"],
        "Red": ["Card28", "Card29"],
        "Green": ["Card30", "Card31"],
        "Artifact": ["Card32", "Card33"],
        "Multicolor": ["Card34", "Card35"]
    },
    "rare": {
        "White": ["Card36"],
        "Blue": ["Card37"],
        "Black": ["Card38"],
        "Red": ["Card39"],
        "Green": ["Card40"],
        "Artifact": ["Card41"],
        "Multicolor": ["Card42"]
    }
}

# Function to generate a random pack
def generate_pack(pack_number):
    pack = []
    rarity_slots = {
        "Rare/Mythic": 1,
        "Uncommon": 3,
        "Common": 11
    }

    # Generate cards for each rarity slot
    for rarity, count in rarity_slots.items():
        for _ in range(count):
            color = random.choice(list(card_pool[rarity.lower()].keys()))  # Pick a random color
            card = random.choice(card_pool[rarity.lower()][color])  # Pick a random card of that color
            pack.append({"rarity": rarity, "color": color, "card": card})

    # Optional: Add lands for fixing
    lands = random.choices(["Plains", "Island", "Swamp", "Mountain", "Forest"], k=random.randint(1, 2))
    for land in lands:
        pack.append({"rarity": "Land", "color": "N/A", "card": land})

    # Generate Markdown table
    print(f"### Pack {pack_number}")
    print("| Rarity        | Color         | Card           |")
    print("|---------------|---------------|----------------|")
    for slot in pack:
        print(f"| {slot['rarity']} | {slot['color']} | {slot['card']} |")
    print("\n")

# Generate packs
number_of_packs = 3  # Adjust this for the desired number of packs
for i in range(1, number_of_packs + 1):
    generate_pack(i)