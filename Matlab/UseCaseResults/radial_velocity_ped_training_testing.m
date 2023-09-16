%%                      VALIDATION
%% Validation set - 70%
clear all;
clc;

% TESTING
GTA_ideal_test=[89.7952 82.8238 78.1343];
GTA_ideal_x_test=[0.92 1.92 2.97];
% Training
GTA_ideal_train=[90.2921 83.1017 78.6196];
GTA_ideal_x_train=[0.92 1.92 2.93];



% TESTING
GTA_vel_test=[76.6790 67.6892 62.2399];
GTA_vel_x_test=[1 2 3];
% Training
GTA_vel_train=[77.5468 69.0546 63.8644];
GTA_vel_x_train=[1 2 3];


% TESTING
GTA_zero_test=[75.7888 66.9071 61.5934];
GTA_zero_x_test=[1.1 2.1 3.1];
% Training
GTA_zero_train=[76.9261 68.0309 62.8254];
GTA_zero_x_train=[1.1 2.1 3.1];

%IM=GTA_ideal_test-GTA_zero_test
%IM=GTA_ideal_train-GTA_zero_train

figure
% plot(GTA_ideal_x_train,GTA_ideal_train,"o",Color="#0072BD",MarkerSize=15, LineWidth=7)
hold on 
plot(GTA_ideal_x_test,GTA_ideal_test,".",Color="#0072BD",MarkerSize=70, LineWidth=4)
hold on 
% plot(GTA_vel_x_train,GTA_vel_train,"o",Color="#7E2F8E",MarkerSize=15, LineWidth=7)
hold on 
% plot(GTA_zero_x_train,GTA_zero_train,"o",Color="#A2142F",MarkerSize=15, LineWidth=7)
hold on 
plot(GTA_zero_x_test,GTA_zero_test,".",Color="#A2142F",MarkerSize=70, LineWidth=4)

%errorbar(GTA_vel_x,GTA_vel,GTA_vel_errneg,GTA_vel_errpos,'.',Color="m",MarkerSize=70,LineWidth=2)
hold on 
%errorbar(GTA_zero_x,GTA_zero,GTA_zero_errneg,GTA_zero_errpos,'.',Color="#FF8800",MarkerSize=70,LineWidth=2)
grid on
ylim([60 100])
xlim([0.5,3.5])
yticks(0:5:100);
ylabel("AP@R40 0.5 0.5 0.5")
set(gca,'XTick',0:1:3)
set(gca,'XTickLabel',{'','Easy','Moderate','Hard'})
lgd=legend('Point cloud 1B:(x,y,z,(Bool)Is\_Ped)','Point cloud 5:(x,y,z)', Location='northeast')
lgd.FontSize = 30;
box on
set(gca,'FontSize',30)
set(gcf,'color','w');
set(gca,'color','w');
