# Technical Context: Instagram To Mealie

## Technology Stack

### Backend
- **Python 3.12**: Core programming language
- **Flask 3.1.0**: Web framework for handling HTTP requests
- **Waitress 3.0.2**: Production WSGI server
- **Instaloader 4.14**: Library for downloading Instagram content
- **PyOTP 2.9.0**: Library for handling TOTP (Time-based One-Time Password) authentication
- **Requests**: HTTP client for API communication

### Frontend
- **HTML/CSS**: Simple web interface
- **JavaScript**: Minimal client-side functionality

### Deployment
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration

## Development Environment

### Requirements
- Python 3.12 or higher
- Docker and Docker Compose (for containerized deployment)
- Access to Instagram (for testing)
- Access to Mealie instance with OpenAI/Ollama configured

### Local Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables
4. Generate Instagram session file (recommended)
5. Run the application: `python -u main.py`

### Docker Setup
1. Clone the repository
2. Configure environment variables in compose.yaml
3. Build and run: `docker-compose up -d`

## Configuration

### Environment Variables
- **MEALIE_URL**: URL of the Mealie instance
- **MEALIE_API_KEY**: API key for Mealie authentication
- **INSTA_USER**: Instagram username
- **INSTA_PWD**: Instagram password (optional if using session file)
- **INSTA_TOTP_SECRET**: Secret key for 2FA (optional)
- **MEALIE_OPENAI_REQUEST_TIMEOUT**: Timeout for OpenAI/Ollama requests (default: 60s)
- **MEALIE_USE_INSTAGRAM_TAGS**: Whether to include Instagram tags in Mealie (default: true)
- **HTTP_PORT**: Port for the web server (default: 9001)

### Files
- **session-file**: Instagram session file (recommended authentication method)

## External Dependencies

### Instagram
- **Authentication**: Requires valid credentials or session file
- **Rate Limiting**: Subject to Instagram's rate limits and anti-scraping measures
- **Content Access**: Requires public posts or authenticated access to private posts

### Mealie
- **API Access**: Requires valid API key
- **OpenAI/Ollama**: Mealie must have OpenAI or Ollama configured
- **Version Compatibility**: Tested with Mealie v2.1.0

## Technical Constraints

### Instagram Limitations
- Rate limiting can block access if too many requests are made
- Authentication is complex and subject to security measures
- Session files expire and need to be regenerated
- Instagram's structure may change, breaking the scraping functionality

### Mealie Limitations
- OpenAI/Ollama processing can be slow (hence the timeout configuration)
- API structure may change between versions
- Large media uploads may fail or timeout

### System Limitations
- Temporary storage needed for downloaded files
- Network connectivity required to both Instagram and Mealie
- Processing videos may require significant resources

## Security Considerations

### Authentication
- Instagram credentials should be protected
- Mealie API keys have full access to the Mealie instance
- Session files contain sensitive authentication data

### Data Handling
- Temporary files are created during processing
- Files are cleaned up after processing
- No persistent storage of Instagram content

### Network Security
- HTTPS recommended for production deployment
- API communication should be over secure connections
- Docker network isolation recommended

## Performance Considerations

### Resource Usage
- Minimal CPU and memory requirements for basic operation
- Temporary disk space needed for downloaded media
- Network bandwidth for downloading and uploading media

### Scalability
- Single-instance design, not designed for horizontal scaling
- Rate limited by Instagram's API restrictions
- Suitable for personal or small-team usage

### Optimization
- Session-based authentication reduces Instagram API calls
- File cleanup prevents disk space issues
- Configurable timeout for OpenAI/Ollama processing
