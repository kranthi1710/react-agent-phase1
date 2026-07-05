# 🤖 ReAct AI Agent From Scratch - Phase 1

> Build your first Local AI Agent using **Python**, **Ollama**, and **Llama 3.2** — without relying on any AI frameworks.

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-green)
![Llama](https://img.shields.io/badge/Llama-3.2-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 📖 Overview

This project is the **first phase** of building an AI Agent from scratch.

Instead of using frameworks like LangChain or LangGraph, we first learn the **fundamental building blocks** of an AI application.

The application communicates with a **locally running Llama 3.2 model through Ollama**, accepts user questions from the terminal, and displays AI-generated responses in a clean command-line interface.

The main goal of this phase is to understand how an AI application is structured before introducing concepts like tool calling, memory, and autonomous reasoning.

---

# 🎯 Learning Objectives

After completing this project, you will understand:

* What a Local LLM is
* How Ollama serves AI models
* How Python communicates with an LLM
* How System Prompts influence AI behavior
* Why modular project architecture is important
* How to organize AI projects using clean code principles

---

# 🏗 Project Architecture

```text
                    User
                      │
                      ▼
                 app.py
                      │
                      ▼
            Reads User Question
                      │
                      ▼
                LocalLLM
                 (llm.py)
                      │
                      ▼
         Reads system_prompt.txt
                      │
                      ▼
             config.py
                      │
                      ▼
        Ollama (llama3.2 Model)
                      │
                      ▼
             AI Response
                      │
                      ▼
          Rich Console Output
```

---

# 📂 Project Structure

```text
react-agent-phase1
│
├── app.py
├── config.py
├── llm.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── prompts
│   └── system_prompt.txt
│
└── core
    └── console.py
```

---

# 📁 File-by-File Explanation

## app.py

### Purpose

This is the **entry point** of the application.

Whenever you run:

```bash
python app.py
```

execution begins here.

### Responsibilities

* Starts the application
* Displays a welcome banner
* Accepts user input
* Sends the prompt to the AI model
* Displays the AI response
* Continues the conversation until the user exits

Think of this file as the **manager** of the entire application.

---

## config.py

### Purpose

Stores all application configuration in one place.

Instead of hardcoding values throughout the project, configuration is centralized.

Example:

* Model Name
* Temperature
* Future configuration values

### Why?

Suppose tomorrow you want to switch from **Llama 3.2** to **Mistral**.

Instead of modifying multiple files, only one configuration value needs to change.

Benefits:

* Better maintainability
* Cleaner architecture
* Easy model switching

---

## llm.py

### Purpose

Handles communication between Python and Ollama.

Responsibilities include:

* Loading the System Prompt
* Connecting to Ollama
* Sending user prompts
* Receiving AI responses

This file acts as the **bridge** between the application and the language model.

---

## prompts/system_prompt.txt

### Purpose

Contains the **System Prompt**.

The System Prompt defines how the AI should behave.

Example:

> You are a helpful AI assistant.

Changing this file changes the personality of the assistant without modifying any Python code.

---

## core/console.py

### Purpose

Creates a reusable Rich Console instance.

Using Rich instead of Python's default `print()` provides:

* Beautiful panels
* Colored output
* Better readability
* Professional terminal UI

---

## requirements.txt

Contains all Python dependencies required to run the project.

Install them using:

```bash
pip install -r requirements.txt
```

---

## .gitignore

Specifies files that should not be committed to Git.

Examples:

* Virtual environments
* Cache files
* Compiled Python files
* IDE settings

---

# 🔄 Application Flow

## Step 1

User starts the application.

```bash
python app.py
```

↓

## Step 2

A welcome message is displayed.

↓

## Step 3

The application waits for user input.

↓

## Step 4

The user enters a question.

↓

## Step 5

The question is sent to the LocalLLM.

↓

## Step 6

The System Prompt is loaded.

↓

## Step 7

Python communicates with Ollama.

↓

## Step 8

Llama 3.2 generates a response.

↓

## Step 9

The response is displayed using Rich Panels.

↓

## Step 10

The application waits for the next question.

---

# 🧠 Why Separate the Code into Multiple Files?

As projects grow, placing everything in a single file becomes difficult to maintain.

This project follows the **Single Responsibility Principle**, where each file has one clear responsibility.

| File              | Responsibility            |
| ----------------- | ------------------------- |
| app.py            | Controls application flow |
| config.py         | Stores configuration      |
| llm.py            | Handles AI communication  |
| console.py        | Manages terminal output   |
| system_prompt.txt | Defines AI behavior       |

This modular design makes the application easier to understand, maintain, and extend.

---

# 🚀 How to Run the Project

## Clone the repository

```bash
git clone https://github.com/kranthi1710/react-agent-phase1.git
cd react-agent-phase1
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama

Download Ollama from:

https://ollama.com/download

---

## Pull the Llama 3.2 model

```bash
ollama pull llama3.2
```

---

## Start the application

```bash
python app.py
```

---

# 💬 Example Conversation

```text
You > What is an AI Agent?

Assistant

An AI Agent is a software system capable of reasoning,
making decisions, and interacting with tools to
complete tasks autonomously.
```

---

# 🛠 Technologies Used

* Python
* Ollama
* Llama 3.2
* Rich
* Pydantic

---

# 📚 Concepts Learned

* Local Large Language Models (LLMs)
* Prompt Engineering
* Modular Programming
* Configuration Management
* Separation of Concerns
* Command Line Interfaces
* AI Application Architecture

---

# 🚀 Future Improvements (Phase 2)

The next phase will transform this chatbot into a real AI Agent by adding:

* ReAct (Reason → Act → Observe)
* Tool Calling
* Function Calling
* Calculator Tool
* Web Search Tool
* Memory
* Conversation History
* Error Handling
* Logging
* Environment Variables
* Unit Tests

---

# 📖 Key Takeaways

This project is intentionally simple.

The focus is **not on building a feature-rich chatbot**, but on understanding the foundational architecture of AI applications.

By separating configuration, prompts, AI communication, and user interaction into dedicated modules, the project follows software engineering best practices and creates a solid foundation for more advanced AI Agent capabilities in future phases.

---

## ⭐ If you found this project useful

If this repository helped you understand how to build an AI application from scratch, consider giving it a ⭐ on GitHub.

Happy Learning! 🚀
