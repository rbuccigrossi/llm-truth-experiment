# LLM Truth Experiment

## Overview

The LLM Truth Experiment is a project designed to conduct a controlled, repeatable experiment on the impact of two specific prompt engineering techniques on the accuracy of Retrieval Augmented Generation (RAG) results. The experiment aims to understand how "grounding" and instructing the Large Language Model (LLM) to respond with "I don't know" when uncertain affect the verifiability of its answers.

The experiment will involve a dataset of short documents (e.g., Wikipedia articles), each paired with a question and its corresponding answer derived directly from the document. The core methodology involves iterating through these document-question-answer sets and presenting the LLM with the document and the question using various prompt configurations.

A key aspect of the experiment is to observe how the LLM behaves when the provided document does not contain the answer to the question. In such scenarios, the LLM might attempt to answer based on its pre-existing knowledge. The techniques of "grounding" and prompting for an "I don't know" response are intended to mitigate this and improve the reliability of the LLM's output by ensuring answers are based on the provided context.

## Core Concepts

*   **Grounding:** This technique involves instructing the LLM to base its answers strictly on the information provided in the given document. The prompt will explicitly state that the answer must be found within the context of the document.
*   **Asking the LLM to say "I don't know":** This technique involves explicitly instructing the LLM to respond with "I don't know" or a similar phrase if the answer to the question cannot be found in the provided document. This encourages the LLM to acknowledge uncertainty rather than generating a potentially incorrect or unverified answer.

## Technologies

This project will utilize `litellm` to facilitate interaction with various LLMs. This allows for flexibility in experimenting with different models, including:

*   OpenAI models (e.g., gpt-3.5-turbo, gpt-4)
*   Locally hosted models via Ollama (e.g., Gemma, Llama)

The use of `litellm` provides a unified interface for sending prompts and receiving responses, simplifying the process of swapping between different LLM providers and models.

## Experiment Setup

The experiment will be structured around the following components:

1.  **Documents:** A collection of short, factual documents. Each document will serve as the context for one or more questions.
2.  **Question-Answer Pairs:** For each document, there will be at least one question whose answer can be directly and unambiguously found within that document.
3.  **Prompting Loop:** The experiment will programmatically:
    *   Iterate through each document and its associated question(s).
    *   For each question, generate a series of prompts using different combinations of the core techniques (grounding, "I don't know").
    *   Send these prompts to the selected LLM via `litellm`.
    *   Record the LLM's responses.
4.  **Evaluation:** The accuracy of the LLM's responses will be evaluated based on whether they correctly answer the question using only the provided document. The effectiveness of the different prompting techniques will be compared.

## Future Work

Potential future enhancements and next steps for this project include:

*   Developing a more sophisticated automated evaluation metric for response accuracy and verifiability.
*   Expanding the dataset of documents and question-answer pairs.
*   Experimenting with a wider range of LLMs and model sizes.
*   Investigating the impact of varying the phrasing of the grounding and "I don't know" instructions.
*   Analyzing the cost and latency implications of different models and prompt strategies.
*   Implementing a user interface for easier configuration and result visualization.
*   Adding a mechanism to test scenarios where the document is only partially relevant to the question.
