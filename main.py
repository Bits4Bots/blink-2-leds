def on_button_pressed_a():
    basic.pause(100)
    led.plot(0, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
