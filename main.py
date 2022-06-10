def on_button_pressed_a():
    global isPlaying
    isPlaying = not (isPlaying)
input.on_button_pressed(Button.A, on_button_pressed_a)

isPlaying = False
isPlaying = False

def on_forever():
    while isPlaying:
        music.play_melody("E B C5 A B G A F ", 120)
basic.forever(on_forever)

def test_function():
    basic.show_icon(IconNames.HEART)
    basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)