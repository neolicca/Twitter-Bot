import tweepy
import time
import random

def main():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler("1z3rQObOuiRmnIG6ywLLsQN6h",
                            "WXCoj5Eh8k2ZhslDP7mmB7ESpnrxKyBHf8G4D0580lVPfrCrHw")
    auth.set_access_token("1011239315895013380-K3tac7dAIc8xaSlW96osSZRNbangWA",
                        "IYXiMB9y8Gycmw7wO6WL7Bzw4ceROB8rocAQOSii5QDgB")

    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    while True:
        random_number = random.randint(1,4)
        image_path = f'gifs/{random_number}.gif'
        api.update_with_media(image_path,'')
        print('Uploaded')
        time.sleep(1800)

if __name__ == "__main__":
    main()
    
