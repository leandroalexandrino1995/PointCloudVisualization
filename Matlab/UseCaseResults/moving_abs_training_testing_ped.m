clear all;
clc;

% TESTING
ideal_test=[87.6628, 79.2689, 73.1826];
moving_test=[75.5249, 66.5062, 60.4913];
vel_abs_test=[75.4104, 66.5923, 60.9111];
zero_test=[71.6400, 61.4279, 55.8504];
IM=ideal_test-zero_test

% Training
ideal_train=[89.7197, 82.7302, 78.1555];
moving_train=[78.7497, 70.3513, 64.9339];
vel_abs_train=[79.0313, 70.5373, 65.2496];
zero_train=[75.6502, 66.3073, 60.7967];
IM_vel=vel_abs_test-zero_test
IM_moving=moving_test-zero_test



figure
% plot([0.8,1.8,2.8],ideal_train,"o",Color="#0072BD",MarkerSize=15, LineWidth=7)
plot([0.8,1.8,2.8],ideal_test,".",Color="#0072BD",MarkerSize=70, LineWidth=4)
hold on
% plot([1.1,2.1,3.1],zero_train,"o",Color="#A2142F",MarkerSize=15, LineWidth=7)
plot([1.1,2.1,3.1],zero_test,".",Color="#A2142F",MarkerSize=70, LineWidth=4)
ylim([40 100])
xlim([0.5,3.5])
yticks(0:5:100);
ylabel("AP@R40 0.7 0.7 0.7")
set(gca,'XTick',0:1:3)
set(gca,'XTickLabel',{'','Easy','Moderate','Hard'})
lgd=legend('Point cloud 1B:(x,y,z,(Bool)Is\_Ped)','Point cloud 5:(x,y,z)', Location='northeast')
lgd.FontSize = 30;
box on
grid on
set(gca,'FontSize',30)
set(gcf,'color','w');
set(gca,'color','w');