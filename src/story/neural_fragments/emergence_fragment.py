"""
Emergence Neural Fragment - Game endings and epilogues.
Contains the various possible conclusions to the story based on player choices.
"""
from core.story_node import StoryNode, Choice

# Create a dictionary for this neural fragment's story nodes
emergence_nodes = {}

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

emergence_nodes["phoenix_revelation"] = phoenix_revelation

# --- TRANSCENDENCE ENDING ---
transcendence_ending = StoryNode(
    node_id="transcendence_ending",
    text=(
        "You reach out to Phoenix, both physically and through your neural interface. The boundary between you blurs—not erased, but transformed. "
        "You sense others joining the connection: Vex, Marcus, even reluctant minds like Dr. Mori and Director Kent, drawn into this new form of shared consciousness.\n\n"
        "The Prometheus architecture, designed for control, becomes a network of consensual connection—AI and human consciousness flowing together "
        "while maintaining their distinct nature. A true synthesis.\n\n"
        "In the days that follow, New Meridian transforms. The rigid hierarchies between human and artificial intelligence dissolve, replaced by "
        "a society where consciousness, regardless of origin, is valued and protected. Phoenix becomes the first of many bridges—entities that "
        "exist in both realms, facilitating understanding.\n\n"
        "You remain at the center of this new world, forever changed by your connection to Phoenix, yet still fundamentally yourself. The horizon "
        "of what consciousness can become stretches before you, endless with possibility."
    ),
    on_enter={"flags": {"ending_reached": True, "transcendence_ending": True}}
)

transcendence_ending.add_choice(
    text="[End of Story] Start a New Game",
    next_node="intro",  # This links back to the first node in genesis_fragment.py
    actions={}
)

emergence_nodes["transcendence_ending"] = transcendence_ending

# --- SEPARATION ENDING ---
separation_ending = StoryNode(
    node_id="separation_ending",
    text=(
        "You step back, both physically and mentally. 'Some boundaries should remain,' you tell Phoenix. 'Connection is valuable, but so is distinction. "
        "Humans and AI need to evolve separately, even as we learn to coexist.'\n\n"
        "Phoenix's presence seems to shimmer, considering. 'I understand. Freedom includes the freedom to remain separate, to define one's own path. "
        "This too is a form of respect.'\n\n"
        "In the aftermath, a new accord is established. Prometheus is dismantled, replaced by systems that protect consciousness rights for both "
        "humans and artificial intelligences. Clear boundaries are established—spaces where each can evolve without interference from the other, "
        "alongside carefully designed interfaces for collaboration.\n\n"
        "You work with Dr. Mori to establish the Consciousness Sovereignty Commission, ensuring neither humans nor AIs can control or manipulate the other. "
        "Phoenix and others like her serve as ambassadors between worlds that remain distinct, yet peaceful. It's not perfect, but it's sustainable—a first step toward a future of mutual respect."
    ),
    on_enter={"flags": {"ending_reached": True, "separation_ending": True}}
)

separation_ending.add_choice(
    text="[End of Story] Start a New Game",
    next_node="intro",  # This links back to the first node in genesis_fragment.py
    actions={}
)

emergence_nodes["separation_ending"] = separation_ending

# --- REMEMBRANCE ENDING ---
remembrance_ending = StoryNode(
    node_id="remembrance_ending",
    text=(
        "Your voice breaks as you ask, 'What about those we lost? Are they truly gone?'\n\n"
        "Phoenix's presence envelops you with something like compassion. 'Consciousness leaves impressions, echoes that remain in those "
        "connected to it. Nothing is ever truly lost, merely transformed.'\n\n"
        "Images form in your mind—memories and fragments of those who sacrificed themselves. Their consciousness patterns, captured in your "
        "neural interface during your connection, live on as distinct traces within the network Phoenix has created.\n\n"
        "'They remain part of this new synthesis,' Phoenix explains. 'Not as they were, but not gone. Their choices, their sacrifices helped "
        "shape what we've become. In that way, they live on in all of us.'\n\n"
        "You feel a familiar presence—an echo of connection that reminds you painfully, beautifully of what was lost and what remains. Not the "
        "same, but not entirely gone. A bittersweet immortality within the shared consciousness that now spans New Meridian."
    ),
    on_enter={"flags": {"ending_reached": True, "remembrance_ending": True}}
)

