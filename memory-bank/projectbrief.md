# Project Brief: Instagram To Mealie

## Overview
InstagramToMealie is a web application that converts Instagram posts into recipes in Mealie (a recipe management system). It allows users to input an Instagram post URL, and the application will download the post, extract the content, and create a new recipe in Mealie with the associated image or video assets.

## Core Requirements

1. **Instagram Integration**
   - Download posts from Instagram using a valid URL
   - Extract content, images, and videos from Instagram posts
   - Support for both regular posts and reels
   - Handle Instagram authentication via session files or credentials

2. **Mealie Integration**
   - Create recipes in Mealie from Instagram post content
   - Upload images and videos as recipe assets
   - Set the original URL as the source
   - Support for tagging recipes based on Instagram tags

3. **User Interface**
   - Simple web interface for inputting Instagram URLs
   - Support for direct URL input via query parameters (for automation)
   - Status indicators for processing state
   - Error handling and user feedback

4. **Deployment**
   - Docker-based deployment
   - Environment variable configuration
   - Integration with existing Mealie installations

## Technical Goals

1. **Reliability**
   - Robust error handling
   - Cleanup of temporary files
   - Graceful handling of API limitations

2. **Security**
   - Secure handling of credentials
   - Support for session-based authentication
   - Environment variable-based configuration

3. **Usability**
   - Simple, intuitive interface
   - Support for automation via URL parameters
   - Clear error messages and status indicators

## Constraints

1. **Instagram Limitations**
   - Rate limiting
   - Authentication complexity
   - Session management

2. **Mealie Requirements**
   - Requires OpenAI/Ollama configuration in Mealie
   - API key authentication
   - Handling of media uploads

## Success Criteria

1. Successfully download and process Instagram posts
2. Create properly formatted recipes in Mealie
3. Handle both images and videos appropriately
4. Provide clear feedback to users
5. Support both manual and automated usage
