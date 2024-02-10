pkg load control;

% creation of a nyquist plot
% G(s) = 1/(s^2 + 2s + 1)
num = [1];
den = [1 2 1];
G = tf(num, den)
nyquist(G)
title('Nyquist plot of G(s) = 1/(s^2 + 2s + 1)')
grid on
hold on
