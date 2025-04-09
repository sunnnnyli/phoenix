#!/usr/bin/env python3

import os
import sys
import time
from core.game_state import GameState
from core.game_engine import GameEngine
from ui.text_ui import TextUI

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main entry point for the Synthesis RPG game."""
    clear_screen()
    
    ui = TextUI()
    game_state = GameState()
    game_engine = GameEngine(game_state, ui)
    
    ui.display_title_screen("SYNTHESIS", "Where Humanity Meets Artificial Consciousness")
    ui.display_message("Press Enter to start your journey...")
    input()
    
    # Start the game
    game_engine.start_new_game()
    
    # Main game loop
    while game_state.is_running:
        game_engine.update()
    
    ui.display_message("Thank you for playing SYNTHESIS.")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame terminated by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1) 