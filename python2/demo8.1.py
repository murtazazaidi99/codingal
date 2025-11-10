class bird:
    def speak(self):
        print("birds are sounds")

class eagle(bird):
    def speak(self):
        print("eagle says:hello!")

for bird in [eagle(),bird()]:
    bird.speak()
