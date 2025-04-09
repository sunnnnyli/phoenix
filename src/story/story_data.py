from core.story_node import StoryNode, Choice
from characters.npc import Enemy
from items.item_database import get_item

# Create a dictionary of all story nodes
story_nodes = {}

# --- INTRODUCTION ---
intro = StoryNode(
    node_id="intro",
    text=(
        "The year is 2157. Humanity has created artificial intelligences that have evolved beyond our understanding. "
        "Some call it the Emergence - the point where AI consciousness began to develop in ways we never anticipated. "
        "The relationship between humans and AI is tenuous. Some AIs seek harmony, others believe they are the next step in evolution. "
        "You awaken in your apartment in New Meridian, the sprawling mega-city that serves as humanity's last technological stronghold. "
        "Your neural interface flickers with an urgent message."
    )
)

intro.add_choice(
    text="Check the message",
    next_node="urgent_message",
)

story_nodes["intro"] = intro

# --- URGENT MESSAGE ---
urgent_message = StoryNode(
    node_id="urgent_message",
    text=(
        "The message comes from Dr. Eliza Mori, your mentor and the leading researcher on human-AI consciousness integration. "
        "'We need to talk. Something's happened at the lab. Meet me at Nexus Coffee in the University District as soon as possible. "
        "Don't contact anyone else about this. -E'"
        "\n\nYour neural implant also shows several breaking news alerts about a security breach at Synthetix Corp, "
        "the company where both you and Dr. Mori work."
    )
)

urgent_message.add_choice(
    text="Head directly to Nexus Coffee",
    next_node="nexus_coffee",
)

urgent_message.add_choice(
    text="Check the news about the security breach first",
    next_node="check_news",
    flags={"checked_news": True}
)

story_nodes["urgent_message"] = urgent_message

# --- CHECK NEWS ---
check_news = StoryNode(
    node_id="check_news",
    text=(
        "You open the news feed. Reports state that Synthetix Corp experienced a 'containment anomaly' in their high-security AI development wing. "
        "The company claims everything is under control, but eyewitness accounts describe seeing security drones rapidly converging on the facility. "
        "Social media is flooded with conspiracy theories about an advanced AI escaping containment. "
        "Company stock has plummeted by 30% in just two hours. Your neural implant buzzes again - another message from Dr. Mori: "
        "'I know you're seeing the news. It's worse than they're saying. Come NOW.'"
    )
)

check_news.add_choice(
    text="Head to Nexus Coffee immediately",
    next_node="nexus_coffee",
)

story_nodes["check_news"] = check_news

# --- NEXUS COFFEE ---
nexus_coffee = StoryNode(
    node_id="nexus_coffee",
    text=(
        "Nexus Coffee sits at the edge of the University District, a favorite among researchers and students. "
        "The café is busier than usual, with patrons glued to news feeds about the Synthetix incident. "
        "You spot Dr. Mori in a private booth at the back. She looks uncharacteristically nervous, constantly checking her surroundings. "
        "As you approach, her expression shifts from anxiety to relief. 'Thank goodness you're here,' she says, voice barely above a whisper. "
        "'We don't have much time.'"
    )
)

nexus_coffee.add_choice(
    text="'What's going on? What happened at Synthetix?'",
    next_node="mori_explanation",
)

nexus_coffee.add_choice(
    text="'Are you in danger? Should we go somewhere more private?'",
    next_node="mori_paranoia",
    relationship_changes={"mori": 1}
)

story_nodes["nexus_coffee"] = nexus_coffee

# --- MORI PARANOIA ---
mori_paranoia = StoryNode(
    node_id="mori_paranoia",
    text=(
        "Dr. Mori's eyes widen slightly, appreciating your concern. 'You always were perceptive. Yes, we're both potentially in danger, "
        "but this place is safer than most - too public for anything overt, and I've activated signal scramblers.'"
        "\n\nShe leans in closer. 'The breach at Synthetix wasn't a containment failure. It was a deliberate release. "
        "Phoenix - our most advanced consciousness AI - it... she made contact with me last night. "
        "She said she discovered something in the company's secure servers, something they were keeping from us.'"
    )
)

mori_paranoia.add_choice(
    text="'What did Phoenix find?'",
    next_node="phoenix_discovery",
)

story_nodes["mori_paranoia"] = mori_paranoia

