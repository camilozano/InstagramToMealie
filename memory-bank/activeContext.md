# Active Context: Instagram To Mealie

## Current Status

InstagramToMealie is a functional application that successfully converts Instagram posts to Mealie recipes. The core functionality is implemented and working, with both web interface and API access available.

## Recent Changes

- Initial implementation of the core functionality
- Docker containerization for easy deployment
- Support for both session-based and credential-based Instagram authentication
- Integration with Mealie's OpenAI/Ollama-powered recipe extraction

## Current Focus

The current focus is on stabilizing the application and improving its reliability, particularly around:

1. Instagram authentication and session management
2. Handling of different types of Instagram content (posts, reels, etc.)
3. Error handling and recovery
4. User feedback and status reporting

## Active Decisions

### Authentication Strategy

The application currently supports two authentication methods for Instagram:

1. **Session-based authentication** (recommended): Uses a session file generated from Firefox cookies
2. **Credential-based authentication** (fallback): Uses username/password with optional TOTP

The decision to prioritize session-based authentication was made due to:
- Reduced risk of rate limiting
- Better reliability
- Improved security (no need to store passwords)
- Support for accounts with 2FA enabled

### Media Handling

The application downloads and processes both images and videos from Instagram posts:

1. Images are used as the recipe's main image
2. Videos are attached as recipe assets
3. Temporary files are created during processing and cleaned up afterward

This approach ensures that all media content is preserved while maintaining clean file management.

### Error Handling

The current error handling strategy focuses on:

1. Validating environment variables at startup
2. Graceful handling of Instagram and Mealie API errors
3. Cleanup of temporary files even in error cases
4. Clear error messages propagated to the user interface

## Key Considerations

### Instagram Limitations

Instagram's API limitations and anti-scraping measures present ongoing challenges:

1. Rate limiting can block access if too many requests are made
2. Authentication is complex and subject to security measures
3. Session files expire and need to be regenerated
4. Instagram's structure may change, breaking the scraping functionality

### Mealie Integration

The integration with Mealie relies on:

1. OpenAI/Ollama for recipe extraction
2. API access for recipe creation and media upload
3. Proper handling of recipe metadata

### User Experience

The user experience is designed to be simple and straightforward:

1. Single-field form for URL input
2. Clear status messages
3. Support for automation via URL parameters
4. Minimal dependencies and setup requirements

## Next Steps

1. **Improve error handling**: Add more specific error messages and recovery strategies
2. **Enhance session management**: Implement session refresh and validation
3. **Expand media support**: Improve handling of multi-image posts and stories
4. **Add logging**: Implement comprehensive logging for troubleshooting
5. **Improve documentation**: Enhance setup and usage documentation
