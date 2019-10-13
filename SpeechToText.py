# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:09:25 2019

@author: LEo
"""
COMMAND_VERBS = ["circle", "radius","rectangle","extrude","object","axis", "sketch", "sphere", "ketchup", "plane", "view", "cm", "centimeter", "centimeters", "mm", "millimiter", "millimeters", "m", "meter", "meters"]

list_commands = []

import speech_recognition as sr
import csv

def export_file():
    #f = open("intructions.txt", "w")
    
    with open("instructions.csv","w") as f:
        wr = csv.writer(f)
        wr.writerows(list_commands)
#    
#    for ele in list_commands:
#        print(ele)
#        for items in ele:
#            print(str(ele), file=f)
#        #for com in ele:
#            #print(str(com), file=f)
#        #print("\n", file=f)
            

def recognize_speech_from_file(recognizer, lan):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    sound = sr.AudioFile('1.wav') #redo 2,3,4,8 5 is not well defined
    with sound as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio, language = lan)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def behaviour(ele, command_raw, i, max_n):
     
    #use dictionaries to make decision tree
    
    symmetric = False #assume false
    revolve = False
    RectangularPattern = False
    x = 0
    y = 0
    z = 0
    x2 = 0
    y2 = 0
    z2 = 0
    
    j = 0
    if ele == "circle":
        circle = []
        commands_av = command_raw[i+1:]
        for com in commands_av:
            if com == "in":
                x = commands_av[j+1] #save next number
                y = commands_av[j+2] #save next number
                z = commands_av[j+3] #save next number
#                units_center = commands_av[j+4]
            if com == "radius":
                radius = commands_av[j+1] #save next number
                break
            j+=1
        circle.append("Circle")
        circle.append(radius)
        circle.append(x)
        circle.append(y)
        circle.append(z)
        list_commands.append(circle)       
        
    
    if ele == "rectangle":
        rectangle = [] #hacer la lista
        rectangle.append("Rectangle")
        commands_av = command_raw[i+1:]
        for com in commands_av:
            if (com == "plane") or (com == "plain") or (com == "playing"):
                if commands_av[j+1] == "top":#xy
                    plane = "xy"
                if commands_av[j+1] == "front":#xz
                    plane = "xz"
                if commands_av[j+1] == "right":#yz
                    plane = "yz"
                rectangle.append(plane)
            if (com == "in") and (plane == "xy"):
                x = commands_av[j+1] #save next number
                y = commands_av[j+2] #save next number
                z = commands_av[j+3] #save next number
#                units_center = commands_av[j+4]
                rectangle.append(x)
                rectangle.append(y)
                rectangle.append(z)
            if ( commands_av[j+4] == "and") and (plane == "xy"):
                x2 = commands_av[j+5] #save next number
                y2 = commands_av[j+6] #save next number
                rectangle.append(x2)
                rectangle.append(y2)
#                units_center = commands_av[j+3]
                break
                
            if (com == "in") and (plane == "xz"):
                x = commands_av[j+1] #save next number
                y = commands_av[j+2] #save next number
                z = commands_av[j+3] #save next number
                rectangle.append(x)
                rectangle.append(y)
                rectangle.append(z)
#                units_center = commands_av[j+4]
                
            if (commands_av[j+4] == "and") and (plane == "xz"):
                x2 = commands_av[j+5] #save next number
                z2 = commands_av[j+6] #save next number
                rectangle.append(x2)
                rectangle.append(z2)
#                units_center = commands_av[j+3]
                break
            
            if (com == "in") and (plane == "yz"):
                x = commands_av[j+1] #save next number
                y = commands_av[j+2] #save next number
                z = commands_av[j+3] #save next number
                rectangle.append(x)
                rectangle.append(y)
                rectangle.append(z)
                #units_center = commands_av[j+4]
            if (commands_av[j+4] == "and") and (plane == "yz"):
                x2 = x
                y2 = commands_av[j+5] #save next number
                z2 = commands_av[j+6] #save next number
                rectangle.append(y2)
                rectangle.append(z2)
#                units_center = commands_av[j+3]
                break
            j+=1
        list_commands.append(rectangle) 
        
            
    if (ele == "sketch") or (ele == "ketchup"):
        sketch = []
        sketch.append("NewSketch")
        if (i+1) < (max_n-1):
            commands_av = command_raw[i+1:]
            if commands_av[1] == "top":
                sketch.append("top")
            elif commands_av[1] == "right":
                sketch.append("right")
            elif commands_av[1] == "front":
                sketch.append("front")
            else:
                sketch.append("top")
        
            sketch.append(True)
            #make new sketch then reset to false
        list_commands.append(sketch)
        
    if ele == "axis":
        axis = []
        axis.append("Axis")
        commands_av = command_raw[i+1:]
        for com in commands_av:
            if com == "from":
                x = commands_av[j+1] #save next number
                y = commands_av[j+2] #save next number
                z = commands_av[j+3] #save next number
                x2 = 0
                y2 = 0
                z2 = 0
            if (commands_av[j+1] == "to") or (commands_av[j+1] == "2"):
                x2 = commands_av[j+2] #save next number
                y2 = commands_av[j+3] #save next number
                z2 = commands_av[j+4] #save next number
                break
            j+=1
        axis.append(x)
        axis.append(y)
        axis.append(z)
        axis.append(x2)
        axis.append(y2)
        axis.append(z2)
        list_commands.append(axis)
        
        
    if ele == "sphere":
       sphere = []
       sphere.append("Sphere")
       commands_av = command_raw[i+1:]
       for com in commands_av:
           
           if com == "in":
               x = commands_av[j+1] #save next number
               y = commands_av[j+2] #save next number
               z = commands_av[j+3] #save next number7
                
               if (commands_av[j+4] == "with") and (commands_av[j+5] == "radius"):
                   radius = commands_av[j+6]
               break
           j+=1
       sphere.append(radius)
       sphere.append(x)
       sphere.append(y)
       sphere.append(z)
       list_commands.append(sphere)
           
                   
    if ele == "extrude":
        extrude = []
        extrude.append("Extrude")
        distance = 2
        commands_av = command_raw[i+1:]
        for com in commands_av:
            if com == "distance":
                distance = commands_av[j+1] #save next number
                if (i+2) < (max_n-1):
                    if commands_av[j+2] == "symmetric":
                        symmetric = True
                        break
                break
            j+=1
        extrude.append(distance)
        extrude.append(symmetric)
        list_commands.append(extrude)
    
    if ele == "revolve":
        rev = []
        rev.append("Revolve")
        commands_av = command_raw[i+1:]
        rev.append(commands_av[1])
        revolve = True
        rev.append(revolve)
        list_commands.append(revolve)
    
    if ele == "loft":
        loft = []
        loft.append("Loft")
        #commands_av = command_raw[i+1:]
        #for com in commands_av:
        #    if com == "between":
        #        object0 = commands_av[j+1]
        #    if com == "and":
        #        object1 = commands_av[j+1]
        #        break
        #    j+=1
        #loft.append(object0, object1)
        list_commands.append(loft)
    
    if ele == "rectangular":
        rec_pattern = []
        rec_pattern.append("Rectangular_Pattern")
        commands_av = command_raw[i+1:]
        if commands_av[1] == "pattern":
            RectangularPattern = True
            Nx = commands_av[2] 
            dx = commands_av[3] 
            Ny = commands_av[4] 
            dy = commands_av[5] 
        
        rec_pattern.append(Nx,dx,Ny,dy)
        list_commands.append(rec_pattern)
                    

if __name__ == "__main__":
        
    lan ='en-US'
        
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    
    guess = recognize_speech_from_file(recognizer, lan)
    
    command_raw = guess["transcription"].lower().split()
    command = []
    i = 0
    
    for ele in command_raw:
        if ele == "to":
            command_raw[i] = 2
        if ele == "fear":
            command_raw[i] = "circle"
        if ele == "into":
            temp = []
            for j in range(i+1, len(command_raw)):
                temp.append(command_raw[j]) 
            command_raw[i] = "in"
            command_raw[i+1] = 2    
            for l in range(0 , len(command_raw) - i -2):
                command_raw[i+2+l] = temp[l]
            command_raw.append(temp[l+1])
        if ele == "one":
            command_raw[i] = 1
        if ele == "two":
            command_raw[i] = 2    
        if ele == "three":
            command_raw[i] = 3
        if ele == "four":
            command_raw[i] = 4
        if ele == "five":
            command_raw[i] = 5
        if ele == "six":
            command_raw[i] = 6
        if ele == "seven":
            command_raw[i] = 7
        if ele == "eight":
            command_raw[i] = 8
        if ele == "nine":
            command_raw[i] = 9
        if ele == "there":
            command_raw[i] = "sphere" 
        i +=1
    
    i=0
    for ele in command_raw:
        if ele == "to":
            ele = 2
            command_raw[i] = ele
        for com in COMMAND_VERBS:
            if ((ele == com) ):
                command.append(ele)
                behaviour(ele, command_raw, i, len(command_raw))
                break
        i+=1
    
    export_file()
    


