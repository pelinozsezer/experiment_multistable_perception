###############################
######### DEFINITIONS #########
###############################


### TRAINING PHASE ###
def training_phase(nx_trials_training):
    # 20 trials - z=horizontal & m=vertical
    
    corr_resp_training = 0
    accuracy_training = 0
    
    training_block_no = []
    training_trial_no = []
    training_motion_type = []
    training_key_response = []
    training_rt = []
    
    
    ## Values for height & weight
    
    # Values for extending horizontally
    width_val = []
    current_value = 17.5*scaler
    
    # Add values in the increasing phase
    while current_value <= 90*scaler:
        width_val.append(current_value)
        current_value += 3*scaler
    
    # Subtract values in the decreasing phase
    while current_value >= 17.5*scaler:
        width_val.append(current_value)
        current_value -= 3*scaler
    print(width_val)
    
    # Values for extending vertically
    height_val = []
    current_value = 17.5*scaler
    
    # Add values in the increasing phase
    while current_value <= 90*scaler:
        height_val.append(current_value)
        current_value += 3*scaler
    
    # Subtract values in the decreasing phase
    while current_value >= 17.5*scaler:
        height_val.append(current_value)
        current_value -= 3*scaler
    print(height_val)
    
    
    #
    import random
    training_phase = ['vertical'] * int(nx_trials_training/2) + ['horizontal'] * int(nx_trials_training/2)
    random.shuffle(training_phase)
    print(training_phase)
    
    
    # prepare stimuli
    width=20
    height=20
    
    upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
    upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
    lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
    lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
    stimuli = [upper_left, upper_right, lower_left, lower_right]
    
    
    while True:
        message = visual.TextStim(win, text='"z" for horizontal; \n "m" for vertical; \n "space" for continue.').draw()
        # message.autoDraw = True  # Automatically draw every frame
        win.flip()
        keyPressed = kb.waitKeys()
        if keyPressed == ["space"]:
            break
    # message.autoDraw = False
    
    # fixation cross
    fixation = visual.ShapeStim(win,
        vertices=((0, -0.05), (0, 0.05), (0,0), (-0.05,0), (0.05, 0)),
        lineWidth=75,
        closeShape=False,
        lineColor="white"
    )
    
    fixation.draw()
    win.flip()
    core.wait(2)
    
    
    training_block=0
    while accuracy_training < 0.9:
    
        
        if not training_block==0:
            while True:
                message = visual.TextStim(win, text='Accuracy is lower than 90%. \n It must be more than 90%. \n "space" to continue for more training.').draw()
                # message.autoDraw = True  # Automatically draw every frame
                win.flip()
                keyPressed = kb.waitKeys()
                if keyPressed == ["space"]:
                    break
    
    
        for trial_no in range(nx_trials_training):
    
            if training_phase[trial_no]=="vertical":
    
                fixation.draw()
                win.flip()
                core.wait(1)
    
                duration = 2 # seconds
    
                kb.getKeys()
                kb.clock.reset()
    
                for i in list(range(0,duration)):
    
                    # 1 second
                    for i in list(range(0,freq)):
    
    
                        for i in list(range(0,2)):
                            stimuli[i].draw()
    
                        win.flip()
                        core.wait((1/freq)/2)
    
    
                        for i in list(range(2,4)):
                            stimuli[i].draw()
                        win.flip()
                        core.wait((1/freq)/2)
    
    
                keyPressed = kb.getKeys()
    
                if keyPressed == []:
                    print('no response')
                    message = visual.TextStim(win, text='NO RESPONSE').draw()
                    win.flip()
    
                    training_block_no=training_block_no+[training_block+1]
                    training_trial_no=training_trial_no+[trial_no+1]
                    training_motion_type=training_motion_type+["vertical"]
                    training_key_response=training_key_response+["no response"]
                    training_rt= training_rt+ ["N/A"]
    
                    core.wait(1)
    
                elif keyPressed[0].name == "z":
                    print(keyPressed[0].name)
                    #print(keyPressed[1].name)
                    message = visual.TextStim(win, text='INCORRECT').draw()
                    win.flip()
    
                    training_block_no=training_block_no+[training_block+1]
                    training_trial_no=training_trial_no+[trial_no+1]
                    training_motion_type=training_motion_type+["vertical"]
                    training_key_response=training_key_response+["z"]
                    training_rt= training_rt+ [keyPressed[0].rt]
    
                    core.wait(1)
    
                elif keyPressed[0].name == "m":
                    print(keyPressed[0].name)
                    message = visual.TextStim(win, text='CORRECT').draw()
                    corr_resp_training=corr_resp_training+1
                    win.flip()
    
                    training_block_no=training_block_no+[training_block+1]
                    training_trial_no=training_trial_no+[trial_no+1]
                    training_motion_type=training_motion_type+["vertical"]
                    training_key_response=training_key_response+["m"]
                    training_rt= training_rt+ [keyPressed[0].rt]
    
                    core.wait(1)
    
                else:
                    print(keyPressed[0].name)
                    message = visual.TextStim(win, text='INCORRECT - except z & m').draw()
                    win.flip()
    
                    training_block_no=training_block_no+[training_block+1]
                    training_trial_no=training_trial_no+[trial_no+1]
                    training_motion_type=training_motion_type+["vertical"]
                    training_key_response=training_key_response+["other"]
                    training_rt= training_rt+ [keyPressed[0].rt]
    
                    core.wait(1)
    
    
            if training_phase[trial_no]=="horizontal":
    
                fixation.draw()
                win.flip()
                core.wait(1)
    
                duration = 2 # seconds
    
                kb.getKeys()
                kb.clock.reset()
    
                for i in list(range(0,duration)):
    
    
                    # 1 second
                    for i in list(range(0,freq)):
    
                        for i in list(range(1,4,2)):
                            stimuli[i].draw()
                        win.flip()
                        core.wait((1/freq)/2)
    
    
                        for i in list(range(0,3,2)):
    
                            stimuli[i].draw()
                        win.flip()
                        core.wait((1/freq)/2)
    
                keyPressed = kb.getKeys()
    
                if keyPressed == []:
                    print('no response')
                    message = visual.TextStim(win, text='NO RESPONSE').draw()
                    win.flip()
    
                    training_block_no=training_block_no+[training_block+1]
                    training_trial_no=training_trial_no+[trial_no+1]
                    training_motion_type=training_motion_type+["horizontal"]
                    training_key_response=training_key_response+["no response"]
                    training_rt= training_rt+ ["N/A"]
    
                    core.wait(1)
                elif keyPressed[0].name == "z":
                    print(keyPressed[0].name)
                    message = visual.TextStim(win, text='CORRECT').draw()
                    corr_resp_training=corr_resp_training+1
                    win.flip()
    
                    training_block_no=training_block_no+[training_block+1]
                    training_trial_no=training_trial_no+[trial_no+1]
                    training_motion_type=training_motion_type+["horizontal"]
                    training_key_response=training_key_response+["z"]
                    training_rt= training_rt+ [keyPressed[0].rt]
    
                    core.wait(1)
    
                elif keyPressed[0].name == "m":
                    print(keyPressed[0].name)
                    message = visual.TextStim(win, text='INCORRECT').draw()
                    win.flip()
    
                    training_block_no=training_block_no+[training_block+1]
                    training_trial_no=training_trial_no+[trial_no+1]
                    training_motion_type=training_motion_type+["horizontal"]
                    training_key_response=training_key_response+["m"]
                    training_rt= training_rt+ [keyPressed[0].rt]
    
                    core.wait(1)
    
                else:
                    print(keyPressed[0].name)
                    message = visual.TextStim(win, text='INCORRECT - except z & m').draw()
                    win.flip()
    
                    training_block_no=training_block_no+[training_block+1]
                    training_trial_no=training_trial_no+[trial_no+1]
                    training_motion_type=training_motion_type+["horizontal"]
                    training_key_response=training_key_response+["other"]
                    training_rt= training_rt+ [keyPressed[0].rt]
    
                    core.wait(1)
    
        accuracy_training = corr_resp_training/nx_trials_training
        training_block=training_block+1
        corr_resp_training=0
    
    
    # save data from training phase
    df = pd.DataFrame({'block': training_block_no, 'trial': training_trial_no, 'motion_type': training_motion_type, 'key_response': training_key_response, 'RT': training_rt})
    training_full_file_path = training_folder_path + '/' + training_file_name
    df.to_csv(training_full_file_path, index=False)
    print(f"Data saved to '{training_full_file_path}'")
    
    while True:
        message = visual.TextStim(win, text='Training phase has been succesfully completed. \n "space" to continue.').draw()
        # message.autoDraw = True  # Automatically draw every frame
        win.flip()
        keyPressed = kb.waitKeys()
        if keyPressed == ["space"]:
            break




