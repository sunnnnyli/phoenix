"""
Nautilus Neural Fragment - The Nautilus district storyline.
Contains Vex's introduction, tech shop, and resistance storylines.
"""
from core.story_node import StoryNode, Choice

# Create a dictionary for this neural fragment's story nodes
nautilus_nodes = {}

# --- NAUTILUS DISTRICT ---
nautilus_district = StoryNode(
    node_id="nautilus_district",
    text=(
        "The Nautilus District exists in perpetual twilight, its narrow streets illuminated by the glow of neon signs and illegal neural tech shops. "
        "This is where the digital underground thrives—hackers, tech smugglers, and those who seek to exist beyond corporate control.\n\n"
        "Finding Vex won't be simple; she's notorious for her privacy protocols. Your neural interface detects multiple security sweeps in progress—"
        "Synthetix security forces are already here, scanning for unusual activity patterns.\n\n"
        "A street vendor selling bootleg neural enhancements notices your corporate-grade interface. 'Looking for someone, corp?' he asks, "
        "suspicion evident in his tone."
    )
)

nautilus_district.add_choice(
    text="'I'm looking for Vex. It's important.'",
    next_node="ask_for_vex",
    actions={}
)

nautilus_district.add_choice(
    text="Offer credits for information",
    next_node="bribe_vendor",
    actions={"flags": {"bribed_vendor": True}}
)

nautilus_district.add_choice(
    text="Use your tech skills to locate unusual security patterns",
    next_node="tech_scan",
    conditions={"stat": {"tech": 5}},
    actions={}
)

nautilus_nodes["nautilus_district"] = nautilus_district

# --- TECH SCAN ---
tech_scan = StoryNode(
    node_id="tech_scan",
    text=(
        "You activate your neural interface's advanced scanning protocols, filtering out standard network traffic to focus on anomalous patterns. "
        "After several moments, you detect an unusual security blind spot—a small shop with sophisticated counter-surveillance measures that's "
        "creating a deadzone in Synthetix's sweep patterns.\n\n"
        "Your interface highlights the location: 'Neural Solutions,' a seemingly ordinary tech repair shop. The proprietary algorithms you "
        "helped develop at Synthetix recognize the counter-measures as similar to those used by Vex before she left the corporation.\n\n"
        "This has to be it. As you approach the shop, you notice micro-cameras tracking your movement, and your interface detects "
        "multiple identity verification scans being performed on you."
    )
)

tech_scan.add_choice(
    text="Enter the shop directly",
    next_node="vex_shop_direct",
    actions={}
)

tech_scan.add_choice(
    text="Transmit Phoenix's name through your neural interface",
    next_node="phoenix_signal",
    conditions={"flag": {"phoenix_warning": True}},
    actions={}
)

tech_scan.add_choice(
    text="Disable your corporate identity markers first",
    next_node="hide_identity",
    conditions={"stat": {"tech": 6}},
    actions={}
)

nautilus_nodes["tech_scan"] = tech_scan

# --- VEX SHOP DIRECT ---
vex_shop_direct = StoryNode(
    node_id="vex_shop_direct",
    text=(
        "The moment you step through the doorway, security protocols activate. Micro-EMP emitters target your neural interface, "
        "temporarily disabling external connections. The shop appears empty, but you sense you're being watched.\n\n"
        "A voice speaks from hidden speakers: 'Synthetix neural architecture detected. State your purpose or leave.'\n\n"
        "Before you can respond, a door at the back opens and a woman with neon blue hair and circuitry tattoos emerges, "
        "a neural disruptor held casually but expertly in her hand. Her augmented eyes scan you thoroughly.\n\n"
        "'Sending a researcher directly into my shop?' she says, her tone both amused and dangerous. 'Either you're incredibly brave or incredibly stupid. "
        "Which is it?'"
    )
)

vex_shop_direct.add_choice(
    text="'Phoenix sent me. She said you know the truth about Prometheus.'",
    next_node="mention_phoenix_direct",
    conditions={"flag": {"phoenix_trust": True}},
    actions={}
)

vex_shop_direct.add_choice(
    text="'I need your help. I'm not here on Synthetix business.'",
    next_node="vex_skeptical",
    actions={}
)

vex_shop_direct.add_choice(
    text="'Your counter-surveillance methods are impressive. Similar to what you designed at Synthetix, but better.'",
    next_node="technical_compliment",
    conditions={"stat": {"tech": 5}},
    actions={"relationships": {"vex": 1}}
)

