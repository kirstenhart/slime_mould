%% Amanda Dings
% 12/12/2020

clc; clear variables; close all;
%%
load('field_16_obs.mat','field');

colormap(jet);
surf(field,'EdgeAlpha',0.05,'FaceAlpha',1); hold on;


c = colorbar;
c.Label.String = 'Objective Function Cost';
c.Label.FontSize=18;
a = gca;
a.FontSize = 18;
f = gcf;
f.Color = 'white';
xlabel('X, (m)');
ylabel('Y, (m)');
zlabel('Z, (m)');

start_loc = [900,900];
end_loc   = [80,90];
% Emphasize the starting and ending points
    plot3(start_loc(1),start_loc(2),field(start_loc(1),start_loc(2)),...
        '.r','markersize',45)
    plot3(end_loc(1),end_loc(2),field(end_loc(1),end_loc(2)), ...
        '.g','markersize',45)
    
    
%% 2D field now
field(field<600) = NaN;
field(750:end,750:end) = NaN;
field(500:end,900:end) = NaN;
hold off
surf(field,'EdgeAlpha',1,'FaceAlpha',0); hold on;

% Emphasize the starting and ending points
    plot3(start_loc(1),start_loc(2),0,...
        '.r','markersize',45)
    plot3(end_loc(1),end_loc(2),0, ...
        '.g','markersize',45)
    
        % Plot the "walls"
    plot3([1000 1000],[0 1000], [0,0],'-k','linewidth',5)
    plot3([0 1000],[1000 1000], [0,0],'-k','linewidth',5)
    plot3([0 0],[0 1000], [0,0],'-k','linewidth',5)
    plot3([0 1000],[0 0], [0,0],'-k','linewidth',5)
a = gca;
a.FontSize = 18;
f = gcf;
f.Color = 'white';
xlabel('X, (m)');
ylabel('Y, (m)');
view(2)