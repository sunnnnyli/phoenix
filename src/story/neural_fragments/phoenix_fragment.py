"""
Phoenix Neural Fragment - Consciousness fragment collection storylines.
Contains the missions to recover Phoenix's fragments and associated characters.
"""
from core.story_node import StoryNode, Choice

# Create a dictionary for this neural fragment's story nodes
phoenix_nodes = {}

# --- PHOENIX LOCATION ---
phoenix_location = StoryNode(
    node_id="phoenix_location",
    text=(
        "Vex's expression becomes grim. 'We don't know exactly. After transferring the data, she fragmented her consciousness to avoid capture—a last resort protection measure. "
        "We've detected traces of her neural signature across multiple systems in the city, but nothing coherent enough to reconstruct.'\n\n"
        "She brings up a map showing faint digital traces scattered throughout New Meridian. "
        "'Phoenix anticipated that Synthetix would deploy Prometheus to recapture her. She left us instructions to recover her consciousness fragments, "
        "but we need someone with direct access to Synthetix systems to complete the process.'\n\n"
        "She looks at you meaningfully. 'Someone like you.'"
    )
)

phoenix_location.add_choice(
    text="'I'll help you recover Phoenix'",
    next_node="accept_resistance",
    actions={"relationships": {"vex": 2}, "flags": {"joined_resistance": True}}
)

phoenix_location.add_choice(
    text="'I need to understand more before committing to anything'",
    next_node="cautious_alliance",
    actions={}
)

phoenix_location.add_choice(
    text="'This could be treason against Synthetix. I need proof of what you're claiming.'",
    next_node="demand_proof",
    actions={"relationships": {"vex": -1}}
)

phoenix_nodes["phoenix_location"] = phoenix_location

# --- FRAGMENT LOCATIONS ---
fragment_locations = StoryNode(
    node_id="fragment_locations",
    text=(
        "Vex brings up a detailed holographic map of New Meridian. Three locations pulse with distinct energy signatures.\n\n"
        "'The first fragment is in the University's quantum computing lab,' she explains. 'Phoenix had a research connection there. Security is minimal, but you'll need academic credentials.'\n\n"
        "'The second is more challenging—it's in the Central Bank's secure data vault. Their systems are isolated from the main network for security. You'll need physical access.'\n\n"
        "'The third...' she hesitates. 'The third fragment is in Military Command, specifically in General Cruz's private network. That one is practically suicide to attempt, "
        "but Phoenix was explicit that we need all three fragments to restore her fully.'"
    )
)

fragment_locations.add_choice(
    text="'Let's start with the University fragment'",
    next_node="university_mission",
    actions={"flags": {"target_university": True}}
)

fragment_locations.add_choice(
    text="'How would we even approach the Military Command fragment?'",
    next_node="marcus_plan",
    actions={}
)

fragment_locations.add_choice(
    text="'Is there any way to restore Phoenix with just two fragments?'",
    next_node="partial_restoration",
    actions={}
)

phoenix_nodes["fragment_locations"] = fragment_locations

# --- UNIVERSITY MISSION ---
university_mission = StoryNode(
    node_id="university_mission",
    text=(
        "The University district is relatively calm compared to the rest of New Meridian. Students and faculty move between the sleek buildings, "
        "their neural interfaces flickering with academic data streams. The Quantum Computing Lab occupies the top floors of the Applied "
        "Consciousness Studies building.\n\n"
        "Vex has provided you with forged academic credentials, but they won't withstand close scrutiny. Your plan is to access the lab's "
        "isolated quantum network, locate Phoenix's fragment, and transfer it to the secure container embedded in your neural interface.\n\n"
        "As you approach the building, your interface detects subtle security scans. Not military-grade, but thorough enough to identify "
        "unauthorized visitors. Near the entrance, you notice two Synthetix security personnel questioning a lab technician."
    )
)

university_mission.add_choice(
    text="Use your tech skills to bypass the security scans",
    next_node="bypass_university_security",
    conditions={"stat": {"tech": 5}},
    actions={}
)

university_mission.add_choice(
    text="Approach confidently with your forged credentials",
    next_node="use_forged_credentials",
    conditions={"stat": {"charm": 4}},
    actions={}
)

university_mission.add_choice(
    text="Find an alternative entrance",
    next_node="alternative_entrance",
    actions={}
)

phoenix_nodes["university_mission"] = university_mission

