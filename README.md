# Research Paper Rewriting API

A FastAPI-based service that rewrites research papers to make them appear more naturally human-written while preserving academic integrity and content accuracy.

## Overview

This API takes research paper text as input and applies two-stage processing:
1. **AI Rewriting**: Uses OpenRouter API (GPT-4o-mini) to rewrite content naturally
2. **Humanization**: Applies post-processing to inject authentic academic writing patterns

## Project Structure

```
Rewriting-Research-Papers/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration and environment settings
│   ├── models/
│   │   └── paper.py         # Pydantic models for API requests/responses
│   ├── routers/
│   │   └── papers.py        # API endpoints for paper rewriting
│   ├── services/
│   │   └── rewrite_service.py # Core business logic
│   └── utils/
│       ├── openrouter.py    # OpenRouter API integration
│       └── humanizer.py     # Text humanization algorithms
└── README.md
```

## Code Architecture Explained

### Core Application Files

#### `app/main.py`
**Purpose**: FastAPI application entry point and configuration
- Creates the main FastAPI application instance
- Includes router modules for API endpoints
- Sets up application metadata (title, description)
- Acts as the central hub that ties all components together

#### `app/config.py`
**Purpose**: Environment configuration and settings management
- Uses Pydantic Settings for type-safe configuration
- Loads environment variables from `.env` file
- Defines default values for OpenRouter API settings
- Provides centralized access to configuration across the app

### API Layer

#### `app/routers/papers.py`
**Purpose**: HTTP endpoint definitions and request handling
- Defines the `/papers/rewrite` POST endpoint
- Handles both JSON and raw text input formats
- Validates incoming requests and formats responses
- Acts as the interface between HTTP requests and business logic
- Includes error handling for malformed requests

#### `app/models/paper.py`
**Purpose**: Data models and validation schemas
- Defines Pydantic models for API request/response structure
- `PaperRequest`: Validates incoming paper text
- `PaperResponse`: Structures the API response format
- Ensures type safety and automatic API documentation

### Business Logic Layer

#### `app/services/rewrite_service.py`
**Purpose**: Core business logic orchestration
- Coordinates the two-stage rewriting process
- Calls OpenRouter API for AI-based rewriting
- Applies humanization post-processing
- Acts as the main service layer between API and utilities
- Currently uses "extreme" humanization strength

### Utility Layer

#### `app/utils/openrouter.py`
**Purpose**: External API integration for AI rewriting
- Handles HTTP communication with OpenRouter API
- Contains the system prompt that guides AI rewriting behavior
- Manages API authentication and request formatting
- Implements async HTTP client for non-blocking requests
- Includes specific headers for API identification

**Key Features**:
- System prompt designed to create natural, human-like writing
- Temperature set to 0.9 for creative variation
- Preserves citations, equations, and academic references
- Maintains paper length within ±10% of original

#### `app/utils/humanizer.py`
**Purpose**: Post-processing algorithms to reduce AI detection
- Implements sophisticated text humanization techniques
- Applies multiple passes of natural writing patterns
- Configurable strength levels (mild, medium, strong, extreme)

**Humanization Techniques**:
1. **Academic Hedges**: Injects tentative phrasing ("it appears that", "may suggest")
2. **Transition Injection**: Adds natural academic connectors between sentences
3. **Academic Clichés**: Sprinkles common scholarly phrases
4. **Rhythm Variation**: Breaks long sentences and varies structure
5. **Contribution Signals**: Adds research impact statements
6. **Limitations**: Includes academic humility phrases

**Algorithm Flow**:
- Phase 1: Inject academic clichés at strategic positions
- Phase 2: Add hedging language within sentences
- Phase 3: Insert transition words between sentences
- Phase 4: Append contribution statements
- Phase 5: Add limitation acknowledgments
- Phase 6: Adjust sentence rhythm and length

#### `app/__init__.py`
**Purpose**: Python package initialization
- Empty file that makes the `app` directory a Python package
- Allows imports from the app module
- Required for proper module structure in Python

## Features

- **Flexible Input**: Accepts both JSON and raw text input
- **Academic Tone Preservation**: Maintains scholarly language while adding natural variations
- **Configurable Humanization**: Multiple strength levels (mild, medium, strong, extreme)
- **Citation Safety**: Preserves references, equations, and citations exactly
- **Length Control**: Maintains original paper length (±10%)

## Prerequisites

