from gpiozero import Button
button = Button(2)
while True:
   if button.is_pressed:
        print("Button Pressed")
   else:
        print("Idle")

"""
These don’t block the flow of the program
button.when_pressed = led.on
button.when_released = led.off
Block the flow os the program
button.wait_for_press()
print("Pressed")
button.wait_for_release()
print("Released")
"""
