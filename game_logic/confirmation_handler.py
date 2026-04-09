class ConfirmationHandler:
    """
    Управляет процессом подтверждения выбора.
    Не создаёт отдельного окна, а меняет состояние UI в текущей сцене.
    """
    def __init__(self):
        self.is_waiting = False          # ожидается ли подтверждение
        self.pending_choice = None       # текст выбранной кнопки
        self.on_confirm_callback = None  # функция, вызываемая при подтверждении

    def request_confirmation(self, choice_text: str, on_confirm):
        """
        Запускает ожидание подтверждения.
        :param choice_text: текст, который выбрал пользователь (например, название кнопки)
        :param on_confirm: функция, которая будет вызвана при нажатии «Да»
        """
        self.is_waiting = True
        self.pending_choice = choice_text
        self.on_confirm_callback = on_confirm

    def confirm(self):
        """Вызывается при положительном ответе пользователя."""
        if self.is_waiting and self.on_confirm_callback:
            self.on_confirm_callback(self.pending_choice)
        self.reset()

    def cancel(self):
        """Вызывается при отрицательном ответе или отмене."""
        self.reset()

    def reset(self):
        """Сбрасывает состояние подтверждения."""
        self.is_waiting = False
        self.pending_choice = None
        self.on_confirm_callback = None
