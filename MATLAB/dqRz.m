function [Q] = dqRz(a)
%% This function computes a rotation �a� along �z� axis in Dual Quaternion form
    Q = transpose([cos(a/2) 0 0 sin(a/2) 0 0 0 0]);
end