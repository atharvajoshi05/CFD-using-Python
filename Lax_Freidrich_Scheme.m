clear;
nx=500; % no. of points, try changing this no. from 41 to 81
nt=500;  % no. of timesteps
dt =0.025; %amount of time each time step covers
c=1;
sigma = 1
dx = 2/(nx-1);

%dt = sigma * dx  %For using CFL number for better accuaracy

%Establishing initial conditions

Nfront = round(nx/2);  %wave front, intermediate point from which u=0

for i = 1:(nx+1)
    if i<Nfront
        u(i,1)=1.;    
    else
        u(i,1)=0.;
    end
    x(i) = (i-1)*dx; % define vector x, for space discretization
end

% Boundary Conditions,value the 'u' function takes at the boundaries at any
% time

for k = 1:(nt+1)
    u(1,k)=1.;
    u(nx+1,k)=0.;
    t(k)=(k-1)*dt; %define vector t, for time discretization   
end

%Applying the Lax-Method

for k = 1:nt  %time loop
    for i = 2:nx %space loop
        u(i,k+1) = 0.5*(u(i+1,k) + u(i-1,k)) - (sigma/2)*(u(i+1,k)- u(i-1,k));
    end
end

%PLotting the wave at different time steps
plot(x,u(:,1),'-b',x,u(:,round(nt/10)),'--g',x,u(:,round(nt/3)),':b',x,u(:,nt),'-r')
xlabel('X')
ylabel('Amplitude(X)')

%blue line is the initial timestep
%green and dotted blue lines are the further timesteps
%red is the final time step

%NOTE: The solution blows up for sigma>1, hence the Lax-Friedrich's Scheme
%is stable for only sigma<=1

