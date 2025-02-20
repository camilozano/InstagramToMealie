import os
import google.generativeai as genai
from typing import Optional
import time

class VideoProcessor:
    """Helper class for processing recipe videos using Google's Gemini AI."""
    
    def __init__(self):
        """Initialize the VideoProcessor with Gemini API configuration."""
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError('GEMINI_API_KEY environment variable is required')
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

    def process_video(self, video_path: str) -> Optional[str]:
        """
        Process a video file and return recipe markdown.
        
        Args:
            video_path (str): Path to the video file to process
            
        Returns:
            Optional[str]: Markdown formatted recipe text, or None if processing fails
            
        Raises:
            Exception: If video processing or API requests fail
        """
        try:
            # Upload video to Gemini
            print(f"Uploading video: {video_path}")
            video_file = genai.upload_file(path=video_path)
            
            # Wait for processing
            while video_file.state.name == "PROCESSING":
                print("Waiting for video processing...")
                time.sleep(10)
                video_file = genai.get_file(video_file.name)
                
            if video_file.state.name == "FAILED":
                raise ValueError(f"Video processing failed: {video_file.state.name}")
                
            print("Video processing complete. Generating recipe...")
            
            # Process with a recipe-focused prompt
            prompt = """
            Analyze this recipe video and create a complete recipe in markdown format.
            Include the following sections:
            
            1. Recipe title (as a level 1 heading)
            2. Brief description of the dish
            3. Preparation time and cooking time
            4. List of ingredients with measurements
            5. Step-by-step cooking instructions
            6. Any notes or tips shown in the video
            
            Use proper markdown formatting:
            - Use appropriate heading levels (# for title, ## for sections)
            - Use unordered lists for ingredients
            - Use ordered lists for instructions
            - Preserve any specific measurements or timing mentioned
            - Include any special equipment needed
            
            Focus on accuracy and clarity in the recipe instructions.
            """
            
            response = self.model.generate_content(
                [prompt, video_file],
                request_options={
                    "timeout": 600,  # 10 minute timeout
                }
            )
            
            # Cleanup
            print("Cleaning up uploaded file...")
            genai.delete_file(video_file.name)
            
            if not response.text:
                raise ValueError("No recipe content generated")
                
            return response.text
            
        except Exception as e:
            print(f"Error processing video: {str(e)}")
            # Attempt cleanup in case of error
            if 'video_file' in locals():
                try:
                    genai.delete_file(video_file.name)
                except:
                    pass
            raise Exception(f"Video processing error: {str(e)}")
