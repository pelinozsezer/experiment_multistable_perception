
%% Pelin Ozsezer

sca
clc
clearvars
close all

% Break and issue an error message if the installed Psychtoolbox
% is not based on OpenGL or Screen() is not working properly
AssertOpenGL;


%% Screen setup
PsychDefaultSetup(2);
Screen('Preference', 'VisualDebugLevel', 3);
Screen('Preference', 'SuppressAllWarnings', 1);
Screen('Preference', 'SkipSyncTests', 1);
screens = Screen('Screens');
screenNumber = max(screens);
black = BlackIndex(screenNumber);
white = WhiteIndex(screenNumber);
gray = (black + white)/2;
[window, windowRect] = PsychImaging('OpenWindow', screenNumber, gray);
Screen('Flip', window);
[screenXpixels, screenYpixels] = Screen('WindowSize', window);
[xCenter, yCenter] = RectCenter(windowRect);



try
  
    % parameters of the apparent motion quartet
    imageSize = 200;    % Size of each image in the quartet
    spacing = 100;      % Spacing between the images
    duration = 2;       % Duration of each image in seconds
    delay = 0.5;        % Delay between each image in seconds

    % create the images for the quartet
    image1 = ones(imageSize, imageSize);
    image2 = zeros(imageSize, imageSize);
    image3 = zeros(imageSize, imageSize);
    image4 = ones(imageSize, imageSize);

    % positions for the images
    xPos = [screenXpixels/2-spacing, screenXpixels/2+spacing, screenXpixels/2-spacing, screenXpixels/2+spacing];
    yPos = screenYpixels/2;

    % Draw and flip 
    for i = 1:4
        Screen('PutImage', window, [image1 image2 image3 image4] * 255, [0 0 imageSize imageSize], [xPos(i) yPos xPos(i) yPos]);
        Screen('Flip', window);

        WaitSecs(duration);
        WaitSecs(delay);
    end

    % Wait for a key press to exit
    KbStrokeWait;
    sca;

catch
    sca;
    psychrethrow(psychlasterror);
end
