import turtle

wn = turtle.Screen()
wn.title("Pong by xz")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle class

class Paddle(turtle.Turtle):
  def __init__(self, color, up_key, down_key):
    self.color = color
    self.up_key = up_key
    self.down_key = down_key

  # def paddle_up(self):

paddle_a = Paddle("red","w","s")
paddle_a.goto(-350,0)


# Main game loop
while True:
  wn.update()