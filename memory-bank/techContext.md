# Technical Context

## Technology Stack
1. Core Technologies
   - Python (Main implementation language)
   - Flask (Web server framework)
   - Docker (Containerization)

2. External Services
   - Instagram (Content source)
   - Mealie API (Recipe management)
   - OpenAI/Ollama (Through Mealie for processing)

## Development Environment
1. Project Structure
   ```
   InstagramToMealie/
   ├── helpers/
   │   ├── instadownloader.py
   │   ├── instaloader_login_helper.py
   │   └── mealie_api.py
   ├── templates/
   │   └── index.html
   ├── main.py
   ├── requirements.txt
   ├── Dockerfile
   └── compose.example.yaml
   ```

2. Dependencies
   - Instaloader (Instagram integration)
   - Flask (Web framework)
   - Requests (HTTP client)
   - Docker (Containerization)

## Configuration
1. Environment Variables
   ```
   MEALIE_URL                      # Mealie instance URL
   MEALIE_API_KEY                  # Authentication key
   MEALIE_OPENAI_REQUEST_TIMEOUT   # AI request timeout (optional)
   MEALIE_USE_INSTAGRAM_TAGS       # Tag preservation flag (optional)
   INSTA_USER                      # Instagram username
   INSTA_PWD                       # Password (optional)
   INSTA_TOTP_SECRET              # 2FA secret (optional)
   HTTP_PORT                       # Web server port (optional)
   ```

2. Authentication Methods
   - Session file (recommended)
   - Username/password
   - 2FA support (not recommended)

## Deployment
1. Docker Support
   - Official image: jotec2002/instagramtomealie
   - Build from source option
   - Docker Compose integration

2. Prerequisites
   - Mealie instance with OpenAI/Ollama configured
   - Valid Mealie API key
   - Instagram authentication (session/credentials)

3. Network Requirements
   - Access to Instagram
   - Access to Mealie instance
   - Exposed web port (default: 9001)
