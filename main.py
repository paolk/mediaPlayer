import sys
import os

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QGridLayout, QLabel, QWidget, QPushButton

from lib.config import *
from bin.gui_movie import *


logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def get_movies():
    """
    creates a list out of directory files
    :return: list
    """
    return [thumb for thumb in os.listdir(DEV_THUMB)]


class MoviePlayer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        logger.debug(f'[{__name__}] - Start')

        self.movie_list = get_movies()

        self.dock_area = QDockWidget(self)
        self.dock_area_container = QWidget()
        self.dock_area.setWidget(self.dock_area_container)
        self.dock_area_container_grid = QGridLayout()
        self.dock_area_container.setLayout(self.dock_area_container_grid)
        self.dockLayout()

    def dockLayout(self):
        logger.debug(f'[{__name__}] - Creating Dock area')
        # --- dock definitions -------------------------------------------------------
        self.dock_area.setTitleBarWidget(QLabel("Title bar"))
        self.dock_area.setGeometry(0, 0, (GUI_WIDTH + 50), DOCK_HEADER_HEIGHT)
        self.dock_area.setStyleSheet(f"background: {BG_COLOR1};")
        self.dock_area.setFeatures(QDockWidget.DockWidgetClosable)
        self.dock_area.setAllowedAreas(Qt.TopDockWidgetArea)

        # ---Layout dock area container-----------------------------------------------
        pix_logo = QPixmap('images/film_strip.jpeg')
        pix_logo = pix_logo.scaled(QSize(60, 100))

        lbl_logo = QLabel()
        lbl_logo.setPixmap(pix_logo)

        btn_set_movies = QPushButton("Start Movies")
        btn_set_movies.clicked.connect(self.btn_action)

        self.dock_area_container_grid.addWidget(lbl_logo, 0, 0, 4, 1)
        self.dock_area_container_grid.addWidget(QLabel("To be filled"), 0, 1, 1, 4)
        self.dock_area_container_grid.addWidget(btn_set_movies, 3, 1, 1, 1)

    def btn_action(self):
        sender = self.sender().text()
        logger.debug(f'[{__name__}] - Button clicked: {sender}')

        if sender == "Start Movies":
            self.setCentralWidget(GuiMovie(self.movie_list))


app = QApplication(sys.argv)
medPlayer = MoviePlayer()
medPlayer.show()
medPlayer.setGeometry(500, 200, GUI_WIDTH, GUI_HEIGHT)
medPlayer.setWindowTitle("Media Player")
sys.exit(app.exec_())