## DEMONSTRATION PHASE OF EXPERIMENTAL PARADIGM ##

def demonstration_phase(nx_trials_demonstration):
    while True:
        message = visual.TextStim(win, text='DEMONSTRATION PHASE OF EXPERIMENTAL PARADIGM. \n "space" for continue.').draw()
        #message.autoDraw = True  # Automatically draw every frame
        win.flip()
        keyPressed = kb.waitKeys()
        if keyPressed == ["space"]:
            break
    
    
    width_val = []
    current_value = 17.5*scaler
    
    # Add values in the increasing phase
    while current_value <= 90*scaler:
        width_val.append(current_value)
        current_value += 3*scaler
    
    # Subtract values in the decreasing phase
    while current_value >= 17.5*scaler:
        width_val.append(current_value)
        current_value -= 3*scaler
    # Now, 'values' contains the desired array
    print(width_val)
    
    max_idx_width = width_val.index(max(width_val))
    
    
    
    height_val = []
    current_value = 17.5*scaler
    
    # Add values in the increasing phase
    while current_value <= 90*scaler:
        height_val.append(current_value)
        current_value += 3*scaler
    
    # Subtract values in the decreasing phase
    while current_value >= 17.5*scaler:
        height_val.append(current_value)
        current_value -= 3*scaler
    
    # Now, 'values' contains the desired array
    print(height_val)
    
    max_idx_height = height_val.index(max(height_val))
    
    
    
    
    
    
    message = visual.TextStim(win, text='Stimuli during the Experimental Phase')
    message.autoDraw = True  # Automatically draw every frame
    win.flip()
    core.wait(3.0)
    message.autoDraw = False
    
    
    
    flag_demonstration = True
    while flag_demonstration:
        
        for iteration in range(nx_trials_demonstration):
            
            idx_counter=0
            for width in width_val:
                print(width)
                height=(360/width)*scaler
                
                idx_counter += 1
                
                # prepare stimuli
                upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
                upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
                lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
                lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
                stimuli = [upper_left, upper_right, lower_right, lower_left]
                    
                if idx_counter <= max_idx_width:
                    message = visual.TextStim(win, text='extending horizontally', pos=[0, -60])
                    message.autoDraw = True  # Automatically draw every frame
                    
                    duration = 1 # seconds
                    for i in list(range(0,duration)):
                    
                        # 1 second
                        for i in list(range(0,freq)):
                        
                            for i in list(range(0,3,2)):
                                stimuli[i].draw()
                            win.flip()
                            core.wait((1/freq)/2)    
                            
                            for i in list(range(1,4,2)):
                                stimuli[i].draw()
                            win.flip()
                            core.wait((1/freq)/2)  
                     
                    message.autoDraw = False   
                        
                elif idx_counter> max_idx_width:
                    message = visual.TextStim(win, text='shrinking horizontally', pos=[0, -60])
                    message.autoDraw = True  # Automatically draw every frame
                    
                    duration = 1 # seconds
                    for i in list(range(0,duration)):
                    
                        # 1 second
                        for i in list(range(0,freq)):
                        
                            for i in list(range(0,3,2)):
                                stimuli[i].draw()
                            win.flip()
                            core.wait((1/freq)/2)    
                            
                            for i in list(range(1,4,2)):
                                stimuli[i].draw()
                            win.flip()
                            core.wait((1/freq)/2)  
                            
                    message.autoDraw = False   
                     
                # if len(kb.getKeys()) > 0: # if a key is pressed
                #     print('KEYYYYYYYY')
                #     # thisKey = kb.getKeys()
                #     # print(thisKey)
                #     break
            event.clearEvents()
            
            
            idx_counter=0
            for height in height_val:
                print(height)
                width=(360/height)*scaler
                
                idx_counter += 1
                
                # prepare stimuli
                upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=[1, 1, 1],lineColor=[11, 1, 1])
                upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
                lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
                lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
                stimuli = [upper_left, upper_right, lower_right, lower_left]
                
                
                if idx_counter <= max_idx_height:
                    message = visual.TextStim(win, text='extending vertically', pos=[0, -120])
                    message.autoDraw = True  # Automatically draw every frame
                    
                    duration =  1 # seconds
                    for i in list(range(0,duration)):
                    
                        # 1 second
                        for i in list(range(0,freq)):
                        
                            for i in list(range(0,3,2)):
                                stimuli[i].draw()
                            win.flip()
                            core.wait((1/freq)/2)    
                            
                            for i in list(range(1,4,2)):
                                stimuli[i].draw()
                            win.flip()
                            core.wait((1/freq)/2)  
                   
                            
                    message.autoDraw = False   
            
            
                elif idx_counter > max_idx_height:
                    message = visual.TextStim(win, text='shrinking vertically', pos=[0, -120])
                    message.autoDraw = True  # Automatically draw every frame
                    
                    duration =  1 # seconds
                    for i in list(range(0,duration)):
                    
                        # 1 second
                        for i in list(range(0,freq)):
                        
                            for i in list(range(0,3,2)):
                                stimuli[i].draw()
                            win.flip()
                            core.wait((1/freq)/2)    
                            
                            for i in list(range(1,4,2)):
                                stimuli[i].draw()
                            win.flip()
                            core.wait((1/freq)/2)  
                            
                            
                            
                    message.autoDraw = False   
                     
                # if len(kb.getKeys()) > 0: # if a key is pressed
                #     print('KEYYYYYYYY')
                #     # thisKey = kb.getKeys()
                #     # print(thisKey)
                #     break
            event.clearEvents()
            
            
            
        message = visual.TextStim(win, text='End of demonstration')
        message.autoDraw = True  # Automatically draw every frame
        win.flip()
        core.wait(2.0)
        message.autoDraw = False  # Automatically draw every frame
    
    
        
    
        # ask participants if they want more
        while True:
            message = visual.TextStim(win, text='Would you like more demonstration? \n Press y for yes. \n Press n for no.').draw()
            #message.autoDraw = True  # Automatically draw every frame
            win.flip()
            keyPressed = kb.waitKeys()
            if keyPressed == ["y"]:
                flag_demonstration = True
                break
            elif keyPressed == ["n"]:
                message = visual.TextStim(win, text='continuing to the experimental phase')#.draw()
                message.autoDraw = True  # Automatically draw every frame
                win.flip()
                core.wait(5.0)
                message.autoDraw = False  # Automatically draw every frame
                
                flag_demonstration = False
                break











#def draw_motquarts(stimulus_size, freq, height, width):
