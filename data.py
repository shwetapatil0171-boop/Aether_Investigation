victims = [
    "Rahul Sharma", "Ananya Deshmukh", "Vikram Joshi", "Sneha Patil",
    "Arjun Malhotra", "Priya Nair", "Devansh Kapoor", "Meera Iyer",
    "Rohan Bhatt", "Kavya Reddy"
]
locations = [
    "Mumbai Apartment", "Pune Hostel", "Office Building", "Old Warehouse",
    "Hill Station Resort", "Riverside Bungalow", "Art Gallery", "Train Compartment",
    "Farmhouse", "Rooftop Restaurant"
]
location_images = {
    "Mumbai Apartment": "apartment.jpg",
    "Pune Hostel": "hostel.jpg",
    "Office Building": "office.jpg",
    "Old Warehouse": "old_warehouse.jpg",
    "Hill Station Resort": "resort.jpg",
    "Riverside Bungalow": "riverside_bungalow.jpg",
    "Art Gallery": "art_gallery.jpg",
    "Train Compartment": "train.jpg",
    "Farmhouse": "farmhouse.jpg",
    "Rooftop Restaurant": "rooftop_restaurant.jpg",
}

weapons = [
    "Knife", "Gun", "Rope", "Poison", "Blunt Object", "Broken Glass"
]

suspect_names = [
    "Amit Verma", "Rohit Singh", "Karan Mehta", "Soham Desai",
    "Naina Kulkarni", "Ishaan Rao", "Tara Bose", "Yusuf Khan",
    "Diya Chauhan", "Aryan Kapoor", "Riya Saxena", "Manav Pillai"
]

occupations = [
    "Engineer", "Doctor", "Student", "Businessman", "Driver",
    "Security Guard", "Chef", "Artist", "Lawyer", "Journalist"
]

ages = list(range(19, 55))

personalities = [
    "Calm", "Nervous", "Aggressive", "Silent", "Confident", "Shy", "Sarcastic", "Cold"
]

motives = [
    "Inheritance dispute", "Jealousy over a relationship", "Business betrayal",
    "Old rivalry", "Blackmail gone wrong", "Gambling debt", "Revenge for past insult",
    "Hidden affair exposed", "Property dispute", "Witnessed a crime"
]

clue_pool = [
    {"text": "Has scratches on hands", "weight": 3},
    {"text": "Was seen near the crime scene that night", "weight": 4},
    {"text": "Has no verifiable alibi", "weight": 4},
    {"text": "Was nervous and evasive during questioning", "weight": 2},
    {"text": "Avoids eye contact when the victim is mentioned", "weight": 1},
    {"text": "Owns a weapon matching the murder weapon", "weight": 5},
    {"text": "Had a recent heated argument with the victim", "weight": 3},
    {"text": "Lied about their whereabouts", "weight": 5},
    {"text": "Recently withdrew a large, unexplained sum of money", "weight": 3},
    {"text": "Fingerprints found at the scene", "weight": 5},
    {"text": "Was seen disposing of an unknown item that night", "weight": 4},
    {"text": "Has a documented history with the victim's family", "weight": 2},
    {"text": "Changed their story when re-questioned", "weight": 4},
    {"text": "Claims innocence but gives inconsistent details", "weight": 2},
    {"text": "Was financially struggling before the murder", "weight": 1},
]

interrogation_lines = {
    "Calm": [
        "{name} answers each question evenly, almost too composed.",
        "{name} maintains steady eye contact throughout.",
    ],
    "Nervous": [
        "{name}'s hands tremble slightly while answering.",
        "{name} keeps glancing at the door.",
    ],
    "Aggressive": [
        "{name} snaps back, irritated by the questions.",
        "{name} raises their voice, demanding to leave.",
    ],
    "Silent": [
        "{name} answers in clipped, minimal responses.",
        "{name} stays quiet for long stretches before replying.",
    ],
    "Confident": [
        "{name} smirks, seemingly unbothered by the interrogation.",
        "{name} answers quickly, almost rehearsed.",
    ],
    "Shy": [
        "{name} avoids looking up, voice barely above a whisper.",
        "{name} fidgets and hesitates before each answer.",
    ],
    "Sarcastic": [
        "{name} responds with a dry, mocking tone.",
        "{name} rolls their eyes at several questions.",
    ],
    "Cold": [
        "{name} answers flatly, showing no emotion at all.",
        "{name} stares blankly, giving short answers.",
    ],
}
