# 🤖 AI Support Triage Agent

> An intelligent customer support automation system using LangGraph, LLMs, and fine-tuned classifiers

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-green.svg)](https://github.com/langchain-ai/langgraph)

## 🎯 Overview

An AI-powered support triage system that automatically classifies customer messages into categories (billing, technical, general), routes them to appropriate handlers, and generates intelligent responses. Built with LangGraph for state management and orchestration.

## ✨ Features

- 🔄 **Smart Routing**: Automatically classifies messages into billing, technical, or general categories
- 🛠️ **Tool Integration**: Looks up orders and searches FAQs based on message content
- 🤖 **LLM-Powered Responses**: Generates contextual, helpful replies
- 📊 **Evaluation Framework**: Comprehensive testing with routing accuracy, tool correctness, and LLM-as-judge
- 🔍 **LangSmith Integration**: Full tracing and monitoring

## 🏗️ Architecture

```
Customer Message 
    ↓
[Classify] → Determines category (billing/technical/general)
    ↓
[Route] → Conditional routing
    ↓
[Tool Call] → lookup_order() or search_faq()
    ↓
[Respond] → Generate helpful reply
    ↓
Response
```

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.10 or higher
python --version
```

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/support-triage-agent.git
cd support-triage-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
LANGSMITH_API_KEY=your_langsmith_key_here
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
```

### Run the Agent

```bash
python agent.py
```

## 📊 Evaluation

Run the evaluation suite to test routing accuracy, tool correctness, and response quality:

```bash
# Create evaluation dataset (first time only)
python dataset.py

# Run evaluation
python evaluate.py
```

## 🛠️ Tech Stack

- **LangGraph**: Agent orchestration and state management
- **LangChain**: LLM integration
- **Groq**: Fast LLM inference
- **LangSmith**: Tracing and evaluation
- **Python 3.10+**: Core language

## 📁 Project Structure

```
support-triage-agent/
├── agent.py           # Main LangGraph agent logic
├── tools.py           # Tool definitions (lookup_order, search_faq)
├── llm.py             # LLM configuration
├── dataset.py         # Evaluation dataset creation
├── evaluate.py        # Evaluation suite
├── .env               # Environment variables
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🎯 Roadmap

- [ ] Add RAG-based FAQ retrieval with vector database
- [ ] Fine-tune DistilBERT classifier for faster, cheaper routing
- [ ] Implement sentiment analysis and priority routing
- [ ] Build production FastAPI backend
- [ ] Add real-time monitoring dashboard
- [ ] Deploy to production

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 👤 Author

**Your Name** - [GitHub](https://github.com/YOUR_USERNAME) | [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)

## 🙏 Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Powered by [Groq](https://groq.com)
- Evaluated with [LangSmith](https://smith.langchain.com)

---

⭐ Star this repo if you find it helpful!
