class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200  # ширина экрана
        self.screen_heigt = 800  # высота экрана
        self.bg_color = (18, 39, 82)

        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 200, 0)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction = 1 обозначает движение на право; а -1 на лево
        self.fleet_direction = 1
