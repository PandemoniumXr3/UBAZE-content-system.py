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
    },
    {
    "title": "Building in Spain",
    "say": [
        "what you're working on",
        "why you're doing it here",
        "what you're trying to build"
    ],
    "film": ["coffee", "laptop", "outside"]
},
{
    "title": "Day in my life",
    "say": [
        "what you're doing today",
        "what you're working on",
        "what you finished"
    ],
    "film": ["morning", "laptop", "night"]
},
{
    "title": "No motivation but still working",
    "say": [
        "you don't feel like it",
        "why you're still doing it",
        "small progress matters"
    ],
    "film": ["tired face", "typing", "progress"]
},
{
    "title": "Why I started",
    "say": [
        "why you started building",
        "what you want to achieve",
        "what drives you"
    ],
    "film": ["talking", "walking", "working"]
},
{
    "title": "Small wins",
    "say": [
        "what you finished today",
        "why small wins matter",
        "what's next"
    ],
    "film": ["screen", "typing", "result"]
},
{
    "title": "Building in Spain",
    "say": [
        "what you're working on",
        "why you're doing it here",
        "what you're trying to build"
    ],
    "film": ["coffee", "laptop", "outside"]
},
{
    "title": "Day in my life",
    "say": [
        "what you're doing today",
        "what you're working on",
        "what you finished"
    ],
    "film": ["morning", "laptop", "night"]
},
{
    "title": "No motivation but still working",
    "say": [
        "you don't feel like it",
        "why you're still doing it",
        "small progress matters"
    ],
    "film": ["tired face", "typing", "progress"]
},
{
    "title": "Why I started",
    "say": [
        "why you started building",
        "what you want to achieve",
        "what drives you"
    ],
    "film": ["talking", "walking", "working"]
},
{
    "title": "Small wins",
    "say": [
        "what you finished today",
        "why small wins matter",
        "what's next"
    ],
    "film": ["screen", "typing", "result"]
},
{
    "title": "What I'm building today",
    "say": [
        "what you're making",
        "why you're making it",
        "what it does"
    ],
    "film": ["code", "typing", "screen"]
},
{
    "title": "From idea to reality",
    "say": [
        "your idea",
        "how you're building it",
        "progress"
    ],
    "film": ["thinking", "typing", "result"]
},
{
    "title": "Fixing something",
    "say": [
        "what was broken",
        "how you fixed it",
        "result"
    ],
    "film": ["problem", "typing", "fix"]
},
{
    "title": "Learning while building",
    "say": [
        "what you learned today",
        "what was hard",
        "how you solved it"
    ],
    "film": ["screen", "thinking", "typing"]
},
{
    "title": "You don't need motivation",
    "say": [
        "why motivation is overrated",
        "why starting matters",
        "just do it"
    ],
    "film": ["talking", "typing"]
},
{
    "title": "Stop overthinking",
    "say": [
        "why overthinking kills progress",
        "why action matters",
        "just start"
    ],
    "film": ["thinking", "typing"]
},
{
    "title": "Consistency > everything",
    "say": [
        "why showing up matters",
        "what you're doing daily",
        "progress over time"
    ],
    "film": ["routine", "working"]
},
{
    "title": "No perfect moment",
    "say": [
        "why waiting is useless",
        "why starting now matters",
        "progress > perfect"
    ],
    "film": ["laptop", "typing"]
},
{
    "title": "Tool I use daily",
    "say": [
        "what the tool is",
        "why you use it",
        "what it helps you do"
    ],
    "film": ["screen recording", "clicking"]
},
{
    "title": "This saves me time",
    "say": [
        "what you used before",
        "what changed",
        "why it's better"
    ],
    "film": ["before", "after"]
},
{
    "title": "My workflow",
    "say": [
        "how you work",
        "what tools you use",
        "why it works"
    ],
    "film": ["apps", "screen", "typing"]
},
{
    "title": "Building a brand",
    "say": [
        "what you're building",
        "why you started",
        "what your goal is"
    ],
    "film": ["laptop", "design", "product"]
},
{
    "title": "Behind the scenes",
    "say": [
        "what you're working on",
        "how you're doing it",
        "progress"
    ],
    "film": ["screen", "typing"]
},
{
    "title": "From nothing",
    "say": [
        "starting point",
        "what you're doing now",
        "where you're going"
    ],
    "film": ["old vs new"]
},
{
    "title": "Is this worth it?",
    "say": [
        "what it is",
        "why you tried it",
        "is it good?"
    ],
    "film": ["product", "use"]
},
{
    "title": "Quick review",
    "say": [
        "what it does",
        "what's good",
        "what's bad"
    ],
    "film": ["close up", "use"]
},





]

idea = random.choice(ideas)

print("\n🎥 IDEA:", idea["title"])

print("\n🎤 WHAT TO SAY:")
for s in idea["say"]:
    print("-", s)

print("\n🎬 WHAT TO FILM:")
for f in idea["film"]:
    print("-", f)