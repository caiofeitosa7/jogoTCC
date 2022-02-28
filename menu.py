import pygame
import pygamepopup
from pygamepopup.components import Button, InfoBox, TextElement
from pygamepopup.menu_manager import MenuManager

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500

class MainMenuScene:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.menu_manager = MenuManager(screen)
        self.exit_request = False

        self.create_main_menu_interface()

    def create_main_menu_interface(self):
        main_menu = InfoBox(
            "Menu Principal",
            [
                [
                    Button(
                        title="Personagens",
                        callback=lambda: self.menu_personagens(),
                    )
                ],
                [Button(title="Exit", callback=lambda: self.exit())],
            ],
            has_close_button=False,
        )
        self.menu_manager.open_menu(main_menu)

    def menu_personagens(self):
        other_menu = InfoBox(
            "Personagens",
            [
                [
                    TextElement(
                        text="The text content of a menu is automatically splitted in multiple "
                        "part "
                        "to fit in the box. To add a new paragraph, just create another "
                        "TextElement."
                    )
                ]
            ],
            width=300,
        )
        self.menu_manager.open_menu(other_menu)

    def exit(self):
        self.exit_request = True

    def display(self) -> None:
        self.menu_manager.display()

    def motion(self, position: pygame.Vector2) -> None:
        self.menu_manager.motion(position)

    def click(self, button: int, position: pygame.Vector2) -> bool:
        self.menu_manager.click(button, position)
        return self.exit_request