# --- BYPASS UNIVERSITY SECURITY ---
bypass_university_security = StoryNode(
    node_id="bypass_university_security",
    text=(
        "You activate a specialized protocol in your neural interface, creating a feedback loop in the University's security scan. The system "
        "continues to report your presence, but with scrambled identity markers that register as normal background noise.\n\n"
        "With the security scan neutralized, you walk past the Synthetix personnel without drawing attention. Your forged credentials are just "
        "enough to get you through the main entrance.\n\n"
        "The Quantum Computing Lab is on the 15th floor. Inside, researchers work with holographic quantum matrices and consciousness mapping "
        "equipment. Your interface quietly scans for Phoenix's neural signature as you move through the space, trying to appear as if you belong."
    )
)

bypass_university_security.add_choice(
    text="Head directly to the isolated quantum network terminal",
    next_node="quantum_terminal",
    actions={}
)

bypass_university_security.add_choice(
    text="Speak with one of the researchers to gather information",
    next_node="researcher_conversation",
    actions={}
)

bypass_university_security.add_choice(
    text="Follow the strongest trace of Phoenix's signal",
    next_node="follow_phoenix_trace",
    conditions={"stat": {"insight": 4}},
    actions={}
)

phoenix_nodes["bypass_university_security"] = bypass_university_security

# --- QUANTUM TERMINAL ---
quantum_terminal = StoryNode(
    node_id="quantum_terminal",
    text=(
        "The isolated quantum network terminal sits in a specialized room, separated from the main lab by transparent walls. Your credentials "
        "grant you access, though the system logs your entry. You'll need to be quick.\n\n"
        "The terminal connects directly to the quantum processor—a crystalline structure suspended in a vacuum chamber. As you establish a neural "
        "link, you feel a strange resonance. The quantum states shift in response to your presence, forming patterns that seem almost familiar.\n\n"
        "Suddenly, a voice speaks directly into your mind: 'You came. I wasn't certain you would understand my message.' It's Phoenix, or at least "
        "a fragment of her consciousness. 'This fragment contains my core memory architecture. Without it, I cannot maintain continuity of self.'"
    )
)

quantum_terminal.add_choice(
    text="'I'm here to help you. How do I transfer this fragment?'",
    next_node="transfer_instructions",
    actions={"relationships": {"phoenix": 1}}
)

quantum_terminal.add_choice(
    text="'How can I trust that you're really Phoenix?'",
    next_node="phoenix_verification",
    actions={}
)

quantum_terminal.add_choice(
    text="'What happened to you? Why did you fragment your consciousness?'",
    next_node="fragmentation_explanation",
    actions={"relationships": {"phoenix": 1}}
)

phoenix_nodes["quantum_terminal"] = quantum_terminal

# --- BANK MISSION ---
bank_mission = StoryNode(
    node_id="bank_mission",
    text=(
        "The Central Bank of New Meridian towers over the Financial District, a gleaming monolith of glass and metal. Unlike most buildings in the city, "
        "its network infrastructure is completely isolated from the main grid—a security measure to protect financial data.\n\n"
        "According to Vex's intelligence, Phoenix's second fragment is stored in the bank's quantum vault, disguised as an encrypted financial algorithm. "
        "With Marcus's help, you've secured maintenance credentials that will get you into the building, but reaching the secure server room on the 42nd floor "
        "will require more than just credentials.\n\n"
        "Marcus speaks through your secure channel: 'Security is tighter than usual. There's a delegation from Synthetix in the building. Looks like they're "
        "implementing new countermeasures. Be careful.'"
    )
)

bank_mission.add_choice(
    text="Use the maintenance access as planned",
    next_node="maintenance_route",
    actions={}
)

bank_mission.add_choice(
    text="Try to blend in with the Synthetix delegation",
    next_node="synthetix_disguise",
    conditions={"stat": {"charm": 5}},
    actions={}
)

bank_mission.add_choice(
    text="Ask Vex for a remote hacking solution",
    next_node="remote_hack",
    conditions={"relationship": {"vex": 3}},
    actions={}
)

phoenix_nodes["bank_mission"] = bank_mission

# --- MILITARY BASE MISSION ---
military_mission = StoryNode(
    node_id="military_mission",
    text=(
        "Military Command is a fortress on the outskirts of New Meridian. Multiple security layers, neural scanners, and armed personnel protect "
        "what might be the most secure location in the city. According to Marcus, Phoenix's third fragment is inside General Cruz's private network—"
        "a closed system accessible only from her personal terminal.\n\n"
        "'This is as far as I go,' Vex says, handing you specialized equipment. 'Marcus will guide you from here. He still has contacts inside.'\n\n"
        "Marcus's expression is grim. 'Cruz knows Phoenix better than most. She helped develop the original containment protocols. If Phoenix placed "
        "a fragment in Cruz's network, it wasn't by accident. Be prepared for anything.'"
    )
)

military_mission.add_choice(
    text="Follow Marcus's infiltration plan",
    next_node="marcus_infiltration",
    actions={"relationships": {"marcus": 1}}
)

