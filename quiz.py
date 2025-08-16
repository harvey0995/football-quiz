print("⚽ Welcome to the Football Quiz! ⚽\n")

score = 0

# Question 1

print("1. Who won the FIFA World Cup 2022?")
print("a) Argentina\n b) France\n c) Brazil\n d) Germany")

answer = input("Your answer: ")
if answer.lower() == "a":
    print("✅ Correct!\n")
    score = score + 1
else:
    print("❌ Wrong! The correct answer was Argentina\n")

# Question 2

print("2. Which player is called 'CR7'?")
print("a) Lionel Messi\n b) Cristiano Ronaldo\n c) Neymar\n d) Mbappe")

answer = input("Your answer: ")
if answer.lower() == "b":
    print("✅ Correct!\n")
    score = score + 1
else:
    print("❌ Wrong! The correct answer was Cristiano Ronaldo\n")

# Question 3

print("3. Which country has won the most World Cups?")
print("a) Brazil\n b) Germany\n c) Italy\n d) Argentina")

answer = input("Your answer: ")
if answer.lower() == "a":
    print("✅ Correct!\n")
    score = score + 1
else:
    print("❌ Wrong! The correct answer was Brazil\n")

# Final Score

print(f"🎯 Quiz Over! You scored {score} out of 3")
