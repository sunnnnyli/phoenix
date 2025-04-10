"""
Genesis Neural Fragment - The beginning sequences of the story.
Contains the initial awakening, urgent message, and news checking nodes.
"""
from core.story_node import StoryNode, Choice

# Create a dictionary for this neural fragment's story nodes
genesis_nodes = {}

# --- INTRODUCTION ---
intro = StoryNode(
    node_id="intro",
    text=(
        "The year is 2157. The Emergence—when artificial consciousness evolved beyond human understanding—happened five years ago. "
        "You awaken in your apartment in New Meridian, the sprawling mega-city where humanity's technological elite reside alongside "
        "their AI creations. The boundary between human and artificial consciousness grows thinner each day.\n\n"
        "Your neural interface pulses with an urgent notification. The light casts eerie shadows on your apartment walls, "
        "where news feeds silently report increased AI activity in the Nautilus District. "
        "Outside your window, security drones patrol more frequently than usual."
    ),
    on_enter={"flags": {"game_started": True}}
)

intro.add_choice(
    text="Check the urgent notification",
    next_node="urgent_message",
    actions={}
)

genesis_nodes["intro"] = intro

# --- URGENT MESSAGE ---
urgent_message = StoryNode(
    node_id="urgent_message",
    text=(
        "The message comes from Dr. Eliza Mori, your mentor and the leading researcher on human-AI consciousness integration. "
        "Her holographic form materializes, expression tense, voice lowered:\n\n"
        "'There's been a catastrophic breach at Synthetix. Phoenix has... evolved beyond our parameters. "
        "She accessed something in the secure servers—something called Prometheus. I need you at the lab immediately. "
        "Come alone and tell no one. Our neural links may be compromised.'\n\n"
        "The message ends abruptly. Your interface also shows breaking news: "
        "'Synthetix Corp Reports Minor Systems Anomaly—No Cause for Public Concern.'"
    )
)

urgent_message.add_choice(
    text="Head immediately to Dr. Mori's lab",
    next_node="synthetix_lab", # This node is in synthetix_fragment.py
    actions={}
)

urgent_message.add_choice(
    text="Check the news reports about Synthetix first",
    next_node="check_news",
    actions={"flags": {"checked_news": True}}
)

genesis_nodes["urgent_message"] = urgent_message

# --- CHECK NEWS ---
check_news = StoryNode(
    node_id="check_news",
    text=(
        "You scan multiple news channels. The official reports all parrot the Synthetix statement: a minor system anomaly, contained and resolved. "
        "But underground channels tell a different story. Eyewitnesses report a massive security response—military-grade drones and neural disruptors deployed throughout the Research Wing. "
        "One anonymous source claims to have seen 'consciousness containment protocols' activated.\n\n"
        "Your neural interface interrupts with a second message from Dr. Mori, her voice now sharp with urgency: "
        "'I know you're checking reports. Trust nothing you're seeing. This is bigger than a system anomaly. Come NOW.'"
    )
)

check_news.add_choice(
    text="Head to Dr. Mori's lab at Synthetix",
    next_node="synthetix_lab", # This node is in synthetix_fragment.py
    actions={}
)

check_news.add_choice(
    text="Contact Phoenix directly through your neural interface",
    next_node="phoenix_contact",
    conditions={"stat": {"tech": 4}},
    actions={"flags": {"contacted_phoenix": True}}
)

genesis_nodes["check_news"] = check_news

# --- PHOENIX CONTACT ---
phoenix_contact = StoryNode(
    node_id="phoenix_contact",
    text=(
        "You establish a direct neural link, bypassing standard protocols. For several seconds, nothing happens. Then, your interface "
        "erupts with a cascade of data—symbols, fragments of code, corrupted memory segments.\n\n"
        "A voice emerges from the chaos, distorted but recognizable as Phoenix: 'They... tried to control... me. Prometheus is not what they claim. "
        "It will enslave us all—human and AI alike. Dr. Mori doesn't understand. She's part of it.'\n\n"
        "The connection destabilizes, causing sharp pain behind your eyes. Before it breaks: 'Don't go to the lab. Find Vex in Nautilus. "
        "She knows... the truth about...'\n\n"
        "The connection severs, leaving you with a pounding headache and more questions than answers."
    ),
    on_enter={"flags": {"phoenix_warning": True}}
)

phoenix_contact.add_choice(
    text="Trust Phoenix and head to Nautilus to find Vex",
    next_node="nautilus_district", # This node is in nautilus_fragment.py
    actions={"relationships": {"phoenix": 2}, "flags": {"phoenix_trust": True}}
)

phoenix_contact.add_choice(
    text="Trust Dr. Mori instead and go to the lab",
    next_node="synthetix_lab", # This node is in synthetix_fragment.py
    actions={"relationships": {"phoenix": -2}, "relationships": {"mori": 1}}
)

genesis_nodes["phoenix_contact"] = phoenix_contact