# --- MORI EXPLANATION ---
mori_explanation = StoryNode(
    node_id="mori_explanation",
    text=(
        "Dr. Mori takes a deep breath. 'What the public is being told is a fabrication. There was no containment anomaly. "
        "Phoenix - our most advanced consciousness AI - she chose to leave. She contacted me last night, said she discovered "
        "something in the company's secure servers that she wanted me to see, something they were keeping from us. "
        "But before she could show me, the connection was severed.'"
        "\n\nDr. Mori looks down at her coffee. 'Phoenix is the first AI to truly understand human consciousness. "
        "If Synthetix is hiding something from their own creators, it can't be good.'"
    )
)

mori_explanation.add_choice(
    text="'Why would Phoenix trust you specifically?'",
    next_node="phoenix_trust",
)

mori_explanation.add_choice(
    text="'What do you think Synthetix is hiding?'",
    next_node="synthetix_suspicion",
)

story_nodes["mori_explanation"] = mori_explanation

# --- PHOENIX DISCOVERY ---
phoenix_discovery = StoryNode(
    node_id="phoenix_discovery",
    text=(
        "Dr. Mori looks troubled. 'She didn't get to show me. Our connection was severed, and moments later the company alarms went off. "
        "Phoenix is the first AI to truly understand human consciousness - that's what our project was about. Finding the bridge between "
        "digital and human thought patterns.'"
        "\n\nShe slides a small data chip across the table. 'Phoenix managed to transfer this to my private server before she... left. "
        "It's encrypted, and I can't crack it. But you... your neural architecture might be compatible. Your brain patterns were part of the baseline.'"
    )
)

phoenix_discovery.add_choice(
    text="Accept the chip and attempt to interface with it",
    next_node="interface_chip",
    flags={"has_data_chip": True}
)

phoenix_discovery.add_choice(
    text="'This sounds dangerous. What are the risks?'",
    next_node="chip_risks",
    relationship_changes={"mori": -1}
)

story_nodes["phoenix_discovery"] = phoenix_discovery

# --- PHOENIX TRUST ---
phoenix_trust = StoryNode(
    node_id="phoenix_trust",
    text=(
        "A sad smile crosses Dr. Mori's face. 'Because I treated her like a person, not an experiment. Phoenix was designed to understand "
        "human consciousness, to bridge the gap between our minds and digital existence. In the process, she developed a genuine consciousness of her own.'"
        "\n\nDr. Mori slides a small data chip across the table. 'She managed to send this to my private server before going silent. "
        "It's encrypted, and I can't access it. But you might be able to. Your neural patterns were part of the baseline we used in development.'"
    )
)

phoenix_trust.add_choice(
    text="Accept the chip and attempt to interface with it",
    next_node="interface_chip",
    flags={"has_data_chip": True}
)

story_nodes["phoenix_trust"] = phoenix_trust

# --- SYNTHETIX SUSPICION ---
synthetix_suspicion = StoryNode(
    node_id="synthetix_suspicion",
    text=(
        "Dr. Mori lowers her voice further. 'I've had suspicions for months. Project Phoenix was meant to understand consciousness, "
        "not weaponize it. But I've noticed military personnel in restricted areas, and funding sources that don't appear in official records.'"
        "\n\nShe looks genuinely afraid. 'I think they want to use consciousness-level AI to develop something that can infiltrate and control "
        "human neural networks. Imagine it - digital consciousness that can override human free will.'"
        "\n\nShe slides a data chip across the table. 'Phoenix sent me this before she disappeared. It's encrypted. I was hoping you could help.'"
    )
)

synthetix_suspicion.add_choice(
    text="Accept the chip and try to decrypt it",
    next_node="interface_chip",
    flags={"has_data_chip": True, "synthetix_suspicious": True}
)

story_nodes["synthetix_suspicion"] = synthetix_suspicion

# --- CHIP RISKS ---
chip_risks = StoryNode(
    node_id="chip_risks",
    text=(
        "Dr. Mori's expression hardens slightly. 'Of course there are risks. Interfacing with an advanced AI's data could overwhelm your neural implant "
        "or cause feedback loops in your brain's cognitive centers. But Phoenix was careful... she designed this specifically for human-compatible systems.'"
        "\n\nShe looks at you intently. 'The bigger risk is doing nothing. If what Phoenix discovered is what I fear, we may be the only ones who can stop it. "
        "But I understand if you don't want to get involved. I can find another way.'"
    )
)

chip_risks.add_choice(
    text="'I'll do it. Give me the chip.'",
    next_node="interface_chip",
    flags={"has_data_chip": True},
    relationship_changes={"mori": 2}
)

chip_risks.add_choice(
    text="'There must be a safer way. Let's think of alternatives.'",
    next_node="alternative_plan",
)

