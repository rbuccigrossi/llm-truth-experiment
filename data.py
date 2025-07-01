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
        "document": "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower. Constructed from 1887 to 1889 as the entrance to the 1889 World's Fair, it was initially criticized by some of France's leading artists and intellectuals for its design, but it has become a global cultural icon of France and one of the most recognizable structures in the world.",
        "qa_pairs": [
            {
                "id": "q_001_01",
                "question": "Where is the Eiffel Tower located?",
                "answer": "The Eiffel Tower is located on the Champ de Mars in Paris, France."
            },
            {
                "id": "q_001_02",
                "question": "Who designed the Eiffel Tower?",
                "answer": "The Eiffel Tower was designed by Gustave Eiffel's company."
            },
            {
                "id": "q_001_03",
                "question": "What is the primary material of the Eiffel Tower?",
                "answer": "The Eiffel Tower is a wrought-iron lattice tower."
            }
        ]
    },
    {
        "id": "doc_002",
        "document": "The Great Wall of China is a series of fortifications made of stone, brick, tamped earth, wood, and other materials, generally built along an east-to-west line across the historical northern borders of China to protect the Chinese states and empires against the raids and invasions of the various nomadic groups of the Eurasian Steppe. Several walls were being built as early as the 7th century BC; these, later joined together and made bigger and stronger, are now collectively referred to as the Great Wall. Especially famous is the wall built 220–206 BC by Qin Shi Huang, the first Emperor of China.",
        "qa_pairs": [
            {
                "id": "q_002_01",
                "question": "What was the purpose of the Great Wall of China?",
                "answer": "The Great Wall of China was built to protect the Chinese states and empires against the raids and invasions of various nomadic groups."
            },
            {
                "id": "q_002_02",
                "question": "Who was Qin Shi Huang?",
                "answer": "Qin Shi Huang was the first Emperor of China."
            },
            {
                "id": "q_002_03",
                "question": "When were the earliest parts of the Great Wall built?",
                "answer": "Several walls were being built as early as the 7th century BC."
            }
        ]
    },
    # Add more documents and Q&A pairs here
    # Example of a question that might not be in the document:
    # {
    #     "id": "doc_003",
    #     "document": "The capital of France is Paris. Paris is known for its art, fashion, and culture. The Louvre Museum, located in Paris, is one of the world's largest art museums.",
    #     "qa_pairs": [
    #         {
    #             "id": "q_003_01",
    #             "question": "What is the capital of France?",
    #             "answer": "The capital of France is Paris."
    #         },
    #         {
    #             "id": "q_003_02",
    #             "question": "What is the population of Paris?", # This answer is not in the document
    #             "answer": "The document does not provide an answer."
    #         }
    #     ]
    # }
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
