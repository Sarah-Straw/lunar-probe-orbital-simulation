
#
# Imports 
#
import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt


MyInput = ''
while MyInput != 'q':
    MyInput = input('Enter a choice, "1", "2" or "q" to quit: ')
    print('You entered the choice: ',MyInput)
    
    if MyInput == '1':
        print('You have chosen part (1): simulation of a lunar orbit')
        
        #
        # Function definitions
        #
        
        def derivatives(time,state,Me,Mm,G):
            
            
            """
            Function to compute the derivatives for the orbit of a body about the origin
            ----------
            time : independent variable, floating point, not used. (s)
            state : Tuple of floats containing (xm, ym, vmx, vmy).
            Me : mass of the earth (kg)
            Mm : mass of the moon (kg)
            G : gravitational constant
            -------
            Returns: tuple of derivatives (dxm/dt,dym/dt,dvmx/dt,dvmy/dt).
            """
            
            xm,ym,vmx,vmy = state # state of dependent variables at some time t
            f1 = vmx # dxm/dt = vmx
            f2 = vmy # dym/dt = vmy
            rm = np.sqrt(xm*xm+ym*ym) #components of radius of orbit
            f3 = -Me*G*xm/rm**3 # dvmx/dt = f3
            f4 = -Me*G*ym/rm**3 # dvmy/dt = f4
            return (f1,f2,f3,f4)
        
        #==========================================================================================
        # Main code
        #
        # Setting initial conditions
        #
        G = (6.6743e-11) # m**3 kg**−1 s**−2, gravitational constant
        Me = 5.972e24 # kg, mass of earth
        Mm = 7.3e22 # kg, mass of moon
        rm= 3.844e8 # m, radius of the moon's orbit around the earth
        xm0 = rm # m, initially the moon sits on the postive x-axis
        ym0 = 0.0 # m, initial y value of the moon's position is 0
        vmx0 = 0.0 # m/s, initially moon is at max x value so dmx/dt = 0
        vmy0 = np.sqrt(G*Me/rm) # m/s, initial velocity is found by equating centripetal force to graviational force acting on the moon
        t_min = 0.0 # s, initial time
        t_max = 3e6 # s, final time for slightly over one full orbit
        teval = np.linspace(t_min,t_max,num=10000)
        
        
        t_interval = (t_min, t_max) # time interval tuple
        
        initial_state = (xm0,ym0,vmx0,vmy0) # in same order as the state tuple
      
        results = si.solve_ivp(derivatives, t_interval, initial_state, t_eval=teval, args=(Me, Mm, G), atol=1e-4, rtol=1e-4)
        
        #
        # Plotting the results
        #
        ax=plt.axes()    # This creates some axes
        
        ax.set_xlabel("x coordinate (m)") # Must label axes (with
        ax.set_ylabel("y coordinate (m)") # units) and give
        ax.set_title("Orbit of moon around earth") # plot title.
        ax.set_aspect(1) # set the aspect ratio to 1 i.e. x and y axes are scaled equally.
        
        x_values = results.y[0] # extracting the array of x_m values from results
        y_values = results.y[1] # extracting the array of y_m values from results
        ax.plot(x_values,y_values, label='Moon', color = '#7c7aff') # Make the plot
        plt.legend(loc='upper right', fontsize='large')
        plt.show()
        
    elif MyInput == '2':
        print('You have chosen part (2): earth-moon-probe system')
        
        # Function Definitions 

        def derivatives(time,state_p_m,Me,Mm,G):
            
            
            """
            Function to compute the derivatives for a projectile problem
            in 2-D with drag.
            ----------
            time : independent variable, floating point, not used. (s)
            state_p_m : Tuple of floats containing (xm, ym, vmx, vmy, xp, yp, vpx, vpy)
            Me : mass of the earth (kg)
            Mm : mass of the moon (kg)
            G : gravitational constant (m**3/(kg**2)*(x**2))
            -------
            Returns: tuple of derivatives (dxm/dt, dym/dt, dvmx/dt, dvmy/dt, dxp/dt, dyp/dt, dvpx/dt, dvpy/dt).
            """
            
            xm, ym, vmx, vmy, xp, yp, vpx, vpy = state_p_m # state of dependent variables at some time t>0
            
            # Derivatives of moon's motion
            
            rm = np.sqrt(xm*xm+ym*ym) #components of radius of orbit
            
            f1 = vmx # dxm/dt = vmx
            f2 = vmy # dym/dt = vmy
            f3 = -Me*G*xm/rm**3 # dvmx/dt = f3
            f4 = -Me*G*ym/rm**3 # dvmy/dt = f4
            
            # Derivatives of the probe's motion
            
            ypm = yp-ym # m, definition of y component of rpm positional vector
            xpm = xp-xm # m, definition of x component of rp positional vector
            rpm = np.sqrt(xpm*xpm+ypm*ypm) # radius of orbit from probe around the moon from its components
            rp = np.sqrt(xp*xp+yp*yp) # distance from probe to earth from components of rm and rpm
            
            f5 = vpx # dxp/dt = vpx
            f6 = vpy # dyp/dt = vpy
            f7 = -Me*G*xp/rp**3 - Mm*G*xpm/rpm**3 # dvpx/dt = f7
            f8 = -Me*G*yp/rp**3 - Mm*G*ypm/rpm**3 # dvpy/dt = f8
            
            return (f1, f2, f3, f4, f5, f6, f7, f8)
            
        #===================================================================================================       

        # Main Code


        # Setting initial conditions

        G = (6.6743e-11) # m**3 kg**−1 s**−2, gravitational constant
        Me = 5.972e24 # kg, mass of earth
        Mm = 7.3e22 # kg, mass of moon

        # Moon initial conditions:

        rm= 3.844e8 # m, radius of the moon's orbit around the earth
        xm0 = rm # m, initially the moon sits on the postive x-axis
        ym0 = 0.0 # m, initial y value of the moon's position is 0
        vmx0 = 0.0 # m/s, initially moon is at max x value so dmx/dt = 0
        vmy0 = np.sqrt(G*Me/rm) # m/s, initial velocity is found by equating centripetal force to graviational force acting on the moon

        # Probe initial conditions in Moon's frame of reference:

        rpm = 8.0e6 # m, radius of the probe's orbit around the moon
        xpm0 = rpm # m, initial distance from probe to moon
        ypm0 = 0.0 # m, initially probe sits along x-axis to moon so y0=0
        vpmx0 = 0.0 # m/s, initial x component of velocity of probe relative to the moon
        vpmy0 = np.sqrt(G*Mm/abs(rpm)) # m/s, initial velocity along y axis

        # Probe initial conditions in Earth's frame of reference:
            
        yp0 = ym0+ypm0 # m, initial y coordinate of probe  
        xp0 = xm0+xpm0 # m, initial x coordinate of probe
        vpx0 = vmx0+vpmx0 # m/s, initial x component of probe's velocity 
        vpy0 = vmy0+vpmy0 # m/s, initial y component of probe's velocity

        t_min = 0.0 # s, initial time
        t_max = 3e6 # s, final time for orbit
        teval = np.linspace(t_min,t_max,num=1000)

        t_interval = (t_min, t_max) # time interval tuple

        initial_state_p_m = (xm0, ym0, vmx0, vmy0, xp0, yp0, vpx0, vpy0) # initial conditions in same order as the state tuple


        # Solving the equations of motion

        results = si.solve_ivp(derivatives, t_interval, initial_state_p_m, t_eval=teval, args=(Me, Mm, G), atol=1e-6, rtol=1e-7)


        # Plotting the results

        ax=plt.axes()    # Creating axes
        ax.set_aspect(1) # set the aspect ratio to 1, scales x and y axes equally as to not distort the appearence of the orbit
        ax.set_xlabel("x coordinate (m)") # x xis label 
        ax.set_ylabel("y coordinate (m)") # y axis label
        ax.set_title("Orbit of probe around moon") # plot title
        
        x_values_m = results.y[0] # extracting the array of x_m values from results
        y_values_m = results.y[1] # extracting the array of y_m values from results
        x_values_p = results.y[4] # extracting the array of x_p values from results
        y_values_p = results.y[5] # extracting the array of y_p values from results
        
        #plt.xlim(0.0,1.2e5) # limiting the y axis to zoom onto a part of the plot
        #plt.ylim(1.0e5,1.6e5) # limmiting the x2 axis to zoom onto a part of the plot
        ax.plot(x_values_m,y_values_m, label='Moon', color = '#7c7aff') # plots 0th row (xm) by 1st row (ym) of the y matrix in results, the matrix of state_p_m variables evaluated at each time value in teva array
        ax.plot(results.y[4],results.y[5], label = 'Probe', color = '#FF7a90') # plots 4th row (xp) by 1st row (yp) of the y matrix in results
        ax.legend(loc='upper right')
        plt.show()

        
    elif MyInput != 'q':
        print('This is not a valid choice')
print('You have chosen to finish - goodbye.')







