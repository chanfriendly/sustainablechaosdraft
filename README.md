# 😵‍💫 Sustainable Chaos Draft 

Here’s how you could structure your Chaos Draft plan. I’ll include clear sections, rules, and steps to randomize the packs, as well as a simple guide for implementing color and rarity tracking. This setup should give you a foundation for generating balanced packs while maintaining the chaotic spirit.

## **Chaos Draft Plan**

### **Objective**

Create a Chaos Draft experience using an existing Magic: The Gathering card pool, with each pack providing randomness, color balance, and an unpredictable feel while avoiding the structured nature of a Cube Draft.

### **Pack Construction Rules**

  

Each pack will contain:

• **1 Rare/Mythic**: Randomized by color.

• **3 Uncommons**: Randomized by color.

• **11 Commons**: Randomized by color.

• **Optional Lands**: Add 1-2 lands per pack if color fixing is desired.

  

### **Color Distribution Guidelines**

To maintain balance:

• Aim for no more than 5 cards of any single color in a pack.

• Include at least 1 card from each color in a pack (if possible).

• Multi-color, artifacts, and colorless cards can count toward any color for flexibility.


### **Step-by-Step Process**


**1. Organize the Card Pool by Theme**

• **Sort cards into themes**: Tribal (e.g., Elves, Goblins), mechanics (e.g., Morph, Flashback), or general archetypes (e.g., Control, Aggro, Ramp).

• **Separate cards by rarity**: Group them into Rare/Mythic, Uncommon, and Common piles.

**2. Randomize Themes for Each Pack**

Use a randomizer (like rolling a die or a random list generator) to pick a theme for each pack. For example:

• Roll a d6:

1 = Tribal (e.g., Elves, Goblins, or Zombies)

2 = Artifacts/Colorless

3 = Multi-Color

4 = Classic Mechanics (e.g., Morph, Flashback)

5 = Set Flavor (e.g., cards mimicking a specific set or block)

6 = Chaos (entirely random cards)

I will include a simple Python script you can execute if you'd like this to be automated.

**3. Randomize Colors for Rarity Slots**


For each rarity slot in the pack:

• Assign a color to the card using a randomizer. For example:

• Roll a d6:

• 1 = White

• 2 = Blue

• 3 = Black

• 4 = Red

• 5 = Green

• 6 = Artifact/Multicolor

• Select a card from the appropriate rarity and theme pile based on the assigned color.

  
**4. Build Each Pack**


• Combine 1 Rare/Mythic, 3 Uncommons, and 11 Commons using the colors and themes determined in the steps above.

• Check for **color balance**: Ensure no single color dominates the pack and each pack includes at least one card of each color if possible.

• Add 1-2 lands per pack for color fixing (optional).





**Randomization Tools**

  

You can automate the randomization process with:

1. **Dice Rolls**: Use dice to determine themes, colors, and rarity slots.

2. **Spreadsheet Randomizer**: Set up a spreadsheet with your card pool and use random functions to assign cards to packs. Example formulas:

• =RANDBETWEEN(1,6) to pick themes/colors.

• =INDEX(A:A, RANDBETWEEN(1, COUNTA(A:A))) to pick cards from a list.

3. **Apps**: Use random list generators like [Random.org](https://www.random.org/) or card management apps.

4. Python Randomizer:
   
	1. Download the mtgrandom.py file to your computer (Note: The base one is general cards. If you have your cards digitally organized, you can use the mtgrandom2.py file)
	2. Open Terminal or OS equivalent
	3. type "pip3 install python" to ensure you have the up to date version.
	4. type "python3", drag the file to the Terminal window (make sure it includes the .py ending) and press enter. 
	5. The script is set to return 12 packs. You can change this to your needs by opening the file and editing the bottom line:

```
# Generate packs

number_of_packs = 12 # Adjust for desired number of packs

for i in range(1, number_of_packs + 1):

generate_pack(i)
```


  

### **Optional Chaos Elements**

  
1. **Special Rules Packs**: Add unique rules to certain packs, like:

• Planeswalker Packs: Include only planeswalkers and related cards.

• Conspiracy Cards: Add cards that influence drafting mechanics.

• Vintage Chaos: Use older, less-playable cards for nostalgia.

2. **Hidden Rules**: Players don’t know the themes/colors until they draft.

  

### **How to Scale This for Larger Groups**


• If drafting with more than 8 players, expand the card pool by duplicating themes or allowing more loose randomness.

• Create extra packs and shuffle them to avoid predictability.


#mtg #magic #magicthegathering
