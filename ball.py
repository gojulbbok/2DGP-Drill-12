from pico2d import get_canvas_width, load_image
import game_world


class Ball:
    image = None

    def __init__(self, x, y, direction):
        self.x, self.y = x, y
        self.direction = direction
        self.speed = 10
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')

    def update(self):
        self.x += self.direction * self.speed
        # 공이 화면 밖으로 완전히 나가면 게임 월드에서 제거한다.
        if self.x < -11 or self.x > get_canvas_width() + 11:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
