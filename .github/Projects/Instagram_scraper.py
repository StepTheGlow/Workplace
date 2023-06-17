import instaloader
import requests
import json

def scrape_instagram_posts(profiles, webhook_url):
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
            requests.post(webhook_url, json=post_data)
            
        except instaloader.exceptions.ProfileNotExistsException:
            print(f"Profile '{profile}' does not exist.")
        
        except IndexError:
            print(f"No posts found for profile '{profile}'.")
        
        except requests.exceptions.RequestException as e:
            print(f"Webhook request failed: {e}")

# Example usage
instagram_profiles = ['profile1', 'profile2', 'profile3']
webhook_url = 'https://your-webhook-url.com'

scrape_instagram_posts(instagram_profiles, webhook_url)
