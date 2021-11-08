# Lief Johnson
# joh19151
# CSCI 1133 Section 050
# Assignment 2

#==========================================
# Purpose: This function takes the current state of a rocket and the button pressed, and then computes the current state as a result
# Input Parameter(s): current_state represents the current state of the rocket and button represents the button pressed
# Return Value(s): The updated state gets returned to the console
#==========================================

def launch_rocket(current_state, button):

    if current_state == "IDLE" and button == "start_btn":
        new_state = "READY"

    elif current_state == "READY" and button == "safe_btn":
        new_state = "SAFE"

    elif current_state == "SAFE" and button == "launch_btn":
        new_state = "LAUNCH"

    else:
        new_state = "IDLE"

    # prints launch if new_state is set to launch at any point during the previous code
    if new_state == "LAUNCH":
        print("\'LAUNCH\'")
        new_state = "IDLE"

    return new_state
