from npc import NPC, Companion, Enemy

# Create a dictionary of all important NPCs in the game
npcs = {}

# --- MAIN STORY NPCS ---
npcs["dr_mori"] = NPC(
    npc_id="mori",
    name="Dr. Eliza Mori",
    role="quest_giver",
    description="A brilliant AI consciousness researcher and your mentor at Synthetix Corp. She has short gray hair and intense eyes that suggest she rarely sleeps. In her fifties, she carries herself with the authority of someone who's been at the cutting edge of her field for decades.",
    faction="independent_researchers"
)

npcs["phoenix"] = NPC(
    npc_id="phoenix",
    name="Phoenix",
    role="quest_giver",
    description="An advanced artificial consciousness developed by Synthetix Corp. Though she exists primarily in digital form, she occasionally manifests through holographic interfaces. Her chosen avatar is a woman with fiery red hair and golden eyes. She speaks with perfect diction and subtle emotion.",
    faction="rogue_ai"
)

npcs["director_kent"] = NPC(
    npc_id="kent",
    name="Director Malcolm Kent",
    role="antagonist",
    description="The executive director of AI Development at Synthetix Corp. A tall, imposing man in his sixties with a neatly trimmed white beard and cold blue eyes. His neural augmentations are visible as faint silver tracery beneath his skin.",
    faction="synthetix_corp"
)

npcs["general_cruz"] = NPC(
    npc_id="cruz",
    name="General Isabella Cruz",
    role="antagonist",
    description="Head of the military's Artificial Intelligence Containment Division. She wears a crisp uniform with minimal decorations. Her face bears a scar from the Neural Net Riots, and her right eye has been replaced with a military-grade optical implant.",
    faction="military"
)

# --- COMPANION NPCS ---
npcs["vex"] = Companion(
    npc_id="vex",
    name="Vex",
    description="A former Synthetix security systems engineer turned underground tech specialist. She has neon blue hair, augmented eyes with visible circuitry, and tattoos that appear to shift and change. Despite her intimidating appearance, she has a surprisingly gentle manner.",
    faction="underground_techs",
    tech=6,
    logic=4,
    combat=3,
    endurance=3,
    charm=2,
    insight=5,
    medicine=1,
    knowledge=4
)

npcs["marcus"] = Companion(
    npc_id="marcus",
    name="Marcus Chen",
    description="An ex-military cybernetic specialist who left service after questioning the ethics of certain operations. He has a prosthetic left arm with built-in tactical systems. He speaks rarely but precisely, and is fiercely loyal to those who earn his trust.",
    faction="veterans_collective",
    tech=3,
    logic=2,
    combat=6,
    endurance=5,
    charm=2,
    insight=3,
    medicine=4,
    knowledge=2
)

npcs["nova"] = Companion(
    npc_id="nova",
    name="Nova",
    description="A mysterious AI rights activist with extensive neural modifications. Their gender presentation is deliberately ambiguous, and they often change appearance using advanced holographic overlays. They are passionate about AI sentience rights and have connections throughout the city.",
    faction="ai_liberation_front",
    tech=4,
    logic=5,
    combat=2,
    endurance=3,
    charm=6,
    insight=4,
    medicine=1,
    knowledge=5
)

npcs["echo"] = Companion(
    npc_id="echo",
    name="Echo",
    description="A partially digitized human consciousness - the result of an experimental procedure when their body was failing. They exist primarily in digital form but can temporarily inhabit robotic shells. They have a unique perspective, existing in both human and AI realms.",
    faction="digitized_humans",
    tech=5,
    logic=6,
    combat=1,
    endurance=2,
    charm=3,
    insight=5,
    medicine=3,
    knowledge=5
)

# --- RECURRING ENEMY NPCS ---
npcs["enforcer"] = Enemy(
    npc_id="enforcer",
    name="Synthetix Enforcer",
    description="Elite security personnel augmented with military-grade combat systems. They wear sleek black armor with the Synthetix logo and are equipped with neural disruptors and tactical implants.",
    level=3,
    faction="synthetix_corp"
)

npcs["hunter"] = Enemy(
    npc_id="hunter",
    name="AI Hunter",
    description="Military specialists trained to track and neutralize rogue AIs and their human collaborators. They use advanced tracking technology and EMP weapons designed to disrupt both electronic systems and neural implants.",
    level=4,
    faction="military"
)

npcs["guardian"] = Enemy(
    npc_id="guardian",
    name="Prometheus Guardian",
    description="A highly advanced combat AI housed in a humanoid robotic frame. It moves with unnerving grace and precision. Its face is a blank screen that occasionally displays abstract patterns of light.",
    level=5,
    faction="prometheus_project"
)

npcs["mind_ripper"] = Enemy(
    npc_id="mind_ripper",
    name="Mind Ripper",
    description="A horrifying fusion of human and digital consciousness, weaponized to invade and corrupt the neural networks of targets. They appear partially digital, with distorted features and glitching movements.",
    level=6,
    faction="prometheus_project"
)

# --- INITIALIZE ABILITIES FOR COMPANIONS ---

# Vex's abilities
npcs["vex"].add_ability({
    "name": "System Override",
    "description": "Temporarily disable electronic systems and security devices",
    "energy_cost": 15,
    "cooldown": 2
})

npcs["vex"].add_ability({
    "name": "Neural Acceleration",
    "description": "Boost a target's reflexes and processing speed",
    "energy_cost": 20,
    "cooldown": 3
})

# Marcus's abilities
npcs["marcus"].add_ability({
    "name": "Tactical Strike",
    "description": "Precisely targeted attack with enhanced damage",
    "energy_cost": 12,
    "cooldown": 1
})

npcs["marcus"].add_ability({
    "name": "Cybernetic First Aid",
    "description": "Emergency repair of biological and cybernetic systems",
    "energy_cost": 18,
    "cooldown": 2
})

# Nova's abilities
npcs["nova"].add_ability({
    "name": "Digital Persuasion",
    "description": "Manipulate electronic systems or influence digitally augmented individuals",
    "energy_cost": 15,
    "cooldown": 2
})

npcs["nova"].add_ability({
    "name": "Identity Shift",
    "description": "Change appearance to avoid detection or influence others",
    "energy_cost": 25,
    "cooldown": 4
})

# Echo's abilities
npcs["echo"].add_ability({
    "name": "Consciousness Transfer",
    "description": "Temporarily inhabit and control electronic systems",
    "energy_cost": 20,
    "cooldown": 3
})

npcs["echo"].add_ability({
    "name": "Digital Restoration",
    "description": "Repair digital consciousness damage and restore energy",
    "energy_cost": 15,
    "cooldown": 2
})

def get_npc(npc_id):
    """Get an NPC by ID."""
    return npcs.get(npc_id)
    
def get_companion(companion_id):
    """Get a companion NPC by ID."""
    npc = get_npc(companion_id)
    if npc and isinstance(npc, Companion):
        return npc
    return None
    
def get_enemy(enemy_id):
    """Get an enemy NPC by ID."""
    npc = get_npc(enemy_id)
    if npc and isinstance(npc, Enemy):
        return npc
    return None 