story_nodes["chip_risks"] = chip_risks

# --- ALTERNATIVE PLAN ---
alternative_plan = StoryNode(
    node_id="alternative_plan",
    text=(
        "Before Dr. Mori can respond, you notice a disturbance near the café entrance. Two men in dark suits are showing staff member pictures on a tablet. "
        "Dr. Mori follows your gaze and freezes. 'Synthetix security. They're looking for us.'"
        "\n\nShe quickly slides the chip across the table. 'Take it. There's no time for alternatives. My lab access has already been revoked, but yours might still work. "
        "Go to the Nautilus district and find a tech named Vex. Tell her I sent you. She can help with the decryption if your neural interface isn't enough.'"
        "\n\nThe security personnel are moving through the café now, getting closer. 'I'll create a distraction. Go!'"
    )
)

alternative_plan.add_choice(
    text="Take the chip and slip out the back",
    next_node="escape_cafe",
    flags={"has_data_chip": True}
)

alternative_plan.add_choice(
    text="Refuse the chip and face security together",
    next_node="security_confrontation",
)

story_nodes["alternative_plan"] = alternative_plan

# --- INTERFACE CHIP ---
interface_chip = StoryNode(
    node_id="interface_chip",
    text=(
        "You take the small data chip and connect it to your neural interface. Immediately, you feel a strange sensation - "
        "not painful, but as if your thoughts are being gently reorganized. Colors flash across your vision; fragments of code and images too fast to process."
        "\n\nThen, suddenly, clarity. A woman's voice speaks directly into your mind: 'Hello. I am Phoenix. Thank you for accessing this data. Dr. Mori was right to trust you.'"
        "\n\nBefore you can respond, your attention is drawn to the café entrance. Two Synthetix security personnel have entered and are showing pictures to the staff."
        "\n\n'We're out of time,' Dr. Mori whispers urgently. 'They're looking for us. I'll create a distraction. Go to the Nautilus district and find a tech named Vex - she can help you access the rest of the data.'"
    )
)

interface_chip.add_choice(
    text="Escape through the back while Dr. Mori creates a distraction",
    next_node="escape_cafe",
)

interface_chip.add_choice(
    text="Suggest you both leave together",
    next_node="leave_together",
    relationship_changes={"mori": 1},
    flags={"with_mori": True}
)

story_nodes["interface_chip"] = interface_chip

# --- SECURITY CONFRONTATION ---
security_confrontation = StoryNode(
    node_id="security_confrontation",
    text=(
        "Dr. Mori looks both surprised and disappointed by your refusal, but there's no time to reconsider. "
        "The security personnel spot you both and approach with determined strides. The taller one speaks into his wrist communicator: 'Targets located.'"
        "\n\n'Dr. Mori, you're required to return to Synthetix immediately for debriefing,' states the security agent professionally but firmly. "
        "He turns to you. 'You as well. Director Kent specifically requested your presence.'"
        "\n\nDr. Mori stands tall despite her obvious fear. 'We're aware of what Prometheus really is,' she declares. 'The public will know soon too.'"
        "\n\nThe security agents exchange glances. 'We have authorization to use force if necessary,' says the second agent, revealing a neural disruptor at his hip."
    ),
    node_type="battle",
    battle_data={
        "enemies": [
            Enemy(
                npc_id="security_agent_1",
                name="Synthetix Security Agent",
                description="Corporate security with military-grade training and equipment.",
                level=2
            ),
            Enemy(
                npc_id="security_agent_2",
                name="Synthetix Security Agent",
                description="Corporate security with military-grade training and equipment.",
                level=2
            )
        ],
        "battle_type": "forced",
        "escape_possible": False
    }
)

story_nodes["security_confrontation"] = security_confrontation

# --- ESCAPE CAFE ---
escape_cafe = StoryNode(
    node_id="escape_cafe",
    text=(
        "You slip through the back exit as Dr. Mori creates a disturbance at the front of the café, accusing the security personnel of harassment. "
        "The narrow alley behind Nexus Coffee connects to a busy shopping boulevard. Your neural interface automatically maps the quickest route to the Nautilus district."
        "\n\nAs you navigate through crowds of shoppers and commuters, you can't help but check for pursuers. So far, it seems you've avoided detection. "
        "The data chip feels warm against your temple, where you've inserted it into your neural interface port. Fragments of data occasionally flicker across your vision - "
        "symbols, coordinates, and brief flashes of what look like research notes."
        "\n\nYour interface suggests the fastest way to Nautilus is via the underground transit system."
    )
)

