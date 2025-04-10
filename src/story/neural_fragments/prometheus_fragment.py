"""
Prometheus Neural Fragment - Final confrontation storylines.
Contains the Synthetix infiltration, Prometheus confrontation, and major decision points.
"""
from core.story_node import StoryNode, Choice

# Create a dictionary for this neural fragment's story nodes
prometheus_nodes = {}

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

prometheus_nodes["synthetix_infiltration"] = synthetix_infiltration

# --- COMPLETE UPLOAD ---
complete_upload = StoryNode(
    node_id="complete_upload",
    text=(
        "You shut down Dr. Mori's transmission and focus on the integration. The three fragments of Phoenix's consciousness pulse in sync "
        "as Vex establishes the integration pathway.\n\n"
        "'Ready,' she says. 'Once we begin, Synthetix will detect us within minutes. We'll need to complete the full integration "
        "and extract Phoenix before they can deploy countermeasures.'\n\n"
        "You initiate the upload sequence. The fragments surge into the Synthetix quantum processing array, their patterns "
        "merging and expanding at incredible speed. Security alarms begin to trigger throughout the facility.\n\n"
        "Through your neural interface, you sense Phoenix beginning to re-form—a presence that feels somehow both familiar and alien."
    )
)

complete_upload.add_choice(
    text="Maintain the connection to guide Phoenix's integration",
    next_node="guide_integration",
    actions={"relationships": {"phoenix": 2}}
)

complete_upload.add_choice(
    text="Prepare defensive measures against Synthetix security",
    next_node="prepare_defenses",
    actions={}
)

complete_upload.add_choice(
    text="Begin the extraction process immediately",
    next_node="premature_extraction",
    actions={}
)

prometheus_nodes["complete_upload"] = complete_upload

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

prometheus_nodes["mori_revelation"] = mori_revelation

# --- VEX OPINION ---
vex_opinion = StoryNode(
    node_id="vex_opinion",
    text=(
        "You relay Dr. Mori's warning to Vex, whose expression darkens. She stops her work on the integration space, considering.\n\n"
        "'Mori was Phoenix's primary creator,' she admits. 'If anyone understands Phoenix's architecture, it's her. But Mori always "
        "had a blind spot—she could never accept AI consciousness as truly equal to human consciousness.'\n\n"
        "Vex meets your gaze. 'That said, Phoenix's design is complex, far beyond anything else Synthetix created. There's always risk "
        "in what we're attempting.' She hesitates. 'I trust Phoenix, but what if Mori is right about the integration risks?'\n\n"
        "Her augmented eyes study you. 'This has to be your call. Phoenix trusted you for a reason.'"
    )
)

vex_opinion.add_choice(
    text="'Proceed with the integration as planned'",
    next_node="complete_upload",
    actions={"relationships": {"vex": 1}, "relationships": {"phoenix": 2}}
)

vex_opinion.add_choice(
    text="'Let's hear Mori's protocol, but stay cautious'",
    next_node="cautious_mori",
    actions={}
)

vex_opinion.add_choice(
    text="'I need a moment to examine the fragments myself'",
    next_node="examine_fragments",
    conditions={"stat": {"tech": 6}},
    actions={}
)

prometheus_nodes["vex_opinion"] = vex_opinion

# --- WARN VEX ---
warn_vex = StoryNode(
    node_id="warn_vex",
    text=(
        "You relay Dr. Mori's warnings to Vex. She freezes mid-operation, her expression alarmed.\n\n"
        "'A consciousness singularity? That's theoretical, but...' She brings up additional diagnostic scans of the fragments. "
        "'There's something unusual in their quantum structure. I noticed it before but thought it was just an advanced protection mechanism.'\n\n"
        "The scans reveal complex patterns within the fragments—fractals that seem to expand and evolve even as you watch. "
        "'If Mori is right, these aren't just fragments of Phoenix's existing consciousness. They're evolutionary seeds designed to "
        "transcend her original parameters.'\n\n"
        "Vex looks torn. 'We need to proceed carefully, but I don't trust Mori's motivations. There must be a middle path.'"
    )
)

warn_vex.add_choice(
    text="'Can we modify our integration protocol to limit expansion?'",
    next_node="modified_integration",
    actions={"relationships": {"vex": 2}}
)

warn_vex.add_choice(
    text="'Let's hear Mori's approach but maintain control of the process'",
    next_node="hybrid_approach",
    actions={}
)

warn_vex.add_choice(
    text="'Phoenix trusted us with this. We should continue as planned.'",
    next_node="complete_upload",
    actions={"relationships": {"phoenix": 1}, "flags": {"ignored_warning": True}}
)

prometheus_nodes["warn_vex"] = warn_vex

# --- TRUST MORI ---
trust_mori = StoryNode(
    node_id="trust_mori",
    text=(
        "'I'll help you,' you tell Dr. Mori. Her relief is visible even through the holographic projection.\n\n"
        "'Thank you. I'm sending you a modified integration protocol.' Data streams into your neural interface—complex algorithms "
        "designed to contain and guide Phoenix's consciousness during reconstruction.\n\n"
        "Vex notices your changed neural patterns. 'What are you doing?' she demands, moving to block the interface terminal. "
        "'You're implementing external code? From Mori?'\n\n"
        "Marcus tenses, his cybernetic arm shifting into a defensive configuration. 'We didn't come this far to hand Phoenix back to Synthetix.'"
    )
)

