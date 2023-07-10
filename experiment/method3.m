% size and position of each stimulus in the quartet
stimulusSize = 100;
stimulusPositions = [screenXpixels/4, screenYpixels/2;
    screenXpix2els/2, screenYpixels/2;
    3*screenXpixels/4, screenYpixels/2];


frameDuration = 0.5; % in seconds
numFrames = 6; % number of frames for each stimulus
stimulusColor = [255 255 255]; % white

% create a vector of x-coordinates for each frame
xCoords = linspace(-stimulusSize/2, stimulusSize/2, numFrames);

% display each frame of the apparent motion quartet
for frame = 1:numFrames
    % Clear the screen
    Screen('FillRect', window, [0 0 0]);

    % each stimulus in the quartet
    for stimulus = 1:4
        xPos = stimulusPositions(stimulus, 1) + xCoords(frame);
        yPos = stimulusPositions(stimulus, 2);
        rect = CenterRectOnPoint([0 0 stimulusSize stimulusSize], xPos, yPos);
        Screen('FillRect', window, stimulusColor, rect);
    end
    Screen('Flip', window);
    WaitSecs(frameDuration);
end
KbStrokeWait
sca