- Python 3.8+
- OpenRouter API account and key
- pip or poetry for dependency management

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Rewriting-Research-Papers
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn pydantic-settings httpx
   ```

3. **Environment Setup**
   
   Create a `.env` file in the project root:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   OPENROUTER_MODEL=openai/gpt-4o-mini
   ```

   **Getting OpenRouter API Key:**
   - Visit [OpenRouter.ai](https://openrouter.ai)
   - Sign up/login and go to API Keys section
   - Create a new API key
   - Add credits to your account for API usage

## Running the Application

1. **Start the server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Access the API**
   - API Base URL: `http://localhost:8000`
   - Interactive Docs: `http://localhost:8000/docs`
   - OpenAPI Schema: `http://localhost:8000/openapi.json`

## API Usage

### Endpoint: `POST /papers/rewrite`

Rewrites research paper text to appear more naturally human-written.

#### Method 1: JSON Input
```bash
curl -X POST "http://localhost:8000/papers/rewrite" \
  -H "Content-Type: application/json" \
  -d '{"paper": "Your research paper text here..."}'
```

#### Method 2: Raw Text Input
```bash
curl -X POST "http://localhost:8000/papers/rewrite" \
  -H "Content-Type: text/plain" \
  -d "Your research paper text here..."
```

#### Response Format
```json
{
  "rewritten_paper": "The rewritten and humanized paper text..."
}
```

#### Error Response
```json
{
  "error": "No paper text provided"
}
```

## Configuration Options

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENROUTER_API_KEY` | Required | Your OpenRouter API key |
| `OPENROUTER_MODEL` | `openai/gpt-4o-mini` | AI model to use for rewriting |

### Humanization Strength Levels

The system uses "extreme" strength by default, but you can modify in `rewrite_service.py`:

- **mild** (2%): Minimal changes
- **medium** (5%): Moderate humanization
- **strong** (8%): Significant natural patterns
- **extreme** (12%): Maximum humanization

## How It Works

### Request Flow
1. **HTTP Request** → `papers.py` receives and validates input
2. **Service Layer** → `rewrite_service.py` orchestrates the process
3. **AI Rewriting** → `openrouter.py` calls external API
4. **Humanization** → `humanizer.py` applies post-processing
5. **Response** → Formatted JSON returned to client

### 1. AI Rewriting Stage (`openrouter.py`)
- Uses OpenRouter API with carefully crafted system prompt
- Applies natural writing patterns while preserving academic tone
- Maintains original meaning and citations
- Temperature set to 0.9 for creative variation

### 2. Humanization Stage (`humanizer.py`)
The humanizer applies multiple techniques:
- **Academic Hedges**: Adds tentative phrasing ("it appears that", "may suggest")
- **Transitions**: Inserts natural academic connectors
- **Clichés**: Sprinkles common academic phrases
- **Rhythm Variation**: Mixes sentence lengths and structures
- **Contribution Signals**: Adds research impact statements
- **Limitations**: Includes academic humility phrases

## Development

### Adding New Features

1. **New Endpoints**: Add to `app/routers/` (follow `papers.py` pattern)
2. **Business Logic**: Extend `app/services/` (orchestration layer)
3. **Models**: Define in `app/models/` (Pydantic schemas)
4. **Utilities**: Add to `app/utils/` (helper functions and external integrations)
5. **Configuration**: Update `app/config.py` for new environment variables

### Code Modification Guidelines

- **Changing AI Model**: Modify `OPENROUTER_MODEL` in `.env` or `config.py`
- **Adjusting Humanization**: Edit strength levels in `humanizer.py`
- **New API Endpoints**: Create new router files in `app/routers/`
- **External APIs**: Add new utility files in `app/utils/`
- **Request/Response Models**: Extend `app/models/paper.py`

### Testing the API

Use the interactive documentation at `http://localhost:8000/docs` to test endpoints directly in your browser.

### File Dependencies

```
main.py
├── routers/papers.py
│   ├── services/rewrite_service.py
│   │   ├── utils/openrouter.py
│   │   │   └── config.py
│   │   └── utils/humanizer.py
│   └── models/paper.py
└── config.py
```

## Deployment Considerations

### Production Setup
- Use environment variables for all secrets
- Set up proper logging
- Configure CORS if needed for web frontend
- Use production ASGI server (gunicorn + uvicorn)
- Set up monitoring and health checks

### Security Notes
- Never commit API keys to version control
- Use HTTPS in production
- Implement rate limiting if needed
- Consider authentication for production use

## Troubleshooting

### Common Issues

1. **"No module named 'app'"**
   - Run from project root directory
   - Ensure Python path includes current directory

2. **OpenRouter API Errors**
   - Verify API key is correct
   - Check account has sufficient credits
   - Ensure model name is valid

3. **Empty Response**
   - Check input text is not empty
   - Verify API key permissions
   - Review server logs for errors

### Logs and Debugging
- Enable debug mode: `uvicorn app.main:app --reload --log-level debug`
- Check OpenRouter API response status codes
- Validate input text encoding (UTF-8)

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Submit pull request

## Support

For issues and questions:
- Check the troubleshooting section
- Review API documentation at `/docs`
- [Add contact information or issue tracker]