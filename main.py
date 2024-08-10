from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
from random import randint
from time import sleep

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

# CV2 text options for video display
font = cv2.FONT_HERSHEY_SIMPLEX 
font_size = 0.4 
thickness = 1 
line = cv2.LINE_4

computer_option_ind = 0
options = ["rock", "paper", "scissors"]

# CV2 text for the game
# this text should display the winner of a round (task 3)
winner = ""
# this text should display the choices of the user and computer (task 2)
game_update = ""
# this text should display the scores of both the user and computer after x rounds (task 3)
scores = ""
# this is text you can use for
# task 2: display the user action, e.g. rock, paper, scissors, start 
# task 3: tell the user when a new round is starting
string_to_display = ""

# The variables storing chosen options
# FOR TASK 3 ONLY

# Scores
# FOR TASK 4 ONLY

# A boolean that represents whether a game is in progress
# FOR TASK 3 ONLY

# A function that takes the user and computer choices and returns a string
# which states the winner of the round
def evaluate_round(user_choice, computer_choice):
    # TODO for task 3: 
    # write a function which takes the user and computer choices
    # and returns the winner
    print("Who wins?")


# We want to create an infinite loop for the live video..
# It stops when we press the Esc key on the video.
while True:
    # Grab the webcamera's image.
    ret, image = camera.read()
    
    image = cv2.flip(image, 1)
    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    
    # This is where we add text to directly on the live video feed
    # This needs to be done before we show the image. It'll update on every
    # iteration of the loop.
    cv2.putText(image, string_to_display, (0,50), font, font_size, (0, 0, 0), thickness, line)
    cv2.putText(image, scores, (0,100), font, font_size, (255, 0, 0), thickness, line)
    cv2.putText(image, game_update, (0,150),font, font_size, (255, 0, 0), thickness, line)
    cv2.putText(image, winner, (0,200), font, font_size,  (0, 0, 255), thickness, line)
  
    # Show the image in a window
    cv2.imshow("Webcam Image", image)
    
    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    confidence_score_print = str(np.round(confidence_score * 100))[:-2]
    
    # Print the prediction at each step 
    print(f"class name: {class_name}, confidence: {confidence_score_print}")

    # Just some nice variables to make things easier.
    rock = prediction[0][0]
    paper = prediction[0][1]
    scissors = prediction[0][2]
    neutral = prediction[0][3]
    start = prediction[0][4]

    # Some example text you should see on screen - look at the 
    # CV2 text at the top of the screen to update the correct
    # variables to know which ones to update.

    string_to_display = "Hello world!"

    # TASK 2 :TODO
    # Write some code that displays to the user what their action is

    # TASK 3 :TODO
    # Implement a single round of rock paper scissors with the computer choosing a random choice
    # For this, you can use a random number generator
    # See randint(start,end), which will return a random number inclusive of start
    # and end numbers for the computer
    # You will also need to complete the function declared 
    # `evaluate_round(user_choice, computer_choice)`

    # TASK 4: TODO
    # Implement a scoring system which updates after every round.
    # You should see something like, user: 2, computer: 3 


    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

# Make sure we shut everything down properly
camera.release()
cv2.destroyAllWindows()
