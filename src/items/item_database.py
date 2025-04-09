from .item import Item, Weapon, Armor, Consumable, KeyItem, ImplantItem

# Create a dictionary of all items in the game
items = {}

# --- WEAPONS ---
items["pulse_pistol"] = Weapon(
    item_id="pulse_pistol",
    name="Pulse Pistol",
    description="Standard-issue energy pistol with moderate damage.",
    value=50,
    damage=10,
    critical_chance=0.05,
    rarity="common"
)

items["neural_disruptor"] = Weapon(
    item_id="neural_disruptor",
    name="Neural Disruptor",
    description="Specialized weapon that deals extra damage to synthetic enemies.",
    value=150,
    damage=15,
    critical_chance=0.08,
    rarity="uncommon"
)

items["quantum_rifle"] = Weapon(
    item_id="quantum_rifle",
    name="Quantum Rifle",
    description="Advanced rifle that destabilizes molecular bonds. High damage but slow.",
    value=300,
    damage=25,
    critical_chance=0.1,
    rarity="rare"
)

items["cortex_blade"] = Weapon(
    item_id="cortex_blade",
    name="Cortex Blade",
    description="A razor-sharp blade infused with neural-dampening nanites.",
    value=200,
    damage=18,
    critical_chance=0.15,
    rarity="uncommon"
)

items["consciousness_spike"] = Weapon(
    item_id="consciousness_spike",
    name="Consciousness Spike",
    description="Legendary weapon that can disrupt AI consciousness patterns.",
    value=800,
    damage=35,
    critical_chance=0.2,
    rarity="legendary"
)

# --- ARMOR ---
items["combat_exoskin"] = Armor(
    item_id="combat_exoskin",
    name="Combat Exoskin",
    description="Standard protective layer that absorbs physical damage.",
    value=80,
    defense=5,
    rarity="common"
)

items["firewall_mesh"] = Armor(
    item_id="firewall_mesh",
    name="Firewall Mesh",
    description="Digital defense system that protects against cyber attacks.",
    value=120,
    defense=3,
    tech_defense=8,
    rarity="uncommon"
)

items["quantum_shield"] = Armor(
    item_id="quantum_shield",
    name="Quantum Shield Generator",
    description="Creates a probability field that reduces incoming damage.",
    value=350,
    defense=12,
    tech_defense=10,
    rarity="rare"
)

items["neural_lattice"] = Armor(
    item_id="neural_lattice",
    name="Neural Lattice",
    description="A highly advanced consciousness protection system.",
    value=700,
    defense=18,
    tech_defense=20,
    rarity="epic"
)

# --- CONSUMABLES ---
items["nanite_injector"] = Consumable(
    item_id="nanite_injector",
    name="Nanite Injector",
    description="Releases healing nanobots that repair physical damage.",
    value=25,
    effect_type="heal",
    effect_value=30,
    rarity="common"
)

items["energy_cell"] = Consumable(
    item_id="energy_cell",
    name="Energy Cell",
    description="Restores energy for tech abilities and implants.",
    value=20,
    effect_type="energy",
    effect_value=25,
    rarity="common"
)

items["cognitive_enhancer"] = Consumable(
    item_id="cognitive_enhancer",
    name="Cognitive Enhancer",
    description="Temporarily boosts all mental attributes.",
    value=40,
    effect_type="buff",
    effect_value={"logic": 2, "insight": 2, "tech": 2},
    rarity="uncommon"
)

items["combat_stimulant"] = Consumable(
    item_id="combat_stimulant",
    name="Combat Stimulant",
    description="Temporarily boosts all physical attributes.",
    value=40,
    effect_type="buff",
    effect_value={"combat": 2, "endurance": 2},
    rarity="uncommon"
)

items["full_repair_kit"] = Consumable(
    item_id="full_repair_kit",
    name="Full Repair Kit",
    description="Completely restores health and removes negative effects.",
    value=100,
    effect_type="heal",
    effect_value=999,  # Full heal
    rarity="rare"
)

# --- KEY ITEMS ---
items["data_chip"] = KeyItem(
    item_id="data_chip",
    name="Phoenix's Data Chip",
    description="A small encrypted data chip containing information Phoenix wanted to share. It interfaces directly with your neural implant.",
    quest_id="main_quest_1"
)

items["ai_core_fragment"] = KeyItem(
    item_id="ai_core_fragment",
    name="AI Core Fragment",
    description="A fragment of a highly advanced AI consciousness core. Its purpose is unknown.",
    quest_id="main_quest_1"
)

items["cipher_key"] = KeyItem(
    item_id="cipher_key",
    name="Cipher Key",
    description="A complex decryption key that can unlock secure AI systems.",
    quest_id="main_quest_2"
)

items["consciousness_matrix"] = KeyItem(
    item_id="consciousness_matrix",
    name="Consciousness Matrix",
    description="An ethereal digital construct that bridges human and AI understanding.",
    quest_id="main_quest_3"
)

# --- IMPLANTS ---
items["neural_processor"] = ImplantItem(
    item_id="neural_processor",
    name="Neural Processor",
    description="Enhances cognitive functions and logical reasoning.",
    value=200,
    stat_bonuses={"logic": 2, "tech": 1},
    rarity="uncommon"
)

items["reflex_enhancer"] = ImplantItem(
    item_id="reflex_enhancer",
    name="Reflex Enhancer",
    description="Improves combat reflexes and coordination.",
    value=200,
    stat_bonuses={"combat": 2, "initiative": 1},
    rarity="uncommon"
)

items["empathy_module"] = ImplantItem(
    item_id="empathy_module",
    name="Empathy Module",
    description="Enhances ability to understand and connect with others.",
    value=250,
    stat_bonuses={"charm": 2, "insight": 2},
    rarity="rare"
)

items["resilience_frame"] = ImplantItem(
    item_id="resilience_frame",
    name="Resilience Frame",
    description="Reinforces the body to withstand more damage.",
    value=200,
    stat_bonuses={"endurance": 3},
    rarity="uncommon"
)

items["omniscient_cortex"] = ImplantItem(
    item_id="omniscient_cortex",
    name="Omniscient Cortex",
    description="Legendary implant that enhances all mental abilities significantly.",
    value=800,
    stat_bonuses={"logic": 3, "tech": 3, "insight": 3, "knowledge": 3},
    rarity="legendary"
)

def get_item(item_id):
    """Get an item by its ID."""
    return items.get(item_id)
    
def get_items_by_type(item_type):
    """Get all items of a specific type."""
    return [item for item in items.values() if item.item_type == item_type]
    
def get_items_by_rarity(rarity):
    """Get all items of a specific rarity."""
    return [item for item in items.values() if item.rarity == rarity] 