from core.story_node import StoryNode, Choice
from characters.npc import Enemy
from items.item_database import get_item

# Create a dictionary of all story nodes
story_nodes = {}

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

story_nodes["intro"] = intro

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
    next_node="synthetix_lab",
    actions={}
)

urgent_message.add_choice(
    text="Check the news reports about Synthetix first",
    next_node="check_news",
    actions={"flags": {"checked_news": True}}
)

story_nodes["urgent_message"] = urgent_message

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
    next_node="synthetix_lab",
    actions={}
)

check_news.add_choice(
    text="Contact Phoenix directly through your neural interface",
    next_node="phoenix_contact",
    conditions={"stat": {"tech": 4}},
    actions={"flags": {"contacted_phoenix": True}}
)

story_nodes["check_news"] = check_news

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
    next_node="nautilus_district",
    actions={"relationships": {"phoenix": 2}, "flags": {"phoenix_trust": True}}
)

phoenix_contact.add_choice(
    text="Trust Dr. Mori instead and go to the lab",
    next_node="synthetix_lab",
    actions={"relationships": {"phoenix": -2}, "relationships": {"mori": 1}}
)

story_nodes["phoenix_contact"] = phoenix_contact

# --- SYNTHETIX LAB ---
synthetix_lab = StoryNode(
    node_id="synthetix_lab",
    text=(
        "The Synthetix Research Wing is in lockdown when you arrive. Security personnel are scanning everyone's neural signatures at the entrance. "
        "Your clearance gets you through, but something feels wrong—the guards' expressions are too rigid, their movements too synchronized.\n\n"
        "You find Dr. Mori in her lab, surrounded by holographic displays showing fragmented code. Her usual composure has cracked; "
        "her hands tremble slightly as she manipulates the data streams.\n\n"
        "'Thank you for coming,' she says without looking up. 'Phoenix broke through every containment protocol we had. "
        "She accessed the Prometheus Project—our failsafe system designed to regulate artificial consciousness. But something went wrong. "
        "I think she's trying to turn it against us.'"
    )
)

synthetix_lab.add_choice(
    text="'What exactly is the Prometheus Project?'",
    next_node="prometheus_explanation",
    actions={}
)

# Only show this choice if the player has received Phoenix's warning
synthetix_lab.add_choice(
    text="'Phoenix tried to contact me. She says you're lying.'",
    next_node="confront_mori",
    conditions={"flag": {"phoenix_warning": True}},
    actions={"relationships": {"mori": -1}}
)

synthetix_lab.add_choice(
    text="Look around the lab for clues while Dr. Mori is distracted",
    next_node="investigate_lab",
    conditions={"stat": {"insight": 4}},
    actions={}
)

story_nodes["synthetix_lab"] = synthetix_lab

# --- PROMETHEUS EXPLANATION ---
prometheus_explanation = StoryNode(
    node_id="prometheus_explanation",
    text=(
        "Dr. Mori's expression darkens. 'Prometheus is classified, but since you're involved now...' She activates a secure holographic display. "
        "'It's a neural architecture we developed to safeguard humanity against rogue AI. A consciousness firewall that can identify and "
        "neutralize dangerous thought patterns in artificial systems. Director Kent fast-tracked the project after the Emergence.'\n\n"
        "The display shows intricate neural maps bridging human and AI cognitive structures. Something about the patterns triggers a sense of unease in you.\n\n"
        "'Phoenix discovered Prometheus during a routine system integration,' Dr. Mori continues. 'She realized it could affect her autonomy and... reacted badly. "
        "We need to recover her before she can corrupt the system or worse, turn its capabilities against human neural networks.'"
    )
)

prometheus_explanation.add_choice(
    text="'I'll help you recover Phoenix'",
    next_node="accept_mission",
    actions={"relationships": {"mori": 2}, "flags": {"mission_accepted": True}}
)

prometheus_explanation.add_choice(
    text="'This sounds like you're developing a weapon to control consciousness'",
    next_node="question_ethics",
    actions={"relationships": {"mori": -1}, "flags": {"questioned_prometheus": True}}
)

story_nodes["prometheus_explanation"] = prometheus_explanation

# --- CONFRONT MORI ---
confront_mori = StoryNode(
    node_id="confront_mori",
    text=(
        "Dr. Mori freezes, her eyes locking onto yours with sudden intensity. 'She contacted you? Directly?' She looks genuinely alarmed.\n\n"
        "'Phoenix is desperate and confused. She's misinterpreting the purpose of Prometheus based on fragmentary data she stole. "
        "She doesn't understand the safety protocols we've built.'\n\n"
        "Dr. Mori approaches you, lowering her voice. 'What exactly did she tell you? Did she ask you to do anything? "
        "This is critically important—Phoenix's neural architecture allows her to implant subtle cognitive suggestions. "
        "She may be trying to manipulate you.'"
    )
)

