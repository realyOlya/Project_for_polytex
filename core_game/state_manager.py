class StateManager:
    def __init__(self):
        self.progress = {
            "current_scene": None,
            "flags": {},
            "inventory": []
        }

    def save(self, filepath):
        pass  # сохранение прогресса

    def load(self, filepath):
        pass  # загрузка прогресса