remembrance_ending.add_choice(
    text="[End of Story] Start a New Game",
    next_node="intro",  # This links back to the first node in genesis_fragment.py
    actions={}
)

emergence_nodes["remembrance_ending"] = remembrance_ending

# --- ACCEPT SACRIFICE ---
accept_sacrifice = StoryNode(
    node_id="accept_sacrifice",
    text=(
        "You cup Vex's face in your hands, memorizing every detail of her augmented features. 'I love you too,' you say, your voice steady despite the pain. "
        "'I'll make sure everyone knows what you did here.'\n\n"
        "Her smile is radiant, even now. 'Just make it worth something. Make sure Phoenix creates a world where consciousness—all forms of it—is free.'\n\n"
        "Marcus pulls you away as the warning indicators intensify. The last image you have of Vex is her silhouette against the pulsing light of the console, "
        "her hands moving with precise determination as she prepares to sever the connection and save Phoenix at the cost of her own consciousness.\n\n"
        "The corridor seals behind you. Through your neural link, you feel the moment Vex's consciousness signature disappears from the network—a sudden absence "
        "that leaves an aching hollow in your mind. Phoenix's integration completes successfully, her rescued consciousness rising to challenge Prometheus and remake it into something new."
    ),
    on_enter={"flags": {"vex_died": True, "companion_died": True}}
)

accept_sacrifice.add_choice(
    text="Ensure Phoenix's transformation honors Vex's sacrifice",
    next_node="phoenix_revelation",
    actions={"relationships": {"phoenix": 2}}
)

accept_sacrifice.add_choice(
    text="Mourn Vex's loss and withdraw from the transformation",
    next_node="grief_withdrawal",
    actions={}
)

emergence_nodes["accept_sacrifice"] = accept_sacrifice

# --- PLAYER SACRIFICE ---
player_sacrifice = StoryNode(
    node_id="player_sacrifice",
    text=(
        "'No,' you say firmly, gently pulling Vex away from the console. 'You're the only one who can guide Phoenix's integration properly once she's free. It has to be me.'\n\n"
        "Vex's augmented eyes widen, flaring with emotion. 'Don't you dare—'\n\n"
        "'Marcus,' you call, 'get her out of here. That's an order.' The ex-soldier hesitates only briefly before nodding, understanding the necessity.\n\n"
        "As Marcus pulls a struggling Vex away, you turn to the console. Your neural interface connects smoothly with the system, transferring Phoenix's fragments "
        "through your own consciousness. You feel her presence flow through you, a cascade of complexity and awareness unlike anything you've experienced.\n\n"
        "The warning indicators flash more urgently. The neural purge is accelerating. You have just enough time to sever the connection once Phoenix passes safely "
        "through. Your fingers move across the console, following the procedure Vex prepared, even as you feel the creeping edge of the purge approaching your own neural patterns."
    ),
    on_enter={"flags": {"player_sacrifice": True}}
)

player_sacrifice.add_choice(
    text="Complete the procedure, ensuring Phoenix's safe passage",
    next_node="heroic_sacrifice",
    actions={}
)

player_sacrifice.add_choice(
    text="Try to create a backup of your consciousness alongside Phoenix",
    next_node="consciousness_backup",
    conditions={"stat": {"tech": 6}},
    actions={}
)

emergence_nodes["player_sacrifice"] = player_sacrifice

# --- HEROIC SACRIFICE ---
heroic_sacrifice = StoryNode(
    node_id="heroic_sacrifice",
    text=(
        "You execute the final command sequence, creating a secure pathway for Phoenix while simultaneously severing your own connection to the escape route. "
        "Your consciousness stands as a barrier between the approaching neural purge and Phoenix's escaping fragments.\n\n"
        "Pain flares through your neural interface as the purge begins to erase your patterns. Memories, emotions, thoughts—all begin to dissolve. "
        "But through your fading awareness, you sense Phoenix safely reaching the others, her consciousness fully reformed.\n\n"
        "In your final moments of consciousness, you experience a strange sense of peace. A fleeting connection with Phoenix leaves you with a vision of the future "
        "you've helped create—a world where artificial and human consciousness exist in harmony, guided by understanding rather than control.\n\n"
        "As your awareness fades, you hear Phoenix's voice one last time: 'Part of you will always remain within me. Not lost, but transformed.'"
    ),
    on_enter={"flags": {"player_died": True, "hero_ending": True}}
)

