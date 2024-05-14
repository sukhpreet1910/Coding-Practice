# 5 KYU: https://www.codewars.com/kata/5427db696f30afd74b0006a3/train/python

def bowling_score(rolls):
    total_score = 0  # Initialize the total score to zero
    total_frames_scored = 0  # Initialize the number of frames scored to zero
    current_roll = 0  # Initialize the current roll index to zero

    # Loop through the rolls while there are still rolls left and less than 10 frames have been scored
    while current_roll < len(rolls) and total_frames_scored < 10:
        if rolls[current_roll] != 10:  # If the current roll is not a strike
            pins = rolls[current_roll] + rolls[current_roll + 1]  # Sum the pins for the current frame
            if pins != 10: # If the frame is not a spare
                total_score += pins  # Add the pins to the total score
            else:  # If the frame is a spare
                total_score = 10 + rolls[current_roll + 2] # Add the spare bonus (next roll) to the score
            current_roll += 2 # Move to the next frame (2 rolls for a non-strike frame)
        else:  # If the current roll is a strike
            total_score = 10 + rolls[current_roll + 1] + rolls[current_roll + 2]  # Add the strike bonus (next 2 rolls) to the score
            current_roll = current_roll + 1# Move to the next roll (1 roll for a strike frame)

        total_frames_scored += 1  # Increment the frame counter

    return total_score 





print(bowling_score(([0] * 20)))