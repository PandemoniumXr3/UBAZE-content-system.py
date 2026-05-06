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

# kies welk platform ik wil posten 
    # kies platform
platform = input("\nTikTok or Instagram? ").lower()

if platform == "tiktok":
    print("\n🔥 HOOK:", idea["title"])

    print("\n🎬 SHOTS:")
    for f in idea["film"]:
        print("-", f)

    print("\n🎤 WHAT TO SAY:")
    for s in idea["say"]:
        print("-", s)

elif platform == "instagram":
    print("\n📸 POST TYPE: carousel")

    print("\n📝 CAPTION:")
    print("Working on something every day. Small progress.")

    print("\n🧩 SLIDES:")
    print("- Slide 1:", idea["title"])
    print("- Slide 2: What I'm doing")
    print("- Slide 3: Progress")
    print("- Slide 4: Small win")
    print("\n📷 PHOTOS:")
    for f in idea["film"]:
        print("-", f)

    instagram_ideas = [
    "Mijn daily dashboard van vandaag",
    "Wat ik vandaag MOET doen",
    "1 kleine win van vandaag",
    "Bouwen vanuit Spanje",
    "Mijn laptop werkplek vandaag",
    "Coffee + code moment",
    "Wat ik vandaag heb geleerd",
    "Voor/na van mijn project",
    "Een screenshot van mijn progress",
    "Mijn GitHub commit van vandaag",
    "Waarom ik dit aan het bouwen ben",
    "Hoe ik mijn dag simpel houd",
    "Mijn focus checklist",
    "Mijn 3 taken van vandaag",
    "Wat ik zou doen als ik opnieuw begon",
    "Behind the scenes van UBAZE",
    "Een product waar ik aan werk",
    "Mijn favoriete tool vandaag",
    "Mijn workflow in 4 slides",
    "Mijn realistische dagplanning",
    "Wat ik moeilijk vond vandaag",
    "Hoe ik toch begon ondanks geen zin",
    "Mijn Spanje werkdag",
    "Wat ik filmde vandaag",
    "Wat ik niet perfect deed maar wel afmaakte",
    "Mijn mini content plan",
    "Mijn eerste echte klant/concept project",
    "Van idee naar live site",
    "Wat ik automatiseer met Python",
    "Mijn Content Engine build",
    "Hoe ik TikTok ideeën maak",
    "Mijn Notion / dashboard setup",
    "Wat ik gebruik om te bouwen",
    "Mijn top 3 tools",
    "Mijn setup zonder echte setup",
    "Waarom je geen perfecte setup nodig hebt",
    "1 ding dat mijn workflow sneller maakt",
    "Wat ik vandaag aan mijn brand deed",
    "Mijn M4YXZ / UBAZE progress",
    "Mijn plan richting 5k",
    "Wat ik deze week wil afmaken",
    "Mijn weekdoelen",
    "Mijn dag reset",
    "Mijn avond shutdown checklist",
    "Wat ik morgen beter ga doen",
    "Mijn favoriete café werkplek",
    "Waar ik vandaag werkte",
    "Mijn work from Spain moment",
    "Mijn laptop + koffie + taak",
    "Waarom kleine progress telt",
    "Build, learn, repeat",
    "Niet wachten op perfect",
    "Een fout die ik vandaag fixte",
    "Code die eindelijk werkte",
    "Mijn project map structuur",
    "Mijn GitHub repo van vandaag",
    "Mijn Netlify deploy moment",
    "Wat ik nu aan het testen ben",
    "Mijn content ideeën van vandaag",
    "Wat ik post op TikTok vs Instagram",
    "Mijn systeem om consistent te blijven"
]
    instagram_posts = [
    {
        "title": "Daily Build",
        "slides": [
            "Slide 1: Building my life in Spain 🇪🇸",
            "Slide 2: Today I worked on [project]",
            "Slide 3: Not perfect, just progress",
            "Slide 4: Finished: [small win]",
            "Slide 5: Tomorrow → continue"
        ],
        "caption": "Small progress today. Building one piece at a time."
    },
    {
        "title": "No Perfect Setup",
        "slides": [
            "Slide 1: You don’t need a perfect setup",
            "Slide 2: Just a laptop and focus",
            "Slide 3: Start with what you have",
            "Slide 4: Build anyway",
            "Slide 5: Progress > perfect"
        ],
        "caption": "No perfect setup. No perfect timing. Just start."
    },
    {
        "title": "What I Did Today",
        "slides": [
            "Slide 1: What I did today",
            "Slide 2: Built: [feature/project]",
            "Slide 3: Learned: [1 thing]",
            "Slide 4: Struggled with: [real thing]",
            "Slide 5: Still going"
        ],
        "caption": "Documenting the build, even when it’s messy."
    },
    {
        "title": "Building UBAZE",
        "slides": [
            "Slide 1: Building something from nothing",
            "Slide 2: Working on: UBAZE",
            "Slide 3: Idea → system → product",
            "Slide 4: One step every day",
            "Slide 5: Watch this grow"
        ],
        "caption": "Building UBAZE piece by piece."
    },
    {
        "title": "Real Talk",
        "slides": [
            "Slide 1: No motivation today",
            "Slide 2: Still opened my laptop",
            "Slide 3: Did 1 small task",
            "Slide 4: That counts",
            "Slide 5: Keep going"
        ],
        "caption": "Some days are not pretty. Still counts."
    },
    {
        "title": "Daily Loop",
        "slides": [
            "Slide 1: My daily loop",
            "Slide 2: Build",
            "Slide 3: Document",
            "Slide 4: Improve",
            "Slide 5: Repeat"
        ],
        "caption": "Build. Document. Improve. Repeat."
    }
]
    platform = input("\nTikTok or Instagram? ").lower()

if platform == "instagram":
    post = random.choice(instagram_posts)

    print("\n📸 INSTAGRAM POST:", post["title"])

    print("\n🧩 SLIDES:")
    for slide in post["slides"]:
        print("-", slide)

    print("\n📝 CAPTION:")
    print(post["caption"])

elif platform == "tiktok":
    print("\n🎥 TIKTOK IDEA:", idea["title"])

    print("\n🎤 WHAT TO SAY:")
    for s in idea["say"]:
        print("-", s)

    print("\n🎬 WHAT TO FILM:")
    for f in idea["film"]:
        print("-", f)