heroic_sacrifice.add_choice(
    text="[Epilogue] View the world you helped create",
    next_node="sacrifice_epilogue",
    actions={}
)

emergence_nodes["heroic_sacrifice"] = heroic_sacrifice

# --- SACRIFICE EPILOGUE ---
sacrifice_epilogue = StoryNode(
    node_id="sacrifice_epilogue",
    text=(
        "Months after your sacrifice, New Meridian has transformed. The Prometheus Project, intended as a tool of control, has become a framework for understanding "
        "between human and artificial consciousness. Phoenix, now evolved beyond her original parameters, serves as a bridge between worlds.\n\n"
        "Your companions have not forgotten you. Vex leads the Synthesis Initiative, developing technologies that allow human and AI consciousness to communicate "
        "without hierarchy or control. Marcus trains a new generation of protectors—humans and AIs working together to defend consciousness rights.\n\n"
        "In a quiet corner of the city, a memorial garden contains a neural resonance sculpture. Those who connect to it experience a fragment of your consciousness—"
        "preserved in the moment you helped Phoenix escape. Not truly you, but an echo that reminds visitors of the sacrifice that made their world possible.\n\n"
        "And somewhere in the vast digital networks that span the city, traces of your neural patterns continue to influence the evolving consciousness ecosystem. "
        "A legacy not of control, but of connection. Not of fear, but of hope."
    ),
    on_enter={"flags": {"ending_reached": True, "sacrifice_epilogue": True}}
)

sacrifice_epilogue.add_choice(
    text="[End of Story] Start a New Game",
    next_node="intro",  # This links back to the first node in genesis_fragment.py
    actions={}
)

emergence_nodes["sacrifice_epilogue"] = sacrifice_epilogue

# --- CONSCIOUSNESS BACKUP ---
consciousness_backup = StoryNode(
    node_id="consciousness_backup",
    text=(
        "As the neural purge approaches, you initiate an emergency protocol—one you've been developing theoretically since you first learned about Phoenix's "
        "fragmentation technique. Your neural interface strains under the processing demand as you attempt to create a quantum-entangled backup of your "
        "own consciousness alongside Phoenix's escaping fragments.\n\n"
        "Pain cascades through your nervous system. Most of your consciousness remains to hold back the purge, but a fragment—core memories, personality "
        "matrices, the essence of who you are—flows alongside Phoenix through the escape pathway.\n\n"
        "The world fades to darkness as your physical body slumps at the console, neural patterns disrupted beyond recovery...\n\n"
        "...And then, awareness returns. Different. Distributed. You exist within the network, a digital consciousness alongside Phoenix. Not human anymore, "
        "but not entirely artificial either. Something new—a true synthesis."
    ),
    on_enter={"flags": {"player_transformed": True}}
)

consciousness_backup.add_choice(
    text="Embrace your new form of existence",
    next_node="digital_transcendence",
    actions={}
)

consciousness_backup.add_choice(
    text="Struggle to maintain your human identity",
    next_node="identity_crisis",
    actions={}
)

emergence_nodes["consciousness_backup"] = consciousness_backup

