%% Amanda Dings
% CS 534 Project
% Creating objective matrix which represents a 2D obstacle course

clc; clear variables; close all;
%% Step 1 Create a "simple" objective fn
% i.e. a function which represents an empty obstacle field

% Create 2D representation of the field we want
% Define start and end nodes
start_loc = [900,900];  % starting point (mm)
%end_loc   = [101,101];  % ending point   (mm)  
end_loc = [80,90];

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
%save('no_obstacles.mat', 'field')  % note: minimum is at (90,80)!
                                    %       maximum is at (912,922)

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
s=surf(field,'edgealpha',0.0,'facealpha',0.0)%,'facealpha',0.2)
title(sprintf('Start: (900, 900)\nEnd: (101, 101)'));
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


%% Make plots of results
% using kirsten's data but eventually it will be averaged among us all
sma_some_obstacles_x = [900 ...
                        800 ...
                        700 ...
                        602.23541179 ...
                        547.6148882 ...
                        447.6148882 ...
                        347.6148882 ...
                        247.6148882 ...
                        147.6148882 ...
                        78.85107675 ...
                        78.79448071];
sma_some_obstacles_y =  [900 ...
                         800 ...
                         700 ...
                         650.38528421 ...
                         551.71661835 ...
                         451.71661835 ...
                         351.71661835 ...
                         251.71661835 ...
                         151.71661835 ...
                         89.23605288 ...
                         88.96707247];
sma_some_obstacles_z = interp2(field,sma_some_obstacles_x, sma_some_obstacles_y); % 2d table lookup
plot3(sma_some_obstacles_x, sma_some_obstacles_y, sma_some_obstacles_z, '.-b',...
    'LineWidth',5,'MarkerSize',5)

%view(3)
%s.FaceAlpha=0.5;
%s.EdgeAlpha=0.1;






%% Data & shit
% some_obstacles results (SMA)
% Global Best Solution:
% [78.85679782 89.22777493]
% <class 'numpy.ndarray'>
% [[900.         900.        ]
%  [800.         800.        ]
%  [700.         700.        ]
%  [600.         650.37134488]
%  [500.         550.37134488]
%  [400.         450.37134488]
%  [300.         350.37134488]
%  [200.         250.37134488]
%  [100.         150.37134488]
%  [ 78.97384695  88.95362632]
%  [ 78.73103306  89.04949513]]
% Total Distance: [1592.24828161]
% Original SMA Best Fit: [-121.00895831]
% SMA Time Elapsed:  70.45086739499999

% some_obstacles results (GWO)
% Global Best Solution:
% [78.62909453 89.57857042]
% <class 'numpy.ndarray'>
% [[900.         900.        ]
%  [800.         800.        ]
%  [700.         700.        ]
%  [600.         650.38897339]
%  [547.71572648 550.38897339]
%  [447.71572648 450.38897339]
%  [347.71572648 350.38897339]
%  [247.71572648 250.38897339]
%  [147.71572648 150.38897339]
%  [ 78.28813535  89.28152018]
%  [ 78.45630624  88.98213325]]
% Total Distance: [1586.04911356]
% GWO Best Fit: [-121.00762186]
% GWO Time Elapsed:  88.75591872999985