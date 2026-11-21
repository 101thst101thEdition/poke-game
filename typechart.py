#Type effectiveness dictionaries 'Attacker Type': ['Victim Type', 'Victim Type', ...]
superEffective = {
    'fire': ['grass'],
    'water': ['fire','rock'],
    'grass': ['water', 'rock','electric'],
    'electric': ['water', 'flying'],
    'rock': ['fire', 'flying'],
    'flying': ['grass'],
}
notVeryEffective = {
    'fire': ['water', 'fire', 'rock'],
    'water': ['grass', 'water'],
    'grass': ['fire', 'grass', 'flying'],
    'electric': ['grass', 'electric', 'rock'],
    'rock': ['grass'],
    'flying': ['electric', 'rock'],
    'normal': ['rock']
}