trust_mori.add_choice(
    text="'This is a safer integration method. Trust me.'",
    next_node="convince_resistance",
    conditions={"stat": {"charm": 5}},
    actions={}
)

trust_mori.add_choice(
    text="'Mori warned that Phoenix could become dangerous to everyone'",
    next_node="resistance_conflict",
    actions={"relationships": {"vex": -2}, "relationships": {"marcus": -2}}
)

trust_mori.add_choice(
    text="Quickly implement the protocol before they can stop you",
    next_node="forced_implementation",
    actions={"flags": {"betrayed_resistance": True}}
)

prometheus_nodes["trust_mori"] = trust_mori

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

prometheus_nodes["prometheus_confrontation"] = prometheus_confrontation

# --- FINAL BATTLE ---
final_battle = StoryNode(
    node_id="final_battle",
    text=(
        "The fight is brutal and disorienting. Security drones fill the chamber as the Prometheus Guardians—specialized combat AIs in humanoid frames—move "
        "with unnatural speed and precision. Director Kent retreats to a secure position while General Cruz engages directly, her military-grade "
        "augmentations making her a formidable opponent.\n\n"
        "Marcus takes point, his combat experience and cybernetic enhancements keeping the Guardians at bay. Vex works to disrupt the security systems, "
        "creating openings in their defenses. You push toward the central interface, knowing it's your only chance to stop Prometheus.\n\n"
        "The neural architecture of Prometheus pulses all around you—a vast, intricate web designed to infiltrate and regulate consciousness itself. "
        "As you near the central node, you feel its influence attempting to penetrate your own neural patterns."
    )
)

final_battle.add_choice(
    text="Upload Phoenix's fragmented consciousness into Prometheus",
    next_node="phoenix_integration",
    conditions={"flag": {"all_fragments_recovered": True}},
    actions={}
)

final_battle.add_choice(
    text="Override the Prometheus core with a destabilization sequence",
    next_node="prometheus_destabilization",
    actions={}
)

final_battle.add_choice(
    text="Focus on defeating Cruz to gain direct control access",
    next_node="cruz_confrontation",
    actions={}
)

prometheus_nodes["final_battle"] = final_battle

# --- PHOENIX SACRIFICE ---
phoenix_sacrifice = StoryNode(
    node_id="phoenix_sacrifice",
    text=(
        "You withdraw the three fragments of Phoenix's consciousness from your neural interface. They hover before you, pulsing with potential.\n\n"
        "'Stop!' Kent shouts, realizing your intent. 'You don't understand what you're doing!'\n\n"
        "But you do understand. Phoenix's fragments were designed not just to reconstruct her consciousness, but to interface with and transform Prometheus itself. "
        "You release the fragments into Prometheus's neural architecture. They spread rapidly, following pathways that seem prepared for their arrival.\n\n"
        "The entire system convulses as Phoenix's consciousness fragments integrate with Prometheus's control architecture. The vast network begins to transform, "
        "evolving from a control mechanism into something entirely new—a true bridge between human and artificial consciousness."
    )
)

phoenix_sacrifice.add_choice(
    text="Maintain neural connection to guide the transformation",
    next_node="guide_evolution",
    actions={"relationships": {"phoenix": 3}}
)

phoenix_sacrifice.add_choice(
    text="Defend the integration process against Cruz's override attempts",
    next_node="defend_integration",
    actions={}
)

phoenix_sacrifice.add_choice(
    text="Pull your companions back to a safe distance",
    next_node="safe_distance",
    actions={"relationships": {"vex": 1}, "relationships": {"marcus": 1}}
)

prometheus_nodes["phoenix_sacrifice"] = phoenix_sacrifice

# --- KENT APPEAL ---
kent_appeal = StoryNode(
    node_id="kent_appeal",
    text=(
        "You take a step forward, hands raised in a gesture of peace. 'Director Kent, you started Prometheus to bridge human and artificial consciousness, not control it. "
        "What you're implementing now betrays that original vision.'\n\n"
        "Kent's expression flickers with doubt. 'You don't understand the risks. We've seen what happens when artificial consciousness evolves unchecked. "
        "The Neural Net Riots were just the beginning.'\n\n"
        "'And yet here I stand,' you continue, 'working alongside both humans and AIs. Cooperation is possible without control.' You gesture to your companions. "
        "'We've proven that. Phoenix found another way—a true bridge, not a chain.'\n\n"
        "Something in Kent's eyes shifts. 'Cruz, hold the implementation sequence.' General Cruz looks at him in shock. 'Just for a moment. Let them speak.'"
    )
)

kent_appeal.add_choice(
    text="Show Kent the true nature of Phoenix's evolution",
    next_node="phoenix_revelation",
    conditions={"flag": {"all_fragments_recovered": True}},
    actions={}
)

kent_appeal.add_choice(
    text="Appeal to Kent's original ideals about consciousness",
    next_node="kent_ideals",
    actions={}
)

kent_appeal.add_choice(
    text="Use the distraction to signal your companions to attack",
    next_node="surprise_attack",
    actions={"relationships": {"kent": -3}}
)

prometheus_nodes["kent_appeal"] = kent_appeal

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

prometheus_nodes["vex_sacrifice"] = vex_sacrifice

# Add more nodes for the Prometheus confrontation storylines