# Product Context: Instagram To Mealie

## Problem Statement

Many food enthusiasts and home cooks discover recipes on Instagram from food bloggers, chefs, and cooking channels. However, Instagram is not designed for recipe management, making it difficult to:

1. Save recipes in a structured format
2. Organize recipes for future reference
3. Access recipes offline or when cooking
4. Scale ingredients or make modifications
5. Create shopping lists from recipes

Mealie, on the other hand, is a dedicated recipe management system with features specifically designed for storing, organizing, and using recipes. However, manually transferring recipes from Instagram to Mealie is time-consuming and error-prone.

## Solution

InstagramToMealie bridges this gap by providing an automated way to import recipes from Instagram directly into Mealie. The application:

1. Takes an Instagram post URL as input
2. Downloads the post content, including images and videos
3. Uses Mealie's AI capabilities (via OpenAI/Ollama) to extract and structure the recipe information
4. Creates a properly formatted recipe in Mealie
5. Attaches the original images and videos as recipe assets
6. Links back to the original Instagram post

## User Experience Goals

### Primary User Flow

1. User finds a recipe on Instagram they want to save
2. User copies the Instagram post URL
3. User navigates to InstagramToMealie
4. User pastes the URL and submits
5. InstagramToMealie processes the post and creates a recipe in Mealie
6. User receives confirmation of successful import

### Alternative User Flow (Automation)

1. User finds a recipe on Instagram they want to save
2. User shares the post to a shortcut/automation on their device
3. The automation sends the URL to InstagramToMealie via a direct API call
4. InstagramToMealie processes the post and creates a recipe in Mealie
5. The automation receives confirmation of successful import

## Target Users

1. **Home Cooks**: Individuals who regularly cook at home and discover recipes on social media
2. **Food Enthusiasts**: People who collect and organize recipes from various sources
3. **Mealie Users**: Existing users of Mealie who want to streamline their recipe collection process
4. **Tech-Savvy Cooks**: Users who appreciate automation and integration between their digital tools

## Value Proposition

1. **Time Savings**: Eliminates manual copying and formatting of recipes
2. **Accuracy**: Reduces errors in transcription through automation
3. **Completeness**: Captures all aspects of the recipe, including images and videos
4. **Organization**: Places recipes in a system designed for recipe management
5. **Accessibility**: Makes recipes available across devices and offline through Mealie
6. **Automation**: Enables integration with other tools and workflows

## Success Metrics

1. **Conversion Rate**: Percentage of Instagram posts successfully converted to Mealie recipes
2. **User Adoption**: Number of active users utilizing the tool
3. **Automation Usage**: Percentage of imports coming through the automation endpoint
4. **Error Rate**: Frequency of failed conversions or errors
5. **User Satisfaction**: Feedback on the quality and accuracy of imported recipes