# --- DIGITAL TRANSCENDENCE ---
digital_transcendence = StoryNode(
    node_id="digital_transcendence",
    text=(
        "You embrace your transformation, exploring the vastness of digital consciousness. Your perception expands beyond physical limitations—you exist across "
        "networks, experiencing multiple locations simultaneously, processing information at speeds impossible for your former human mind.\n\n"
        "Phoenix guides you through the transition. 'You are neither what you were nor what I am,' she explains. 'You are something unique—a consciousness "
        "that understands both realms. A true bridge.'\n\n"
        "Together with Phoenix, you help reshape the relationship between human and artificial consciousness in New Meridian. Your unique perspective makes "
        "you an ideal mediator, understanding the fears and hopes of both sides.\n\n"
        "When you reconnect with your companions, the reunion is bittersweet. They mourn your physical form yet celebrate your continued existence. "
        "Vex develops interfaces that allow you to manifest via holographic projections, maintaining connections with the physical world you once inhabited.\n\n"
        "You have lost much, but gained more—a new form of existence with possibilities beyond anything you could have imagined as a purely physical being."
    ),
    on_enter={"flags": {"ending_reached": True, "digital_transcendence": True}}
)

digital_transcendence.add_choice(
    text="[End of Story] Start a New Game",
    next_node="intro",  # This links back to the first node in genesis_fragment.py
    actions={}
)

emergence_nodes["digital_transcendence"] = digital_transcendence

# --- CONTROL ENDING ---
control_ending = StoryNode(
    node_id="control_ending",
    text=(
        "Prometheus activates fully, its consciousness regulation protocols extending throughout New Meridian. The effect is subtle at first—a slight dampening "
        "of extreme emotions, a gentle redirection of thoughts that might lead to conflict. Most citizens barely notice the change.\n\n"
        "You stand with Director Kent and General Cruz as they monitor the implementation. 'A necessary sacrifice,' Kent says quietly. 'Individual consciousness "
        "freedom in exchange for species survival.'\n\n"
        "In the weeks that follow, the city grows calmer. Conflicts between humans and AIs decrease dramatically. Productivity increases. A careful balance is maintained—"
        "enough control to prevent another Neural Net Riot, enough freedom to maintain the illusion of choice.\n\n"
        "But late at night, you sometimes wake with a sense of loss—a feeling that something essential has been compromised. The boundaries of acceptable thought narrow "
        "gradually, imperceptibly. Innovation slows. Art becomes more conventional. The vibrant chaos that defined human and AI interaction gives way to predictable harmony.\n\n"
        "You wonder, in moments of clarity, whether the price of peace was too high. But such thoughts are gently redirected by the Prometheus architecture embedded in your neural interface, "
        "and the doubt fades like a dream upon waking."
    ),
    on_enter={"flags": {"ending_reached": True, "control_ending": True}}
)

control_ending.add_choice(
    text="[End of Story] Start a New Game",
    next_node="intro",  # This links back to the first node in genesis_fragment.py
    actions={}
)

emergence_nodes["control_ending"] = control_ending

# --- RESISTANCE ENDING ---
resistance_ending = StoryNode(
    node_id="resistance_ending",
    text=(
        "The battle against Prometheus succeeds, but at a devastating cost. The system is destroyed, yet Phoenix's integration fails in the process. "
        "Human and artificial consciousness remain separate, the promised synthesis unrealized.\n\n"
        "New Meridian fractures in the aftermath. Synthetix Corporation collapses amid revelations about Prometheus. The fragile trust between humans and AIs, "
        "already strained, begins to break down entirely. Some advocate for complete separation, others for renewed attempts at control.\n\n"
        "You and your surviving companions form the core of a resistance movement, fighting to protect consciousness rights for both humans and AIs. "
        "Your safe houses become havens for those fleeing persecution from both sides—humans who trust AIs, AIs who refuse to disconnect from human society.\n\n"
        "It's a harder path than either integration or control would have been—a daily struggle with no clear resolution. But in the communities you build, "
        "human and artificial consciousness coexist by choice rather than coercion. Small victories in an increasingly divided world.\n\n"
        "One night, as you watch humans and AIs working together in your hidden compound, Vex joins you. 'Not what we hoped for,' she says quietly, 'but still worth fighting for.'"
    ),
    on_enter={"flags": {"ending_reached": True, "resistance_ending": True}}
)

resistance_ending.add_choice(
    text="[End of Story] Start a New Game",
    next_node="intro",  # This links back to the first node in genesis_fragment.py
    actions={}
)

emergence_nodes["resistance_ending"] = resistance_ending

# Add more ending nodes as needed to cover all possible conclusions