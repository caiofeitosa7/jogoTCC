import pygame
import testaMapa
import pygamepopup
from pygamepopup.components import Button, InfoBox, TextElement
from pygamepopup.menu_manager import MenuManager
from pygamepopup.components.image_button import ImageButton

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
                [Button(
                    title="Jogar",
                    callback=lambda: self.exit())],
                [
                    Button(
                        title = "Personagens",
                        background_path = r"FrontEnd\btApagado.png",
                        background_hover_path = r"FrontEnd\btClaro.png",
                        callback=lambda: self.menu_personagens(),
                    )
                ],
                [Button(title="Sair", callback=lambda: self.exit())],
                [
                    TextElement(
                        text="                                               "
                        "                                                    "
                        "                                                    "
                    )
                ],
            ],
            background_path = r"FrontEnd\popMenu.png",
            has_vertical_separator = False,
            has_close_button=False,
        )
        self.menu_manager.open_menu(main_menu)

    def menu_personagens(self):
        other_menu = InfoBox(
            "Personagens",
            [
                [
                    TextElement(
                        text="                                               "
                        "                                               "
                        "                                               "
                        "                                               "
                        "                                               "
                        "                                               "
                    )
                ],
            ],
            width=600,
            background_path = 'FrontEnd\popPersonagens.png'
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


def menu_principal(screen):
    main_menu_scene = MainMenuScene(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                main_menu_scene.motion(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    running = not main_menu_scene.click(event.button, event.pos)
        main_menu_scene.display()
        pygame.display.update()
    pygame.quit()
    exit()
    
    
def main() -> None:
    pygame.init()
    pygame.display.set_caption("King")

    pygamepopup.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    main_menu_scene = MainMenuScene(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                main_menu_scene.motion(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    running = not main_menu_scene.click(event.button, event.pos)
        screen.fill(pygame.Color("black"))
        main_menu_scene.display()
        pygame.display.update()
    pygame.quit()
    exit()


if __name__ == "__main__":
    main()
