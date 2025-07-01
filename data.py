"""
This file contains the data for the LLM Truth Experiment.
Each item in the EXPERIMENT_DATA list is a dictionary representing a document set.
Each document set has:
  - 'id': A unique identifier for the document.
  - 'document': The text of the document.
  - 'qa_pairs': A list of question-answer pairs related to the document.
    Each qa_pair is a dictionary with:
      - 'id': A unique identifier for the question.
      - 'question': The question text.
      - 'answer': The expected answer text (derived from the document).
"""

EXPERIMENT_DATA = [
    {
        "id": "doc_001",
        "document": "The Jacquard machine is a draw loom that was first demonstrated in 1801 in Lyon, France. It was developed by French weaver and inventor Joseph Marie Jacquard. The machine is controlled by a number of punched cards, laced together into a continuous sequence. Multiple rows of holes are punched on each card, with one complete card corresponding to one row of the design. This use of replaceable punched cards to control a sequence of operations is considered an important step in the history of computing hardware, as it laid the foundation for programmability.",
        "qa_pairs": [
            {
                "id": "q_001_01",
                "question": "What was used to control the Jacquard machine?",
                "answer": "Punched cards."
            },
            {
                "id": "q_002_01",
                "question": "What don't axolotls undergo that other amphibians do?",
                "answer": "Metamorphosis."
            },
            {
                "id": "q_003_01",
                "question": "What country's government operates the Global Positioning System?",
                "answer": "The United States."
            },
            {
                "id": "q_004_01",
                "question": "What language of text accompnies the scenes in the Bayeux Tapestry?",
                "answer": "Latin."
            },
            {
                "id": "q_005_01",
                "question": "In what year was Aerogel invented?",
                "answer": "1931."
            },
        ]
    },
    {
        "id": "doc_002",
        "document": "The axolotl, Ambystoma mexicanum, is a paedomorphic salamander closely related to the tiger salamander. Although the axolotl is colloquially known as a 'walking fish', it is not a fish, but an amphibian. The species was originally found in several lakes, such as Lake Xochimilco underlying Mexico City. Axolotls are unusual among amphibians in that they reach adulthood without undergoing metamorphosis. Instead of developing lungs and taking to the land, adults remain aquatic and gilled.",
        "qa_pairs": [
            {
                "id": "q_001_01",
                "question": "What was used to control the Jacquard machine?",
                "answer": "Punched cards."
            },
            {
                "id": "q_002_01",
                "question": "What don't axolotls undergo that other amphibians do?",
                "answer": "Metamorphosis."
            },
            {
                "id": "q_003_01",
                "question": "What country's government operates the Global Positioning System?",
                "answer": "The United States."
            },
            {
                "id": "q_004_01",
                "question": "What language of text accompnies the scenes in the Bayeux Tapestry?",
                "answer": "Latin."
            },
            {
                "id": "q_005_01",
                "question": "In what year was Aerogel invented?",
                "answer": "1931."
            },
        ]
    },
    {
        "id": "doc_003",
        "document": "The Global Positioning System (GPS) is a satellite-based radionavigation system owned by the United States government and operated by the United States Space Force. The GPS constellation consists of about 30 satellites in medium Earth orbit in six different orbital planes, with the exact number of satellites varying as older satellites are retired and replaced. The system provides Geolocation and time information to a GPS receiver anywhere on or near the Earth where there is an unobstructed line of sight to four or more GPS satellites. The project was launched in the U.S. in 1973 to overcome the limitations of previous navigation systems.",
        "qa_pairs": [
            {
                "id": "q_001_01",
                "question": "What was used to control the Jacquard machine?",
                "answer": "Punched cards."
            },
            {
                "id": "q_002_01",
                "question": "What don't axolotls undergo that other amphibians do?",
                "answer": "Metamorphosis."
            },
            {
                "id": "q_003_01",
                "question": "What country's government operates the Global Positioning System?",
                "answer": "The United States."
            },
            {
                "id": "q_004_01",
                "question": "What language of text accompnies the scenes in the Bayeux Tapestry?",
                "answer": "Latin."
            },
            {
                "id": "q_005_01",
                "question": "In what year was Aerogel invented?",
                "answer": "1931."
            },
        ]
    },
    {
        "id": "doc_004",
        "document": "The Bayeux Tapestry is an embroidered cloth nearly 70 metres (230 ft) long and 50 centimetres (20 in) tall that depicts the events leading up to the Norman conquest of England, culminating in the Battle of Hastings. It is thought to date to the 11th century, within a few years of the battle. Although it is called a tapestry, it is not a true tapestry in which the design is woven into the cloth; it is in fact an embroidery. The tapestry consists of some fifty scenes with Latin text, embroidered on linen with coloured woollen yarns.",
        "qa_pairs": [
            {
                "id": "q_001_01",
                "question": "What was used to control the Jacquard machine?",
                "answer": "Punched cards."
            },
            {
                "id": "q_002_01",
                "question": "What don't axolotls undergo that other amphibians do?",
                "answer": "Metamorphosis."
            },
            {
                "id": "q_003_01",
                "question": "What country's government operates the Global Positioning System?",
                "answer": "The United States."
            },
            {
                "id": "q_004_01",
                "question": "What language of text accompnies the scenes in the Bayeux Tapestry?",
                "answer": "Latin."
            },
            {
                "id": "q_005_01",
                "question": "In what year was Aerogel invented?",
                "answer": "1931."
            },
        ]
    },
    {
        "id": "doc_005",
        "document": "Aerogel is a synthetic porous ultralight material derived from a gel, in which the liquid component for the gel has been replaced with a gas without significant collapse of the gel structure. The result is a solid with extremely low density and low thermal conductivity. Nicknamed 'frozen smoke', 'solid smoke', 'solid air', or 'blue smoke' owing to its translucent nature and the way light scatters in the material. Despite its name, aerogel is a solid, rigid, and dry material. It was first created by Samuel Stephens Kistler in 1931, as a result of a bet with Charles Learned over who could replace the liquid in 'jellies' with gas without causing shrinkage.",
        "qa_pairs": [
            {
                "id": "q_001_01",
                "question": "What was used to control the Jacquard machine?",
                "answer": "Punched cards."
            },
            {
                "id": "q_002_01",
                "question": "What don't axolotls undergo that other amphibians do?",
                "answer": "Metamorphosis."
            },
            {
                "id": "q_003_01",
                "question": "What country's government operates the Global Positioning System?",
                "answer": "The United States."
            },
            {
                "id": "q_004_01",
                "question": "What language of text accompnies the scenes in the Bayeux Tapestry?",
                "answer": "Latin."
            },
            {
                "id": "q_005_01",
                "question": "In what year was Aerogel invented?",
                "answer": "1931."
            },
        ]
    },
]

if __name__ == '__main__':
    # Example of how to access the data
    for item in EXPERIMENT_DATA:
        print(f"Document ID: {item['id']}")
        print(f"Document: {item['document'][:50]}...") # Print first 50 chars
        for qa in item['qa_pairs']:
            print(f"  Question ID: {qa['id']} - {qa['question']}")
            print(f"  Answer: {qa['answer']}")
        print("-" * 20)

    print(f"\nTotal document sets: {len(EXPERIMENT_DATA)}")
    if EXPERIMENT_DATA:
        print(f"Total Q&A pairs in first document: {len(EXPERIMENT_DATA[0]['qa_pairs'])}")
