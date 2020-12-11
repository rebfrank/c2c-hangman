class DrawHangman: 
    def __init__(self):
        self.hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]
        self.num_wrong_guesses_allowed = len(self.hangman_parts)
        self.words = [
            "apple",
            "butterfly",
            "car",
            "pajama",
            "kayak",
            "zigzag",
            "zombie",
            "oxygen",
            "able",
            "baby",
            "lock",
            "ornament",
            "quality",
            "liquid",
            "suggestion",
            "weather",
            "twist"
            ]

    def draw_hangman(self, num_wrong_guesses):
        if num_wrong_guesses > self.num_wrong_guesses_allowed:
            num_wrong_guesses = self.num_wrong_guesses_allowed

        hangman_characters = {
            "head" : "  O",
            "left arm" : " /",
            "torso" : "|",
            "right arm" : "\\",
            "left leg" : " /",
            "right leg" : " \\"
        }
        hangman_newlines = [ "head", "right arm", "right leg" ]

        output = " _____\n |   |\n | "
        num_newlines = 0
        for i in range(num_wrong_guesses):
            output = output + hangman_characters[self.hangman_parts[i]]
            if self.hangman_parts[i] in hangman_newlines:
                output = output + "\n | "
                num_newlines = num_newlines + 1
        for i in range(len(hangman_newlines) - num_newlines):
            output = output + "\n |"
        output = output + "____\n\n"
        print(output)

# Below lines are just to be used for running
drawhangman = DrawHangman()
drawhangman.draw_hangman(5)