import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
extractor = ConllExtractor()

def main():   
    print("Hello, I am Marvin, the friendly robot.")
    print("You can end this conversation at any time by typing 'bye'")    
    print("After typing each answer, press 'enter'")
    print("How are you today?")

    while True:
 
        user_input = input("> ")

        if user_input.lower() == "bye":            
           
            break
        else:
            
            user_input_blob = TextBlob(user_input, np_extractor=extractor)                        
            np = user_input_blob.noun_phrases                                    
            response = ""

            if user_input_blob.polarity <= -0.5:
                response = "Negative Emotion Detected: Sadness "

            elif user_input_blob.polarity <= 0:
                response = "Negative Emotion Detected: Neutrality "

            elif user_input_blob.polarity <= 0.5:
                response = "Negative Emotion Detected: Pozitivity "

            elif user_input_blob.polarity <= 1:
                response = "Negative Emotion Detected: Pozitivity "

            if response == "Negative Emotion Detected: Sadness ":
                response = "Negativity is bad for your mental health. Sometimes telling your feelings to others can be helpfull. Do you consider to telling me more about that stuff"
                print(response)
                response2 = input(">")
                print("I really cannot understand due to the fact I'm just a program")
                
            if len(np) != 0:
                response = response + "Can you tell me more about " + np[0].pluralize() + "?"

            else:
                response = response + "Can you tell me more?"

            print(response)
    
    print("It was nice talking to you, goodbye!")

# Start the program
main()