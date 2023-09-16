clear all;
clc;

% TESTING
ideal_test=[98.2102, 93.0615, 88.2658];
moving_test=[97.4719, 91.9860, 87.3713];
vel_abs_test=[97.8940, 92.0269, 87.6339];
zero_test=[97.0349 91.5024 87.0416];

% Training
ideal_train=[98.8453, 93.4500, 90.9731];
moving_train=[98.0269, 92.7206, 90.1199];
vel_abs_train=[98.4329, 92.7142, 90.1029];
zero_train=[97.7670, 92.5058, 89.9983];


figure
plot([0.8,1.8,2.8],ideal_test,".",Color="#0072BD",MarkerSize=70, LineWidth=4)
% plot([0.8,1.8,2.8],ideal_train,"o",Color="#0072BD",MarkerSize=15, LineWidth=7)
hold on
% plot([1.1,2.1,3.1],zero_train,"o",Color="#A2142F",MarkerSize=15, LineWidth=7)
plot([1.1,2.1,3.1],zero_test,".",Color="#A2142F",MarkerSize=70, LineWidth=4)
ylim([60 100])
xlim([0.5,3.5])
yticks(0:5:100);
ylabel("AP@R40 0.7 0.7 0.7")
set(gca,'XTick',0:1:3)
set(gca,'XTickLabel',{'','Easy','Moderate','Hard'})
lgd=legend('Point cloud 1A:(x,y,z,(Bool)Is\_Car)','Point cloud 5:(x,y,z)', Location='best')
lgd.FontSize = 30;
box on
grid on
set(gca,'FontSize',30)
set(gcf,'color','w');
set(gca,'color','w');