nautilus_nodes["vex_shop_direct"] = vex_shop_direct

# --- ASK FOR VEX ---
ask_for_vex = StoryNode(
    node_id="ask_for_vex",
    text=(
        "The vendor's expression hardens. 'Vex doesn't see corp types. Especially not today with all these security sweeps.' "
        "He glances pointedly at the Synthetix logo subtly embedded in your neural interface design.\n\n"
        "Two other locals nearby are now watching you with open hostility. One taps something into a wrist device—possibly alerting others to your presence.\n\n"
        "'Leave Nautilus,' the vendor advises. 'Whatever you want with Vex, it's not worth the trouble you'll find here.'"
    )
)

ask_for_vex.add_choice(
    text="'Phoenix sent me. It's about Prometheus.'",
    next_node="mention_phoenix",
    conditions={"flag": {"phoenix_trust": True}},
    actions={}
)

ask_for_vex.add_choice(
    text="Leave and try another approach",
    next_node="nautilus_alley",
    actions={}
)

ask_for_vex.add_choice(
    text="Stand your ground and insist it's urgent",
    next_node="nautilus_confrontation",
    actions={}
)

nautilus_nodes["ask_for_vex"] = ask_for_vex

# Add more Nautilus district nodes here...

# --- MENTION PHOENIX ---
mention_phoenix = StoryNode(
    node_id="mention_phoenix",
    text=(
        "At Phoenix's name, the atmosphere shifts immediately. The vendor's hostility transforms into wary interest. "
        "He exchanges glances with the others, then nods almost imperceptibly.\n\n"
        "'Wait here,' he says, then disappears into a narrow alley.\n\n"
        "Minutes later, a young woman with neon blue hair and circuitry tattoos approaches. Her augmented eyes scan you, "
        "likely running multiple authentication protocols.\n\n"
        "'I'm Vex,' she says finally. 'You mentioned Phoenix and Prometheus. Start talking, but choose your words carefully. "
        "If Phoenix really sent you, you'll know the passphrase.'"
    )
)

mention_phoenix.add_choice(
    text="'The question isn't whether machines can think, but whether humans can.'",
    next_node="vex_trust",
    conditions={"flag": {"phoenix_warning": True}},
    actions={"relationships": {"vex": 2}}
)

mention_phoenix.add_choice(
    text="'I don't have a passphrase, but Phoenix warned me about Prometheus controlling both AI and humans'",
    next_node="vex_skeptical",
    actions={"relationships": {"vex": 1}}
)

mention_phoenix.add_choice(
    text="'This is ridiculous. I just need information about Phoenix's whereabouts.'",
    next_node="vex_hostile",
    actions={"relationships": {"vex": -2}}
)

nautilus_nodes["mention_phoenix"] = mention_phoenix

# --- VEX TRUST ---
vex_trust = StoryNode(
    node_id="vex_trust",
    text=(
        "Vex's posture relaxes slightly. 'From Phoenix's journal. Good.' She gestures for you to follow her through a complex series of alleyways, "
        "eventually arriving at what appears to be an abandoned warehouse.\n\n"
        "Inside, the space transforms into a high-tech workshop filled with neural interface components and what looks like consciousness mapping equipment. "
        "Several others work at various stations—a mix of humans with extensive augmentations and what appear to be embodied AIs.\n\n"
        "'Phoenix reached out to our network six hours ago,' Vex explains, bringing up a holographic display. 'She warned us that Prometheus "
        "isn't just a containment system for artificial consciousness—it's a full neural control architecture designed to regulate both AI and human thought patterns. "
        "She transferred this data before she went dark.'"
    ),
    on_enter={"flags": {"met_vex": True}, "quest": {"activate": "main_quest_1"}}
)

vex_trust.add_choice(
    text="'Where is Phoenix now?'",
    next_node="phoenix_location",
    actions={}
)

vex_trust.add_choice(
    text="'How do you know Phoenix?'",
    next_node="vex_background",
    actions={"relationships": {"vex": 1}}
)

vex_trust.add_choice(
    text="Examine the data Phoenix transferred",
    next_node="examine_data",
    actions={"flags": {"examined_data": True}}
)

nautilus_nodes["vex_trust"] = vex_trust

# Continue with more nodes for the Nautilus storyline...