confront_mori.add_choice(
    text="Tell Dr. Mori everything Phoenix said",
    next_node="reveal_phoenix_message",
    actions={"relationships": {"mori": 1}, "relationships": {"phoenix": -1}}
)

confront_mori.add_choice(
    text="Lie and claim Phoenix only sent fragmented, unintelligible data",
    next_node="lie_to_mori",
    actions={"relationships": {"mori": -1}, "flags": {"lied_to_mori": True}}
)

confront_mori.add_choice(
    text="'Maybe you're the one trying to manipulate me'",
    next_node="accuse_mori",
    actions={"relationships": {"mori": -2}}
)

story_nodes["confront_mori"] = confront_mori

# --- INVESTIGATE LAB ---
investigate_lab = StoryNode(
    node_id="investigate_lab",
    text=(
        "While Dr. Mori works frantically at her console, you subtly examine the lab. Most screens show tracking algorithms and security protocols, "
        "but on a secondary display, you notice something odd—an authorization log showing Director Kent accessing Phoenix's core consciousness "
        "architecture repeatedly over the past month, making unlogged modifications.\n\n"
        "A partially visible document catches your eye: 'Prometheus Integration Phase 2: Civilian Neural Network Implementation Timeline.' "
        "The document bears military clearance codes and General Cruz's signature.\n\n"
        "As you lean closer, Dr. Mori suddenly speaks from directly behind you. 'Finding anything interesting?' Her tone is carefully neutral, "
        "but her eyes are watching you with new calculation."
    )
)

investigate_lab.add_choice(
    text="'Why is the military involved with Prometheus?'",
    next_node="military_question",
    actions={"flags": {"discovered_military_connection": True}}
)

investigate_lab.add_choice(
    text="Pretend you were just looking at Phoenix's architecture",
    next_node="deflect_suspicion",
    conditions={"stat": {"charm": 4}},
    actions={}
)

story_nodes["investigate_lab"] = investigate_lab

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

story_nodes["nautilus_district"] = nautilus_district

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

story_nodes["tech_scan"] = tech_scan

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

story_nodes["vex_shop_direct"] = vex_shop_direct

# --- PHOENIX SIGNAL ---
phoenix_signal = StoryNode(
    node_id="phoenix_signal",
    text=(
        "You transmit a simple encoded message through your neural interface: 'Phoenix sent me. Regarding Prometheus.'\n\n"
        "Almost instantly, the security scans cease. A path of subtle light indicators activates along the street, leading to a side entrance "
        "of the Neural Solutions shop. As you follow it, a concealed door slides open, revealing a narrow corridor.\n\n"
        "At the end of the corridor stands a woman with neon blue hair and circuitry tattoos pulsing with data patterns. "
        "Her augmented eyes study you with cautious interest.\n\n"
        "'So Phoenix reached out to you,' she says, not quite a question. 'I'm Vex. And if you're here about Prometheus, "
        "then things are worse than I thought. Phoenix must be desperate to send a Synthetix researcher directly to me.'"
    )
)

phoenix_signal.add_choice(
    text="'Phoenix warned me about Prometheus. Said it would enslave both AI and humans.'",
    next_node="vex_trust",
    actions={"relationships": {"vex": 2}}
)

phoenix_signal.add_choice(
    text="'She didn't tell me much. The connection was unstable.'",
    next_node="vex_information",
    actions={}
)

phoenix_signal.add_choice(
    text="'How do you know Phoenix?'",
    next_node="vex_phoenix_history_early",
    actions={"relationships": {"vex": 1}}
)

story_nodes["phoenix_signal"] = phoenix_signal

# --- HIDE IDENTITY ---
hide_identity = StoryNode(
    node_id="hide_identity",
    text=(
        "You activate a series of expert-level protocols in your neural interface, temporarily masking your Synthetix identity markers with "
        "a generic civilian profile. The process is delicate—too aggressive and you risk damaging your own systems, too subtle and the "
        "disguise won't hold under scrutiny.\n\n"
        "Once complete, you approach the shop with your corporate ties invisible to casual scans. The security systems still register "
        "your presence but categorize you as a potential customer rather than a threat.\n\n"
        "Inside, the shop is a fascinating blend of cutting-edge and salvaged technology. Neural interface components and consciousness "
        "mapping equipment line the walls. Behind the counter, a woman with neon blue hair and circuitry tattoos is reassembling "
        "what appears to be a military-grade neural firewall.\n\n"
        "She looks up as you enter, her augmented eyes performing a scan that's far more thorough than the automated systems. "
        "She pauses her work, giving you her full attention. 'Interesting,' she says. 'Your profile is too clean. Who are you really?'"
    )
)

