%% Amanda Dings
% 12/9/2020
% Adding more obstacles to the field

clc; clear variables; close all;
addpath('./Progress_Bar');
%% Import the field with no obstacles
load('no_obstacles.mat', 'field');

%% Define start and end points
start_loc = [900,900];
end_loc   = [80,90];

%% Define a square obstacle
obs = 500*ones(101);

%% Place obstacles on the field
rng('default')
fields = cell(1,20);
fields(:,:) = {field};
for m = 1:20
    number_of_obstacles = m;
    obstacle_centers    = randi([150, 850], [number_of_obstacles, 2]);
    % make sure obstacles don't occlude
    if m > 1
        for n = 2:number_of_obstacles
            while checkOcclude(obstacle_centers(n,:), obstacle_centers(1:n-1,:))
                % regenerate this one and check again
                obstacle_centers(n,:) = randi([150, 850], [1, 2]);
            end
        end
    end
    % generate the obstacle field
    for i = 1:number_of_obstacles
        obstacle_center = obstacle_centers(i,:);
        index_x = obstacle_center(2)-50: obstacle_center(2)+50;
        index_y = obstacle_center(1)-50: obstacle_center(1)+50;
        fields{m}(index_x, index_y) = fields{m}(index_x, index_y) + obs;
    end
end


%% Preview the resulting field
% Plot the field we end up with
% for m = 1:20
%     figure('WindowStyle','docked')
%     colormap(jet)
%     s=surf(fields{m},'edgealpha',0.0,'facealpha',0.2);%,'facealpha',0.2)
%     title(sprintf('%d obstacles',m));
%     view(2)
%     hold on
%     
%     % Emphasize the starting and ending points
%     plot3(start_loc(1),start_loc(2),field(start_loc(1),start_loc(2)),...
%         '.r','markersize',45)
%     plot3(end_loc(1),end_loc(2),field(end_loc(1),end_loc(2)), ...
%         '.g','markersize',45)
%     
%     % Plot the "walls"
%     plot3([1000 1000],[0 1000], [0,0],'-k','linewidth',5)
%     plot3([0 1000],[1000 1000], [0,0],'-k','linewidth',5)
%     plot3([0 0],[0 1000], [0,0],'-k','linewidth',5)
%     plot3([0 1000],[0 0], [0,0],'-k','linewidth',5)
%     
%     %pause
%     
% end

%% Save the fields
for i = 1:20
    filename = sprintf('field_%d_obs',i);
    field = fields{i};
    save(filename, 'field');
end

%% Subroutines
function result = checkOcclude(current_point, created_points)
result = false;
for i = 1:size(created_points,1)
    if euclid(current_point, created_points(i,:)) < sqrt(100^2+100^2)
        result = true;
        break
    end
end

    function d = euclid(point1, point2)
        dx = point2(1) - point1(1);
        dy = point2(2) - point1(2);
        d = sqrt(dx^2 + dy^2);
    end

end