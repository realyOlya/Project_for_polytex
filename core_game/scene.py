class Scene:
    """Базовый класс для всех сцен"""

    def __init__(self, scene_manager, state_manager):
        self.scene_manager = scene_manager
        self.state_manager = state_manager

    def handle_event(self, event):
        """Обработка событий Pygame"""
        pass

    def update(self, dt):
        """Обновление логики"""
        pass

    def draw(self, screen):
        """Отрисовка на экране"""
        pass
