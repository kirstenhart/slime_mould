%% Amanda Dings
% 12/12/2020

clc; clear variables; close all;
%% 

x = 0:20;
sma_iter = [11 12 11.67 14 14 10.67 13.33 12.33 14.33 11.67 16 10 9.67 12.33 12 19 15.67 12.67 11.67 16 15];
gwo_iter = [10.50 11.33 11.17 14 12.50 10.33 12.17 11 13 11.17 15.50 9.67 10.33 11.67 12.50 17 16.17 11.83 10.83 15.33 14.83];

f = figure('WindowStyle','docked');
plot(x,sma_iter,'r','LineWidth',3); hold on
plot(x,gwo_iter,'b','LineWidth',3)
legend('SMA','GWO');
xlabel('Number of Obstacles');
ylabel('Number of Iterations');
a = gca;
a.FontSize=18;
f.Color = 'White';

close all; clear f; clear a;
sma_path_length = [1191.06 1189.89 1183.87 1288.26 1194.18 1184.94 1191.77 1189.77 1207.73 1184.00 1244.91 1183.34 1182.26 1182.13 1191.07 1227.38 1196.16 1186.50 1186.76 1327.14 1332.03];
gwo_path_length = [1572.29 1580.40 1570.72 1698.98 1578.88 1576.98 1590.96 1569.52 1602.70 1575.93 1703.06 1571.08 1582.10 1576.06 1579.55 1623.10 1624.79 1580.13 1573.26 1764.37 1800.57];
f = figure('WindowStyle','docked');
plot(x,sma_path_length,'r','LineWidth',3); hold on
plot(x,gwo_path_length,'b','LineWidth',3)
legend('SMA','GWO');
xlabel('Number of Obstacles');
ylabel('Path Length (m)');
a = gca;
a.FontSize=18;
f.Color = 'White';


close all; clear f; clear a;
sma_time_elapsed = [0.344 0.327 0.292 0.300 0.308 0.304 0.337 0.295 0.347 0.305 0.330 0.305 0.288 0.292 0.323 0.293 0.294 0.299 0.300 0.307 0.298];
gwo_time_elapsed = [0.325 0.315 0.294 0.292 0.297 0.287 0.317 0.305 0.322 0.296 0.312 0.296 0.285 0.286 0.304 0.284 0.297 0.293 0.301 0.292 0.309];
f = figure('WindowStyle','docked');
plot(x,sma_time_elapsed,'r','LineWidth',3); hold on
plot(x,gwo_time_elapsed,'b','LineWidth',3)
legend('SMA','GWO');
xlabel('Number of Obstacles');
ylabel('Time elapsed (s)');
a = gca;
a.FontSize=18;
f.Color = 'White';
