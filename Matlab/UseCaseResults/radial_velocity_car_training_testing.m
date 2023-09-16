clear all;
clc;

% TESTING
GTA_ideal_test=[98.5546 93.2475 90.67];
GTA_ideal_x_test=[0.88 1.92 2.97];
% Training
 GTA_ideal_train=[99.1463 96.4706 94.0052];%
 GTA_ideal_x_train=[0.92 1.92 2.93];




GTA_vel_test=[98.0121 92.2971 87.4812];
GTA_vel_x_test=[1 2 3];

 GTA_vel_train=[98.6152 93.3658 93.0458];
 GTA_vel_x_train=[1 2 3];

% 
GTA_zero_test=[97.9304 92.0860 87.7866];
GTA_zero_x_test=[1.1 2.1 3.1];

 GTA_zero_train=[98.0962 93.0856 92.8698];
 GTA_zero_x_train=[1.12 2.1 3.1];

figure
% plot(GTA_ideal_x_train,GTA_ideal_train,"o",Color="#0072BD",MarkerSize=15, LineWidth=7)
hold on 
plot(GTA_ideal_x_test,GTA_ideal_test,".",Color="#0072BD",MarkerSize=70, LineWidth=4)
% hold on 
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
ylabel("AP@R40 0.7 0.7 0.7")
set(gca,'XTick',0:1:3)
set(gca,'XTickLabel',{'','Easy','Moderate','Hard'})
lgd=legend('Point cloud 1A:(x,y,z,(Bool)Is\_Car)','Point cloud 5:(x,y,z)', Location='best')
lgd.FontSize = 30;
box on
set(gca,'FontSize',30)
set(gcf,'color','w');
set(gca,'color','w');
