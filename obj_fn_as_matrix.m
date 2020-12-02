%% Amanda Dings
% CS 534 Project
% Creating objective matrix which represents a 2D obstacle course

clc; clear variables; close all;
%% Step 1 Create a "simple" objective fn
% i.e. a function which represents an empty obstacle field

% Create 2D representation of the field we want
% Define start and end nodes
start_loc = [900,900];  % starting point (mm)
end_loc   = [101,101];  % ending point   (mm)  

% Define the domain
x = 1:1001;
y = 1:1001;
[X,Y] = meshgrid(x,y);

% Define the overal slope of the plane
field = (200/450).*X+(200/850).*Y+20;

% Make a "hill" at the start node
x = -101:101;
y = -101:101;
[x_hill, y_hill] = meshgrid(x,y);
hill = -0.01.*x_hill.^2 -0.01.*y_hill.^2;
field(799:1001,799:1001) = field(799:1001,799:1001)+hill+204.020;

% Make a "valley" at the end node
valley = 0.01.*x_hill.^2 + 0.01*y_hill.^2;
field(1:203,1:203) = field(1:203,1:203)+valley-204.020;

% Plot the field we end up with
colormap(jet)
surf(field,'edgealpha',0.0,'facealpha',0.0)
title(sprintf('Start: (900, 900)\nEnd: (101, 101)'))
hold on

% Emphasize the starting and ending points
plot3(start_loc(1),start_loc(2),field(start_loc(1),start_loc(2)),...
    '.r','markersize',45)
plot3(end_loc(1),end_loc(2),field(end_loc(1),end_loc(2)), ...
    '.g','markersize',45)

% Save field to disk
%save('no_obstacles.mat', 'field')

% Create 2D representation of the field
view(2)
plot3([1000 1000],[0 1000], [0,0],'-k','linewidth',5)
plot3([0 1000],[1000 1000], [0,0],'-k','linewidth',5)
plot3([0 0],[0 1000], [0,0],'-k','linewidth',5)
plot3([0 1000],[0 0], [0,0],'-k','linewidth',5)
%% Step 2 Create an objective fn with obstacles
obs = 500*ones(101);  % a rectangular prism, 101x101x500
field(350:450,150:250) = field(350:450,150:250) + obs; % center: (200,400)
field(550:650,550:650) = field(550:650,550:650) + obs; % center: (600,600)

% Plot the field we end up with
figure
colormap(jet)
surf(field,'edgealpha',0.0,'facealpha',0.0)%,'facealpha',0.2)
title(sprintf('Start: (900, 900)\nEnd: (101, 101)'))
hold on

% Emphasize the starting and ending points
plot3(start_loc(1),start_loc(2),field(start_loc(1),start_loc(2)),...
    '.r','markersize',45)
plot3(end_loc(1),end_loc(2),field(end_loc(1),end_loc(2)), ...
    '.g','markersize',45)

% save field to disk
save('some_obstacles.mat','field')
r = rectangle('position',[150,350,100,100]);
r.FaceColor='k'
r = rectangle('position',[550,550,100,100])
r.FaceColor='k'
view(2)
plot3([1000 1000],[0 1000], [0,0],'-k','linewidth',5)
plot3([0 1000],[1000 1000], [0,0],'-k','linewidth',5)
plot3([0 0],[0 1000], [0,0],'-k','linewidth',5)
plot3([0 1000],[0 0], [0,0],'-k','linewidth',5)