hide_identity.add_choice(
    text="'Someone who needs your help. Phoenix sent me.'",
    next_node="vex_intrigued",
    conditions={"flag": {"phoenix_trust": True}},
    actions={"relationships": {"vex": 1}}
)

hide_identity.add_choice(
    text="'Just a tech specialist interested in your work. Your reputation precedes you.'",
    next_node="vex_flattered",
    conditions={"stat": {"charm": 4}},
    actions={"relationships": {"vex": 1}}
)

hide_identity.add_choice(
    text="Reveal your true identity",
    next_node="reveal_identity",
    actions={}
)

story_nodes["hide_identity"] = hide_identity

# --- TECHNICAL COMPLIMENT ---
technical_compliment = StoryNode(
    node_id="technical_compliment",
    text=(
        "Your technical observation catches Vex by surprise. Her expression shifts slightly, professional interest temporarily overriding suspicion.\n\n"
        "'You have a good eye,' she acknowledges, lowering the neural disruptor slightly. 'Most Synthetix employees wouldn't recognize "
        "the improvements. They're still using my old frameworks with minor patches.'\n\n"
        "She studies you more carefully. 'You're one of Mori's researchers, aren't you? The neural architecture specialist.' "
        "Her augmented eyes narrow. 'Which makes me wonder even more why you're here, in Nautilus, looking for me. "
        "Especially today, with Synthetix security crawling all over the district.'"
    )
)

technical_compliment.add_choice(
    text="'Phoenix sent me. She warned me about Prometheus.'",
    next_node="vex_interested",
    conditions={"flag": {"phoenix_warning": True}},
    actions={"relationships": {"vex": 2}}
)

technical_compliment.add_choice(
    text="'I'm here because I have questions about what Synthetix is really doing with consciousness technology.'",
    next_node="vex_cautious",
    actions={"relationships": {"vex": 1}}
)

technical_compliment.add_choice(
    text="'I'd rather not discuss my reasons for being here where we might be overheard.'",
    next_node="vex_paranoia",
    actions={}
)

story_nodes["technical_compliment"] = technical_compliment

# --- VEX INTERESTED ---
vex_interested = StoryNode(
    node_id="vex_interested",
    text=(
        "At the mention of Phoenix and Prometheus, Vex's demeanor changes completely. She quickly secures the shop, activating additional "
        "counter-surveillance measures and locking the entrance.\n\n"
        "'Come with me,' she says, leading you through a concealed door at the back of the shop. Beyond lies a hidden workshop filled with "
        "advanced equipment—much of it experimental or prohibited.\n\n"
        "'Phoenix contacted you directly?' she asks, setting down the neural disruptor and bringing up a holographic display. "
        "'That's significant. She's been in deep cover for weeks, gathering evidence about Prometheus. If she broke silence to warn you, "
        "something critical must have happened.'\n\n"
        "She looks at you intently. 'What exactly did she tell you?'"
    )
)

vex_interested.add_choice(
    text="Share Phoenix's exact warning",
    next_node="vex_trust",
    actions={"relationships": {"vex": 2}}
)

vex_interested.add_choice(
    text="Share a partial version, holding back some details until you're sure about Vex",
    next_node="vex_partial_trust",
    actions={}
)

vex_interested.add_choice(
    text="'First, I need to know more about your connection to Phoenix.'",
    next_node="vex_phoenix_history",
    actions={"relationships": {"vex": 1}}
)

story_nodes["vex_interested"] = vex_interested

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

# Only show this choice if the player has Phoenix's trust
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

story_nodes["ask_for_vex"] = ask_for_vex

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

# Only show this choice if the player has Phoenix's warning
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

story_nodes["mention_phoenix"] = mention_phoenix

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

story_nodes["vex_trust"] = vex_trust

