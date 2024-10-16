"""
Instagram scraper module.
"""

import instaloader
import requests
import json

WEBHOOK_URL = "https://example.com/webhook"

def scrape_instagram_posts(profiles):
    """
    Function to scrape Instagram posts and send them as a webhook payload.
    Args:
        profiles (list): List of Instagram profiles to scrape.
    """
    L = instaloader.Instaloader()
    
    for profile in profiles:
        try:
            # Load the profile using the username
            user = instaloader.Profile.from_username(L.context, profile)
            # Get the most recent post
            post = user.get_posts()[0]
            
            # Extract the required data points
            post_data = {
                'image_or_video': post.url,
                'caption': post.caption,
                'username': post.owner_username
            }
            
            # Send the data as a webhook payload
            requests.post(WEBHOOK_URL, json=post_data)
            
        except instaloader.exceptions.ProfileNotExistsException:
            print(f"Profile '{profile}' does not exist.")
        
        except IndexError:
            print(f"No posts found for profile '{profile}'.")
        
        except requests.exceptions.RequestException as e:
            print(f"Webhook request failed: {e}")

# Example usage
INSTAGRAM_PROFILES = ['profile1', 'profile2', 'profile3']

if __name__ == "__main__":
    scrape_instagram_posts(INSTAGRAM_PROFILES)
    