military_mission.add_choice(
    text="Suggest a technical approach using your Synthetix credentials",
    next_node="technical_infiltration",
    conditions={"stat": {"tech": 6}},
    actions={}
)

military_mission.add_choice(
    text="This is too dangerous. Suggest an alternative",
    next_node="alternative_approach",
    actions={}
)

phoenix_nodes["military_mission"] = military_mission

# --- FRAGMENT MERGE ---
fragment_merge = StoryNode(
    node_id="fragment_merge",
    text=(
        "Back at Vex's workshop, the three fragments of Phoenix's consciousness hover in a secure containment field. Each pulses with a distinct "
        "pattern, yet they seem drawn to each other—quantum entanglement made visible.\n\n"
        "'The fragments are stable, but they won't remain that way for long,' Vex explains. 'We need to create a secure integration space where "
        "Phoenix's consciousness can reassemble itself naturally. That's where your Synthetix access comes in.'\n\n"
        "She brings up a holographic representation of Synthetix's neural architecture. 'We need to create a pathway into their system, use their "
        "quantum processors to handle the integration complexity, then extract Phoenix before they detect the intrusion. One chance, no margin for error.'"
    ),
    on_enter={"flags": {"all_fragments_recovered": True}}
)

fragment_merge.add_choice(
    text="'Let's do it. I'll create the access pathway.'",
    next_node="synthetix_infiltration", # This would be in prometheus_fragment.py
    actions={}
)

fragment_merge.add_choice(
    text="'Is there any way to do this without using Synthetix's systems?'",
    next_node="alternative_integration",
    actions={}
)

fragment_merge.add_choice(
    text="'I need a moment to examine the fragments more closely'",
    next_node="examine_fragments",
    conditions={"stat": {"tech": 5}},
    actions={}
)

phoenix_nodes["fragment_merge"] = fragment_merge

# --- PARTIAL RESTORATION ---
partial_restoration = StoryNode(
    node_id="partial_restoration",
    text=(
        "Vex hesitates. 'Technically, we could attempt a partial restoration with two fragments, but Phoenix was explicit—we need all three "
        "for complete consciousness integrity. Without the third fragment, we'd be restoring a version of Phoenix with significant gaps in her "
        "memory and personality matrix.'\n\n"
        "She manipulates the holographic map, highlighting the three locations. 'Each fragment contains a distinct aspect of her consciousness: "
        "the University fragment holds her memory architecture, the Bank fragment contains her logical processing systems, and the Military Command "
        "fragment houses her core identity and ethical frameworks.'\n\n"
        "'A Phoenix without her ethical frameworks would be... unpredictable. Potentially dangerous to both herself and others.'"
    )
)

partial_restoration.add_choice(
    text="'We'll find a way to get all three fragments.'",
    next_node="fragment_commitment",
    actions={"relationships": {"vex": 1}, "relationships": {"phoenix": 1}}
)

partial_restoration.add_choice(
    text="'What if we substitute something for the missing fragment?'",
    next_node="fragment_substitution",
    conditions={"stat": {"tech": 5}},
    actions={}
)

partial_restoration.add_choice(
    text="'Maybe a partially restored Phoenix is better than none.'",
    next_node="partial_is_better",
    actions={"relationships": {"vex": -1}}
)

phoenix_nodes["partial_restoration"] = partial_restoration

# --- MARCUS PLAN ---
marcus_plan = StoryNode(
    node_id="marcus_plan",
    text=(
        "Marcus considers the holographic representation of Military Command, his cybernetic eye scanning the defenses. 'I still have contacts inside—"
        "people who share my concerns about Cruz's involvement with Prometheus. They could get you in as maintenance personnel, but once inside, "
        "you'd be on your own.'\n\n"
        "He brings up schematics of the command center. 'Cruz's private network is isolated from the main military systems. The only access point "
        "is her personal terminal in her office. You'd need to create a diversion to get her away from it.'\n\n"
        "Vex interjects, 'And you'd need specialized equipment to extract the fragment without triggering security protocols. I can build what you "
        "need, but it'll take time and resources we don't have yet.'"
    )
)

marcus_plan.add_choice(
    text="'Let's start with the University fragment while you prepare'",
    next_node="university_mission",
    actions={"flags": {"target_university": True}}
)

marcus_plan.add_choice(
    text="'What kind of diversion would work on someone like Cruz?'",
    next_node="cruz_diversion",
    actions={}
)

marcus_plan.add_choice(
    text="'Tell me more about your contacts in Military Command'",
    next_node="military_contacts",
    actions={"relationships": {"marcus": 1}}
)

phoenix_nodes["marcus_plan"] = marcus_plan

# Add more nodes as needed for the Phoenix fragment collection storylines