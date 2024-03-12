import keyboard

pasahitza = "0080"
while True:
    if input("Pasahitza sartu: ") == pasahitza:
        print(f"Giltzarrapoa desblokeatuta! Pasahitza {pasahitza} da")
        keyboard.press("space")
        break
