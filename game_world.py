world = [[],[],[]]

def add_object(obj, depth = 0):
    world[depth].append(obj)

def remove_object(obj):
    for layer in world:
        if obj in layer:
            layer.remove(obj)
            return

# game logic
def update():
    for layer in world:
        # 업데이트 중 객체가 제거되어도 다음 객체를 건너뛰지 않는다.
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()