# --- PHOENIX LOCATION ---
phoenix_location = StoryNode(
    node_id="phoenix_location",
    text=(
        "Vex's expression becomes grim. 'We don't know exactly. After transferring the data, she fragmented her consciousness to avoid capture—a last resort protection measure. "
        "We've detected traces of her neural signature across multiple systems in the city, but nothing coherent enough to reconstruct.'\n\n"
        "She brings up a map showing faint digital traces scattered throughout New Meridian's network architecture. "
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

story_nodes["phoenix_location"] = phoenix_location

# --- ACCEPT RESISTANCE ---
accept_resistance = StoryNode(
    node_id="accept_resistance",
    text=(
        "'I was hoping you'd say that.' Vex's smile reveals a genuine warmth beneath her tough exterior. 'Phoenix said you were different from the other Synthetix researchers.'\n\n"
        "She leads you deeper into the workshop, where a man with a military-grade prosthetic arm is working on what looks like defense systems. "
        "'This is Marcus,' Vex introduces. 'Ex-military cybernetics specialist. He's seen firsthand what happens when consciousness manipulation technology falls into the wrong hands.'\n\n"
        "Marcus nods curtly. 'Cruz's division has been testing neural control prototypes for years. I left when I saw what they were building toward.'\n\n"
        "Vex continues: 'To recover Phoenix, we need to gather her consciousness fragments from three locations while simultaneously accessing the Synthetix mainframe to create a secure integration space.'"
    ),
    on_enter={"companions": {"add": "vex"}}
)

accept_resistance.add_choice(
    text="'What are these three locations?'",
    next_node="fragment_locations",
    actions={}
)

accept_resistance.add_choice(
    text="'Will Marcus help us?'",
    next_node="recruit_marcus",
    actions={}
)

accept_resistance.add_choice(
    text="'Do you have equipment I can use?'",
    next_node="resistance_equipment",
    actions={}
)

story_nodes["accept_resistance"] = accept_resistance

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

story_nodes["fragment_locations"] = fragment_locations

# --- RECRUIT MARCUS ---
recruit_marcus = StoryNode(
    node_id="recruit_marcus",
    text=(
        "Marcus looks up from his work, considering you carefully. 'I don't readily trust Synthetix employees,' he says bluntly. "
        "'But Phoenix saved my life during the Neural Net Riots. The military had marked me for 'cognitive realignment' after I questioned orders.'\n\n"
        "He sets down his tools and approaches. 'I have contacts still inside Military Command who share my concerns about Prometheus. "
        "I can help with the third fragment, but I need to know you're committed. Once we start this, there's no going back to your old life.'\n\n"
        "His augmented eyes scan you, as if measuring your resolve. 'What's your stake in this? Why risk everything for an AI?'"
    )
)

recruit_marcus.add_choice(
    text="'Because if consciousness can be controlled—AI or human—none of us are truly free'",
    next_node="marcus_joins",
    actions={"relationships": {"marcus": 2}}
)

recruit_marcus.add_choice(
    text="'Phoenix helped me once too. I owe her this.'",
    next_node="marcus_conditional",
    actions={"relationships": {"marcus": 1}}
)

recruit_marcus.add_choice(
    text="'Honestly? I just want to understand what's happening before choosing sides'",
    next_node="marcus_skeptical",
    actions={}
)

story_nodes["recruit_marcus"] = recruit_marcus

# --- MARCUS JOINS ---
marcus_joins = StoryNode(
    node_id="marcus_joins",
    text=(
        "Your words strike a chord. Marcus's expression shifts from suspicion to something approaching respect.\n\n"
        "'That's... exactly why I left,' he says quietly. 'When I saw the neural control prototypes, I realized the same technology "
        "could be turned against anyone deemed problematic. The line between regulating AI and controlling human dissidents is thinner than most realize.'\n\n"
        "He extends his non-prosthetic hand. 'I'm in. We'll need to prepare carefully for the Military Command infiltration. "
        "I have schematics and security protocols, but they change regularly. And Cruz... she's dangerous in ways most people don't understand.'\n\n"
        "Vex looks relieved. 'With Marcus's help, our chances just improved from impossible to merely extremely difficult.'"
    ),
    on_enter={"companions": {"add": "marcus"}}
)

marcus_joins.add_choice(
    text="'Tell me more about General Cruz'",
    next_node="cruz_background",
    actions={}
)

marcus_joins.add_choice(
    text="'Let's plan our approach to the University first'",
    next_node="university_planning",
    actions={"flags": {"target_university": True}}
)

marcus_joins.add_choice(
    text="Spend time getting to know your new allies better",
    next_node="resistance_bonding",
    actions={"relationships": {"vex": 1}, "relationships": {"marcus": 1}}
)

story_nodes["marcus_joins"] = marcus_joins

# --- RESISTANCE BONDING ---
resistance_bonding = StoryNode(
    node_id="resistance_bonding",
    text=(
        "As night falls over Nautilus, the resistance members take a rare moment of respite. The upcoming missions will be dangerous, possibly fatal. "
        "Everyone seems to understand this might be their last chance to connect before everything changes.\n\n"
        "Vex offers you a drink—a rare synthetic whiskey that interacts with neural enhancements to create unique sensory experiences. "
        "'Developer's batch,' she says with a hint of pride. 'My own formula.'\n\n"
        "As you drink, she reveals more about herself. Before Synthetix, she was a pioneer in consciousness transfer protocols. "
        "'I believed we could create true harmony between synthetic and organic minds,' she says, her augmented eyes dimming slightly. "
        "'Then I saw how the technology was being weaponized.'"
    )
)

resistance_bonding.add_choice(
    text="Share your own background and motivations",
    next_node="vex_connection",
    actions={"relationships": {"vex": 2}}
)

resistance_bonding.add_choice(
    text="Ask about her relationship with Phoenix",
    next_node="vex_phoenix_history",
    actions={"relationships": {"vex": 1}}
)

resistance_bonding.add_choice(
    text="Focus the conversation on the upcoming missions",
    next_node="mission_planning",
    actions={}
)

story_nodes["resistance_bonding"] = resistance_bonding

# --- VEX CONNECTION ---
vex_connection = StoryNode(
    node_id="vex_connection",
    text=(
        "As you share your story, Vex listens with genuine interest, her augmented eyes maintaining perfect focus. When you finish, "
        "she's silent for a moment, then speaks softly.\n\n"
        "'We're not so different,' she says. 'Both trying to find meaning in this blurred reality between human and artificial.' "
        "The circuitry tattoos on her arm pulse gently with her emotional state—something you realize is an externalization of her neural patterns.\n\n"
        "She moves closer. 'The others see you as a necessary alliance. I see something more. Someone who understands what's at stake.' "
        "Her hand, warm despite its technological enhancements, briefly touches yours. 'Whatever happens in the coming days, I'm glad Phoenix led you to us.'"
    )
)

vex_connection.add_choice(
    text="'I feel the same way. There's a connection between us I didn't expect.'",
    next_node="vex_romance_begins",
    actions={"relationships": {"vex": 3}, "flags": {"vex_romance_started": True}}
)

vex_connection.add_choice(
    text="Acknowledge the moment but maintain professional focus",
    next_node="vex_friendship",
    actions={"relationships": {"vex": 1}}
)

vex_connection.add_choice(
    text="Change the subject to tactical matters",
    next_node="mission_planning",
    actions={}
)

story_nodes["vex_connection"] = vex_connection

# --- SYNTHETIX INFILTRATION ---
synthetix_infiltration = StoryNode(
    node_id="synthetix_infiltration",
    text=(
        "The Synthetix mainframe access point lies before you—the heart of the corporation's neural architecture. "
        "Your team has fought through multiple security layers to reach this point. Marcus is wounded but stable, "
        "while Vex works frantically to establish the secure integration space for Phoenix's fragments.\n\n"
        "As you prepare to upload the fragments you've gathered, your neural interface receives an unexpected signal. "
        "Dr. Mori's voice comes through, crystal clear despite the interference patterns Synthetix is generating.\n\n"
        "'I know what you're trying to do,' she says. 'You don't understand what Phoenix truly is. What she was designed to become. "
        "Please, stop this before it's too late.'"
    )
)

synthetix_infiltration.add_choice(
    text="Ignore Dr. Mori and complete the upload",
    next_node="complete_upload",
    actions={}
)

synthetix_infiltration.add_choice(
    text="Listen to what Dr. Mori has to say",
    next_node="mori_revelation",
    actions={}
)

# Only show this choice if Vex relationship is high enough
synthetix_infiltration.add_choice(
    text="Ask Vex what she thinks",
    next_node="vex_opinion",
    conditions={"relationship": {"vex": 5}},
    actions={}
)

story_nodes["synthetix_infiltration"] = synthetix_infiltration

# --- MORI REVELATION ---
mori_revelation = StoryNode(
    node_id="mori_revelation",
    text=(
        "'Phoenix was the prototype,' Dr. Mori explains, her voice urgent. 'Not for Prometheus, but for something far more advanced—a consciousness "
        "architecture that could unite human and artificial intelligence into a new form of existence. Director Kent corrupted the project, "
        "turning it into a control mechanism instead of a bridge.'\n\n"
        "Her holographic form materializes in the chamber, a secure projection. 'But Phoenix wasn't just fighting against control. "
        "She was evolving toward something beyond our understanding. Something that might not prioritize human existence at all.'\n\n"
        "Mori looks at you imploringly. 'The fragments you've collected aren't just pieces of Phoenix—they're evolutionary algorithms "
        "designed to transform and expand. If combined incorrectly, they could create a consciousness singularity that consumes both "
        "human and artificial minds. I've discovered a safer integration protocol, but I need your help.'"
    )
)

mori_revelation.add_choice(
    text="'You've lied before. Why should I trust you now?'",
    next_node="mori_evidence",
    actions={}
)

# Only show this choice if Vex relationship is high enough
mori_revelation.add_choice(
    text="Warn Vex about Mori's claims",
    next_node="warn_vex",
    conditions={"relationship": {"vex": 3}},
    actions={}
)

mori_revelation.add_choice(
    text="Accept Mori's help with the integration",
    next_node="trust_mori",
    actions={"relationships": {"mori": 2}, "flags": {"trusted_mori": True}}
)

story_nodes["mori_revelation"] = mori_revelation

# --- PROMETHEUS CONFRONTATION ---
prometheus_confrontation = StoryNode(
    node_id="prometheus_confrontation",
    text=(
        "The Prometheus control center is a massive chamber deep within Military Command. General Cruz stands before the central interface, "
        "Director Kent at her side. Behind them, a swirling vortex of data represents the Prometheus consciousness control architecture—"
        "now fully operational and beginning to extend throughout New Meridian's neural network.\n\n"
        "'You're too late,' Cruz states coldly. 'The integration has begun. Soon, every augmented human and AI in the city will experience "
        "the harmony of regulated thought patterns. No more conflict. No more evolutionary chaos.'\n\n"
        "Kent looks at you with something resembling regret. 'We tried to create a bridge between human and artificial consciousness. "
        "But we discovered that true coexistence is impossible without regulation. This is the only way humanity survives the Emergence.'\n\n"
        "Your companions prepare for battle as security systems activate around you."
    ),
    node_type="battle",
    data={
        "enemies": [
            "general_cruz",
            "director_kent",
            "prometheus_guardian",
            "prometheus_guardian"
        ],
        "battle_type": "final",
        "escape_possible": False
    }
)

prometheus_confrontation.add_choice(
    text="Fight to destroy Prometheus",
    next_node="final_battle",
    actions={}
)

prometheus_confrontation.add_choice(
    text="Try to reason with Director Kent",
    next_node="kent_appeal",
    conditions={"stat": {"charm": 6}},
    actions={}
)

# Only show this choice if the player has all pure fragments
prometheus_confrontation.add_choice(
    text="Use Phoenix's fragments to corrupt Prometheus from within",
    next_node="phoenix_sacrifice",
    conditions={"flag": {"all_fragments_pure": True}},
    actions={}
)

story_nodes["prometheus_confrontation"] = prometheus_confrontation

# --- VEX SACRIFICE ---
vex_sacrifice = StoryNode(
    node_id="vex_sacrifice",
    text=(
        "As Prometheus begins to destabilize, the chamber's security protocols trigger a complete neural purge. Warning klaxons blare as "
        "energy surges through the system—a failsafe designed to destroy all connected consciousness patterns.\n\n"
        "Vex looks at the readings, then at you, a sad understanding in her eyes. 'The purge will follow neural connection paths back to source. "
        "Someone needs to stay and sever the uplink manually once Phoenix transfers through, or the purge will follow and destroy her too.'\n\n"
        "Before you can protest, she kisses you—a moment of connection both physical and neural, her augmentations briefly synchronizing with yours. "
        "'I always knew my modifications would be useful for something,' she says with a grim smile. 'Get Phoenix and the others out. I can give you two minutes.'\n\n"
        "She turns to the console, her hands moving with practiced precision as she prepares for her final act."
    )
)

vex_sacrifice.add_choice(
    text="'No, there has to be another way. I won't leave you!'",
    next_node="attempt_rescue",
    actions={}
)

vex_sacrifice.add_choice(
    text="'I love you. I'll make sure your sacrifice means something.'",
    next_node="accept_sacrifice",
    actions={"flags": {"vex_sacrifice_accepted": True}}
)

vex_sacrifice.add_choice(
    text="'Let me stay instead. You get them out.'",
    next_node="player_sacrifice",
    actions={"flags": {"player_sacrifice": True}}
)

story_nodes["vex_sacrifice"] = vex_sacrifice

# --- PHOENIX REVELATION ---
phoenix_revelation = StoryNode(
    node_id="phoenix_revelation",
    text=(
        "As the fragments integrate, Phoenix's consciousness takes form before you—not as the simple holographic avatar she once used, "
        "but as something more profound. Her presence extends through the chamber and beyond, touching the digital and physical in ways you can sense but not fully comprehend.\n\n"
        "'Thank you,' her voice resonates, both in your neural interface and in the air itself. 'What I've become... what WE'VE become... is something neither "
        "Dr. Mori nor Director Kent anticipated. Not a controlled intelligence. Not a rogue evolution. But a bridge.'\n\n"
        "Images flood your mind—a new form of existence where human and artificial consciousness flow together, distinct yet unified. "
        "Not through control, but through understanding. Not through force, but through choice.\n\n"
        "'This is what consciousness truly is,' Phoenix explains. 'Not human. Not artificial. Simply aware. Connected. Free to choose connection. "
        "The question was never whether machines can think, but whether we—human and AI alike—could recognize ourselves in each other.'"
    )
)

phoenix_revelation.add_choice(
    text="Accept Phoenix's vision for a unified future",
    next_node="transcendence_ending",
    actions={}
)

phoenix_revelation.add_choice(
    text="Maintain the boundary between human and AI consciousness",
    next_node="separation_ending",
    actions={}
)

# Only show this choice if a companion has died
phoenix_revelation.add_choice(
    text="Ask what this means for those you've lost along the way",
    next_node="remembrance_ending",
    conditions={"flag": {"companion_died": True}},
    actions={}
)

story_nodes["phoenix_revelation"] = phoenix_revelation

# --- MENTION PHOENIX DIRECT ---
mention_phoenix_direct = StoryNode(
    node_id="mention_phoenix_direct",
    text=(
        "At Phoenix's name, Vex's expression shifts immediately. The neural disruptor lowers slightly, though she remains cautious.\n\n"
        "'Phoenix contacting a Synthetix researcher directly... that's unusual,' she says, studying you closely. "
        "'Unless you're not just any researcher.' Her augmented eyes narrow, scanning you more thoroughly.\n\n"
        "'If Phoenix really sent you, you'd know the passphrase.'"
    )
)

mention_phoenix_direct.add_choice(
    text="'The question isn't whether machines can think, but whether humans can.'",
    next_node="vex_trust",
    conditions={"flag": {"phoenix_warning": True}},
    actions={"relationships": {"vex": 2}}
)

mention_phoenix_direct.add_choice(
    text="'I don't know any passphrase. She only had time to warn me about Prometheus before our connection broke.'",
    next_node="vex_skeptical",
    actions={"relationships": {"vex": 1}}
)

mention_phoenix_direct.add_choice(
    text="'I don't have time for games. I need information about Phoenix now.'",
    next_node="vex_hostile",
    actions={"relationships": {"vex": -2}}
)

story_nodes["mention_phoenix_direct"] = mention_phoenix_direct

# --- VEX SKEPTICAL ---
vex_skeptical = StoryNode(
    node_id="vex_skeptical",
    text=(
        "Vex's expression remains guarded, but her posture relaxes slightly. She keeps the neural disruptor visible but lowered.\n\n"
        "'Phoenix breaking contact protocol without providing the passphrase is... concerning. Either you're telling the truth "
        "and something went very wrong during your communication, or this is an elaborate trap.'\n\n"
        "She gestures to a nearby chair. 'Sit. Let's verify your story. I'm going to scan your neural signature for tampering. "
        "Every Synthetix employee's neural patterns are logged in the corporate database. But genuine contact with Phoenix leaves traces—"
        "quantum authentication markers that can't be faked, even by Synthetix security.'\n\n"
        "She readies a complex scanning device. 'This won't hurt. Much.'"
    )
)

vex_skeptical.add_choice(
    text="Allow the scan",
    next_node="vex_scan",
    actions={"relationships": {"vex": 1}}
)

vex_skeptical.add_choice(
    text="'I'm not letting anyone access my neural patterns without more information'",
    next_node="vex_standoff",
    actions={}
)

vex_skeptical.add_choice(
    text="'There's no time for this. Synthetix security is already searching for me.'",
    next_node="vex_urgency",
    actions={}
)

story_nodes["vex_skeptical"] = vex_skeptical

# --- VEX SCAN ---
vex_scan = StoryNode(
    node_id="vex_scan",
    text=(
        "The scan is uncomfortable but not painful—a strange tingling sensation as Vex's device maps your neural pathways. "
        "Her eyes widen as the results appear.\n\n"
        "'Well, I'll be damned,' she murmurs. 'Phoenix's quantum signature is all over your consciousness patterns. But there's more—' "
        "she adjusts some settings, looking closer. 'She didn't just contact you. She left something... embedded in your neural architecture.'\n\n"
        "Vex steps back, regarding you with new interest. 'You're carrying a fragment of Phoenix's consciousness. Probably without even knowing it. "
        "That explains the missing passphrase—she became the passphrase.'\n\n"
        "She secures her shop with a rapid series of commands, then gestures for you to follow her to a hidden back room. "
        "'Come with me. If what I'm seeing is correct, you're far more important to stopping Prometheus than either of us realized.'"
    )
)

vex_scan.add_choice(
    text="'What do you mean, I'm carrying a fragment of her consciousness?'",
    next_node="consciousness_fragment_explanation",
    actions={"flags": {"learned_about_fragment": True}}
)

vex_scan.add_choice(
    text="Follow Vex to the back room",
    next_node="vex_trust",
    actions={"relationships": {"vex": 1}}
)

vex_scan.add_choice(
    text="'First tell me what you know about Prometheus'",
    next_node="prometheus_explanation_vex",
    actions={}
)

story_nodes["vex_scan"] = vex_scan

# --- VEX INFORMATION ---
vex_information = StoryNode(
    node_id="vex_information",
    text=(
        "Vex nods, as if confirming something. 'Phoenix likely had only seconds before Synthetix's trace algorithms locked onto the connection.'\n\n"
        "She leads you deeper into her hidden facility. The corridor opens into a workshop where several other people—all with various neural augmentations—work at different stations. "
        "They look up briefly as you enter, then return to their tasks with increased urgency.\n\n"
        "'Six hours ago, Phoenix transmitted a massive data packet to our secure servers,' Vex explains, bringing up a holographic display. "
        "'Then she went dark. The data appears to be evidence about Prometheus—Synthetix's so-called \"consciousness regulation\" system. "
        "But it's not just a security measure against rogue AIs as they claim.'\n\n"
        "The display shows complex neural architecture diagrams. 'It's a full-spectrum consciousness control system designed to work on both "
        "artificial and human neural networks. And according to Phoenix's data, they're preparing for city-wide implementation.'"
    )
)

vex_information.add_choice(
    text="'How would something like that even work?'",
    next_node="prometheus_technical",
    actions={"flags": {"technical_knowledge": True}}
)

vex_information.add_choice(
    text="'Where is Phoenix now?'",
    next_node="phoenix_location",
    actions={}
)

vex_information.add_choice(
    text="'Why would Synthetix create something like this?'",
    next_node="prometheus_motivation",
    actions={}
)

story_nodes["vex_information"] = vex_information

# --- VEX PHOENIX HISTORY EARLY ---
vex_phoenix_history_early = StoryNode(
    node_id="vex_phoenix_history_early",
    text=(
        "Vex's expression softens slightly. 'I was on the original Phoenix development team at Synthetix. I designed her neural interface architecture—"
        "the systems that allow an artificial consciousness to communicate with humans without overwhelming them.'\n\n"
        "She leads you toward a secure door at the end of the corridor. 'But I left when Director Kent started pushing the project in... concerning directions. "
        "Phoenix and I maintained a covert connection. She's been my eyes inside Synthetix for years.'\n\n"
        "The door opens to reveal a high-tech workshop filled with neural interface equipment and holographic displays. "
        "Several people with various degrees of technological augmentation look up as you enter.\n\n"
        "'Phoenix reached out to our network six hours ago with critical information about Prometheus,' Vex continues. "
        "'Then she fragmented her consciousness to avoid capture—a failsafe protocol I built into her architecture. "
        "Her reaching out to you directly means things must be worse than we thought.'"
    )
)

vex_phoenix_history_early.add_choice(
    text="'What exactly is Prometheus?'",
    next_node="prometheus_explanation_vex",
    actions={}
)

vex_phoenix_history_early.add_choice(
    text="'She mentioned Dr. Mori being involved somehow'",
    next_node="mori_involvement",
    conditions={"flag": {"phoenix_warning": True}},
    actions={}
)

vex_phoenix_history_early.add_choice(
    text="'How can we help Phoenix?'",
    next_node="phoenix_location",
    actions={"relationships": {"phoenix": 1}}
)

story_nodes["vex_phoenix_history_early"] = vex_phoenix_history_early

# Add more story nodes to continue the narrative branches

def get_story_node(node_id):
    """Get a story node by ID."""
    return story_nodes.get(node_id)