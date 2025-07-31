import random

name = [
    "Virat Kohli", "Salman Khan", "Narendra Modi", "Anubhav", "Raj Kumar", "Donald Trump",
    "Elon Musk", "Kylie Jenner", "Shahrukh Khan", "Ronaldo", "Taylor Swift", "Bill Gates",
    "Amitabh Bachchan", "Ranveer Singh", "Joe Biden", "Sundar Pichai", "Priyanka Chopra"
]

action = [
    "married secretly at", "started a dance battle at", "proposed to someone near",
    "launched a rocket from", "was spotted eating pani puri at", "opened a new startup in",
    "gave a motivational speech at", "got lost near", "built a secret lab under",
    "played hide and seek at", "was arrested for singing loudly at", "donated billions at",
    "won an award at", "was chased by fans near", "hosted a fashion show at"
]

places = [
    "Taj Mahal", "India Gate", "Red Fort", "a tea stall", "the Moon", "a cricket stadium",
    "Delhi Metro", "a wedding hall", "Lonavala", "inside a submarine", "on Mars",
    "a crowded mall", "YouTube headquarters", "a haunted mansion", "Lok Sabha",
    "a luxury yacht", "a remote village in Bihar"
]

while True:
    selected_name = random.choice(name)
    selected_action = random.choice(action)
    selected_place = random.choice(places)

    headline = f"Breaking News: {selected_name} {selected_action} {selected_place}!"
    print("\n" + headline)
    
    user_input = input("\nDo you want another breaking news (yes/no): ").strip().lower()
    if user_input == "no":
        break
