from google import genai
from google.genai import errors  # Import the official error module
from config import GOOGLE_API_KEY
import time


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(api_key=GOOGLE_API_KEY)

    def generate(self, prompt: str):
        retries = 3
        # Start with a 30-second delay, which doubles each time
        delay = 30 

        for attempt in range(retries):
            try:
                response = self.client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                return response.text

            except errors.APIError as e:
                # If it's a quota issue (429), log it and wait
                if e.code == 429:
                    print(f"⚠️ Quota hit on attempt {attempt+1}/{retries}. Retrying in {delay}s...")
                else:
                    print(f"❌ API Error {e.code} hit on attempt {attempt+1}/{retries}...")

                if attempt < retries - 1:
                    time.sleep(delay)
                    delay *= 2  # Double the wait time for the next attempt (Exponential Backoff)
                else:
                    raise e
                    
            except Exception as e:
                # Catch any unexpected system/network crashes immediately
                print(f"Unexpected error: {e}")
                raise e