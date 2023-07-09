
%% Pelin Ozsezer 

sca
clc
clearvars
close all
AssertOpenGL; 

PsychDefaultSetup(2);                               
Screen('Preference', 'SkipSyncTests', 1);
screenNum = max(Screen('Screens')); % set screen 
Screen('Preference', 'VisualDebugLevel', 3);
[w, win.rect] = Screen('OpenWindow', screenNum, [100 100 100], [0 0 800 800]); %DO NOT tamper until final experiment is assembled
Screen('BlendFunction', w, 'GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA');
win.white           = WhiteIndex(screenNum);
win.black           = BlackIndex(screenNum);
win.backcolor       = win.black;
win.forecolor       = win.black;
[screenXpixels, screenYpixels] = Screen('WindowSize', w);              % window size
ifi = Screen('GetFlipInterval', w);                                    % frame duration (should save it)
Screen('BlendFunction', w, 'GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA');  % smoothing
Screen('TextFont', w, 'Ariel');
Screen('TextSize', w, 36);
[xCenter, yCenter] = RectCenter(win.rect); 














%% sample

% Psychtoolbox Example Script - Motion Quartet

% Clear the workspace and the screen
sca;
close all;
clearvars;

% Initialize Psychtoolbox
PsychDefaultSetup(2);
Screen('Preference', 'SkipSyncTests', 1); % Skip screen synchronization tests (for quicker debugging)
screenNumber = max(Screen('Screens'));

try
    % Open a window and get the screen properties
    [window, windowRect] = PsychImaging('OpenWindow', screenNumber, [0 0 0]);
    [screenXpixels, screenYpixels] = Screen('WindowSize', window);
    [xCenter, yCenter] = RectCenter(windowRect);
    
    % Set the text properties
    Screen('TextFont', window, 'Arial');
    Screen('TextSize', window, 30);
    Screen('TextColor', window, [255 255 255]);
    
    % Define the parameters for the rectangles
    rectSize = 200; % Size of each rectangle (pixels)
    rectColor = [255 255 255]; % Color of the rectangles
    
    % Calculate the positions of the rectangles
    positions = [xCenter-rectSize, yCenter-rectSize, xCenter+rectSize, yCenter+rectSize];
    
    % Set the motion directions for the rectangles
    motionDirections = [0, 90, 180, 270]; % In degrees
    
    % Set the speed of the rectangle motion (pixels per frame)
    rectSpeed = 5;
    
    % Set the duration of the stimulus (in seconds)
    stimulusDuration = 5;
    
    % Start the stimulus presentation
    startTime = GetSecs;
    while (GetSecs - startTime) < stimulusDuration
        % Calculate the position offsets for each rectangle
        offsets = rectSpeed * (GetSecs - startTime);
        
        % Draw the rectangles
        for i = 1:4
            rectPos = positions(i, :);
            rectPos = OffsetRect(rectPos, offsets * cosd(motionDirections(i)), offsets * sind(motionDirections(i)));
            Screen('FillRect', window, rectColor, rectPos);
        end
        
        % Flip the screen
        Screen('Flip', window);
    end
    
    % Clear the screen and close the window
    sca;
    
catch exception
    sca;
    disp(exception);
    rethrow(exception);
end
