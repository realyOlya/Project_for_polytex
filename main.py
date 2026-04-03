from core_game.game_engine import GameEngine
from core_game.event_handler import EventHandler

def main():
    event_handler = EventHandler()
    game = GameEngine(event_handler)
    game.run()

if __name__ == "__main__":
    main()