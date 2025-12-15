import sys
import pymunk
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QColorDialog, QSlider, QMessageBox
)
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import QTimer, Qt

class PhysicsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.W, self.H = 600, 400
        self.setFixedSize(self.W, self.H)
        self.ball_radius = 20
        self.ball_color = Qt.GlobalColor.red

        # --- Interface Qt ---
        self.btn_impulse = QPushButton("Impulsion")
        self.btn_reset = QPushButton("Réinitialiser")
        self.btn_color = QPushButton("Changer couleur")
        self.slider_gravity = QSlider(Qt.Orientation.Horizontal)
        self.slider_gravity.setMinimum(-2000)
        self.slider_gravity.setMaximum(2000)
        self.slider_gravity.setValue(-900)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.btn_impulse)
        h_layout.addWidget(self.btn_reset)
        h_layout.addWidget(self.btn_color)
        h_layout.addWidget(self.slider_gravity)

        v_layout = QVBoxLayout(self)
        v_layout.addLayout(h_layout)
        v_layout.addStretch()

        # --- Connexions ---
        self.btn_impulse.clicked.connect(self.apply_impulse)
        self.btn_reset.clicked.connect(self.reset_ball)
        self.btn_color.clicked.connect(self.choose_color)
        self.slider_gravity.valueChanged.connect(self.change_gravity)

        # --- Simulation PyMunk ---
        self.init_simulation()

        # --- Timer pour animation ---
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)
        self.timer.start(16)  # ~60 FPS

    def init_simulation(self):
        # Espace physique
        self.space = pymunk.Space()
        self.space.gravity = (0, -900)

        # --- Sol ---
        self.ground = pymunk.Segment(self.space.static_body, (0, 50), (self.W, 50), 2)
        self.ground.elasticity = 0.8
        self.ground.friction = 1.0
        self.ground.collision_type = 2  # sol
        self.space.add(self.ground)

        # --- Balle ---
        self.create_ball()

        # --- Collision PyMunk comme dans les notes ---
        self.space.on_collision(1, 2, begin=self.on_ball_hit_ground)

    def create_ball(self):
        mass = 5
        moment = pymunk.moment_for_circle(mass, 0, self.ball_radius)
        self.ball_body = pymunk.Body(mass, moment)
        self.ball_body.position = (200, 300)
        self.ball_shape = pymunk.Circle(self.ball_body, self.ball_radius)
        self.ball_shape.elasticity = 0.8
        self.ball_shape.collision_type = 1  # balle
        self.space.add(self.ball_body, self.ball_shape)

    def reset_ball(self):
        self.space.remove(self.ball_body, self.ball_shape)
        self.create_ball()

    def apply_impulse(self):
        self.ball_body.apply_impulse_at_local_point((300, 0), (0, 0))

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ball_color = color

    def change_gravity(self, value):
        self.space.gravity = (0, value)

    def on_ball_hit_ground(self, arbiter, space, data):
        # QMessageBox.information(self, "Collision", "La balle touche le sol !")
        print("rebond")
        return True

    def update_simulation(self):
        dt = 1 / 60
        self.space.step(dt)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        # Fond
        painter.fillRect(self.rect(), Qt.GlobalColor.white)

        # Sol
        painter.setBrush(QBrush(Qt.GlobalColor.gray))
        painter.drawRect(0, self.H - 50, self.W, 50)

        # Balle
        x = int(self.ball_body.position.x - self.ball_radius)
        y = int(self.H - self.ball_body.position.y - self.ball_radius)
        painter.setBrush(QBrush(self.ball_color))
        painter.drawEllipse(x, y, 2 * self.ball_radius, 2 * self.ball_radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhysicsWidget()
    window.show()
    sys.exit(app.exec())
