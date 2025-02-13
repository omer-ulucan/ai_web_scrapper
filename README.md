# AI Webscraper Project

This project is an AI-based web scraping and categorization system built with Python 3.13.

## Key Features

- **Web Scraping:** Uses Playwright and the DuckDuckGo API to collect data.
- **AI Text Processing:** Generates embeddings using the DeepSeek R1 model via Ollama.
- **Category Validation:** Validates categories with a GAT model (using PyTorch Geometric).
- **Reinforcement Learning:** An RL agent corrects miscategorized data.
- **Dataset Optimization:** A RAG model optimizes datasets using vector search via ChromaDB.
- **Noise Reduction:** Applies Scipy (Wiener filter) for text noise reduction.
- **Database Management:** PostgreSQL is used as the main database for scraping results, datasets, and categories.
- **Vector Search:** Embeddings are stored and queried in ChromaDB for AI model optimization.
- **API:** FastAPI microservice for external access.
- **Deployment:** Containerized using Docker and Docker Compose.

## Database Usage

- **PostgreSQL:**

  - Scraping results (text, images, data) are stored in the `scraped_data` table.
  - AI-generated datasets are stored in the `dataset_storage` table.
  - Categories and metadata are stored in the `categories` table.

- **ChromaDB:**
  - Used exclusively for vector search and RAG operations (e.g., storing embeddings and optimizing datasets).

## DeepSeek R1 Integration via Ollama

The project uses the DeepSeek R1 model served by Ollama for embedding generation.

- Configure the Ollama API URL in the `.env` file (default is `http://localhost:11434/api/v1`).
- The AI module sends a POST request to Ollama at `/models/deepseek-r1/generate`.

## Installation

1. Update the settings in the `.env` file.
2. Ensure Docker and Docker Compose are installed.
3. Run the following command to start the services:
   ```bash
   ./scripts/start_server.sh
   ```