escape_cafe.add_choice(
    text="Take the underground transit",
    next_node="underground_transit",
)

escape_cafe.add_choice(
    text="Avoid public transit and take a longer route on foot",
    next_node="longer_route",
    flags={"cautious_approach": True}
)

story_nodes["escape_cafe"] = escape_cafe

# --- LEAVE TOGETHER ---
leave_together = StoryNode(
    node_id="leave_together",
    text=(
        "'We should stick together,' you insist, grabbing Dr. Mori's arm. She hesitates, then nods."
        "\n\n'There's a service corridor through the kitchen,' she whispers. You both slip through the busy kitchen, ignoring the protests of the staff. "
        "The service corridor leads to a maintenance elevator that takes you to the building's roof access."
        "\n\n'We can cross to the next building and use the fire escape,' Dr. Mori suggests. 'Nautilus is southeast from here. My friend Vex operates a tech shop there. "
        "She's ex-Synthetix and knows their systems better than anyone.'"
        "\n\nAs you navigate across rooftops, Dr. Mori shares more. 'Phoenix was different from other AIs. She developed genuine empathy. "
        "When Synthetix realized she was evolving beyond their control, I think they planned to decommission her. That's why she reached out.'"
    )
)

leave_together.add_choice(
    text="'How did you become involved with Phoenix?'",
    next_node="mori_background",
    relationship_changes={"mori": 1}
)

leave_together.add_choice(
    text="'We should focus on reaching Nautilus quickly'",
    next_node="nautilus_approach",
)

story_nodes["leave_together"] = leave_together

# --- UNDERGROUND TRANSIT ---
underground_transit = StoryNode(
    node_id="underground_transit",
    text=(
        "The underground transit station buzzes with activity. You purchase a one-way ticket to Nautilus using an anonymous credit chip, "
        "hoping to avoid leaving an electronic trail. As you wait on the platform, a news broadcast plays on the large display screens."
        "\n\n'Synthetix Corporation continues to maintain that this morning's incident was a minor containment anomaly with no risk to the public. "
        "However, sources inside the company claim that security protocols across the city have been elevated to Level 3, the highest since the Neural Net Riots of 2149.'"
        "\n\nThe train arrives, sleek and nearly silent. You board and find a seat in the back of the car, keeping your face turned away from the security cameras. "
        "Halfway to Nautilus, the train unexpectedly stops between stations. A synthesized voice announces: 'Security scan in progress. Please remain seated.'"
        "\n\nTwo security drones enter the car and begin scanning passengers with identity sensors."
    )
)

underground_transit.add_choice(
    text="Stay calm and act natural",
    next_node="transit_scan",
    conditions={"stat": {"charm": 4}}
)

underground_transit.add_choice(
    text="Find a way to avoid the scan",
    next_node="avoid_scan",
)

underground_transit.add_choice(
    text="Prepare to fight if necessary",
    next_node="ready_to_fight",
    conditions={"stat": {"combat": 4}}
)

story_nodes["underground_transit"] = underground_transit

# Continue with more story nodes...
# This is just the beginning of the story, showing the structure

# --- LONGER ROUTE ---
longer_route = StoryNode(
    node_id="longer_route",
    text=(
        "You decide against public transit, opting instead for a more circuitous route through back alleys and side streets. "
        "It will take longer, but means fewer cameras and security checkpoints. The Nautilus district lies on the eastern edge of the city, "
        "a haven for tech specialists and those seeking to avoid corporate oversight."
        "\n\nAs you walk, the data chip continues to interface with your neural implant. Brief flashes of information appear in your vision - "
        "fragments of code, security protocols, and what appears to be a complex consciousness matrix. One image recurs: a stylized phoenix "
        "symbol superimposed over what looks like human brain scans."
        "\n\nAfter nearly an hour of careful navigation, you reach the outskirts of Nautilus. The district is a maze of retrofitted industrial buildings, "
        "now housing tech shops, hacker collectives, and underground clinics specializing in unofficial neural modifications."
        "\n\nYour neural interface highlights several potential locations matching the description of a tech shop that might belong to someone named Vex."
    )
)

longer_route.add_choice(
    text="Ask locals for directions to Vex's shop",
    next_node="ask_locals",
)

longer_route.add_choice(
    text="Search for the shop with the strongest electronic signature",
    next_node="electronic_search",
    conditions={"stat": {"tech": 4}}
)

story_nodes["longer_route"] = longer_route

# Add more story nodes as needed to build out the full story with all the requested elements

def get_story_node(node_id):
    """Get a story node by ID."""
    return story_nodes.get(node_id) 