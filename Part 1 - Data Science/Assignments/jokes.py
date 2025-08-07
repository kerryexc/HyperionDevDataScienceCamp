import random

def generate_joke():
  jokes = [
      "Why did the scarecrow win an award? Because he was outstanding in his field!",
      "I told my wife she was drawing her eyebrows too high. She looked surprised.",
      "What do you call a factory that makes good products? Satisfactory.",
      "Why did the student eat his homework? Because the teacher told him it was a piece of cake!",
      "I'm so good at sleeping, I can do it with my eyes closed."
  ]
  return random.choice(jokes)

# Example usage:
print(generate_joke())