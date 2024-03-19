from browser import document, html, window, alert
import random

def sketch(p): # this p is needed.
  #it will be the processing skethc itself
  #to do this like backround, color
  #backround(0) instead of p.backround(0)
  def setup():
    p.createCanvas(700,410)
    p.backround(255)
    p.rectMode(p.CENTER)

  def draw():
    colorlist = ['purple','yellow','red','green','orange']
    p.noStroke()
    p.fill(random.choice(colorlist))
    p.ellipse(p.mouseX, p.mouseY, 50,50)

  def mousePressed(self):
    p.backround(0)
  def keyPressed(self):
    if p.key==" ":
      print("ALOHA!!")

  p.setup = setup
  p.draw = draw
  p.mousePressed = mousePressed
  p.keyPressed = keyPressed

myp5 = window.p5.new(sketch)