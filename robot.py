class Robot:
    species = "AI Companion"

    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose

    def introduce(self):
        print("Hello, I am", self.name, "!")
        print("I am a", Robot.species, "created to", self.purpose)

    def abilities(self):
        print("I can assist with learning, problem-solving, and exploring new ideas.")


robot1 = Robot("Copilot", "increase people's knowledge and understanding")

robot1.introduce()
robot1.abilities()
