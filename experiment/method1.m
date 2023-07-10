
%% Pelin Ozsezer

%% Screen Set-up
sca
clc
clearvars
close all

% Break and issue an error message if the installed Psychtoolbox
% is not based on OpenGL or Screen() is not working properly
AssertOpenGL;

try
    PsychDefaultSetup(2);
    Screen('Preference', 'VisualDebugLevel', 3);
    Screen('Preference', 'SuppressAllWarnings', 1);
    Screen('Preference', 'SkipSyncTests', 1); % be aware!

    screenNum = max(Screen('Screens'));
    black = [1/255 1/255 1/255];
    white = WhiteIndex(screenNum);
    [window, windowRect] = PsychImaging('OpenWindow', screenNum, black);
    Screen('Flip', window);

    %% draw fixation cross
    crossColor = [255 255 255];
    crossSize = 20;
    crossWidth = 2;

    % coordinates
    xCoords = [-crossSize crossSize 0 0];
    yCoords = [0 0 -crossSize crossSize];
    allCoords = [xCoords; yCoords];

    % center the cross on the screen
    xPos = screenXpixels / 2;
    yPos = screenYpixels / 2;

    Screen('DrawLines', window, allCoords, crossWidth, crossColor, [xPos yPos]);
    Screen('Flip', window);


catch
    sca
    Screen('Close')
end


MovingLineDemo([xv=10][, twolines=0][, screenid=max])
ScreenDrawDots(windowPtr, xy [, dotdiameter=1][, dotcolor=white][, center2D][, dot_type=1]);





%% sample - draw 4 rectangles for a single motion quartet

try
    % screen setup
    [screenXpixels, screenYpixels] = Screen('WindowSize', window);
    [xCenter, yCenter] = RectCenter(windowRect);

    % parameters for rectangles
    rectSize = 200; % Size of each rectangle (pixels)
    rectColor = [255 255 255]; % white

    %  positions
    positions = [xCenter-rectSize, yCenter-rectSize, xCenter+rectSize, yCenter+rectSize];

    % Set the motion directions for the rectangles
    motionDirections = [0, 90, 180, 270]; % In degrees

    % Set the speed of the rectangle motion (pixels per frame)
    rectSpeed = 5;

    % Set the duration of the stimulus (in seconds)
    stimulusDuration = 10;
    % WaitSecs(10)

    % Start the stimulus presentation
    startTime = GetSecs;


    % Draw the rectangles
    for i = 1:4
        rectPos = positions(i, :);
        rectPos = OffsetRect(rectPos, offsets * cosd(motionDirections(i)), offsets * sind(motionDirections(i)));
        Screen('FillRect', window, rectColor, rectPos);
        Screen('BlendFunction', w, 'GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA'); % smoothing

    end

    Screen('Flip', window);


    % Clear the screen and close the window
    sca;

catch exception
    sca;
    disp(exception);
    rethrow(exception);
end
