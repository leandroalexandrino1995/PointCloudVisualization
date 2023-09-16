%% 
clear all;
clc;
close all;

%% Configuration of source file
% Plot intensity -> True -> use Point cloud intensity values
% Plot intensity -> False -> Intensity set to 0
PlotIntensity = true;

location='D:\bintoply\000725.ply'
ptCloud = pcread(location);

%% Prepare colors
if(~PlotIntensity)
    % Zero intensity
    ZeroIntensity = zeros(ptCloud.Count, 1);
    ptCloud_colored = pointCloud(cat(3, ptCloud.Location(:,1), ptCloud.Location(:,2), ptCloud.Location(:,3)), 'Intensity', ZeroIntensity);
else
    % Use existent intensity value
    ptCloud_colored = pointCloud(cat(3, ptCloud.Location(:,1), ptCloud.Location(:,2), ptCloud.Location(:,3)), 'Intensity', ptCloud.Intensity);
end
ax1=pcshow(ptCloud_colored, 'MarkerSize', 1);

%% Colorbar
cb = colorbar();
cb.FontSize=15
set(gcf, 'Units', 'Normalized', 'OuterPosition', [0 0 1 1]);
minLimit = min(ptCloud.Intensity(:));
maxLimit = max(ptCloud.Intensity(:));
% Axis, changed manually
caxis([-8 8]);

set(gca, 'XColor', [0.15 0.15 0.15], 'YColor', [0.15 0.15 0.15], 'ZColor', [0.15 0.15 0.15])
set(gcf,'color','w');
set(gca,'color','w');
grid on;
set(gca,'xticklabel',{[]})
grid on;
set(gca,'yticklabel',{[]})
grid on;
set(gca,'zticklabel',{[]})

set(gca,'ZGrid','off');
set(ax1,'TickLength',[0 0])
ax1.YAxis.Visible = 'off'; % remove y-axis
ax1.XAxis.Visible = 'off'; % remove y-axis
ax1.ZAxis.Visible = 'off'; % remove y-axis

cb.Color = 'black';
cb.Title.String = {'\bfPoint cloud: (x,y,z,(Float)Radial\_Velocity)','Radial velocity(m/s)'};
set(gcf, 'Toolbar', 'none');
view([-90 30])
cb.TickLabels = compose('{%.1f}',cb.Ticks)

load velocity_colors.mat
colormap(radial_cmap)
    
% load abs_velocity_colors.mat
% colormap(abs_velocity_cmap)
    
%colormap('default')
colormapeditor
%fullscreen()
%velocity_cmap = get(gca,'Colormap');
%radial_cmap = colormap(gca);



