import random 


ideas = [
    {
        "title": "Explain what you are building",
        "say":[
            "what are you making?",
            "why are you making it?",
            "what problem does it solve?"
        ],
        "film": [
            "laptop",
            "typing",
            "small progress"
        ]

    },
    {
        "title": "Day in Spain",
        "say": [
            "what you're doing today",
            "why you're here",
            "what you're working on"
        ],
        "film": [
            "coffee",
            "outside",
            "laptop"
        ]
    }
]

idea = random.choice(ideas)

print("\n🎥 IDEA:", idea["title"])

print("\n🎤 WHAT TO SAY:")
for s in idea["say"]:
    print("-", s)

print("\n🎬 WHAT TO FILM:")
for f in idea["film"]:
    print("-", f)