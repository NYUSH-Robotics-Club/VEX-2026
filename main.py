# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       T34                                                          #
# 	Created:      10/30/2025, 1:34:37 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
brain = Brain()
Deliver_left=Motor(Ports.PORT17, GearSetting.RATIO_18_1, True)
Deliver_right=Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
Jiaolun=Motor(Ports.PORT15, GearSetting.RATIO_18_1, True)
Store=Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
Upsend=Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
Enemy_Store=Motor(Ports.PORT3, GearSetting.RATIO_36_1, False)
intake=Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
middile=Motor(Ports.PORT18, GearSetting.RATIO_18_1, False)
timer=Timer()
CD1=[0,False]
CD2=[0,False]
pushtime=0
controller_1=Controller()
L1=controller_1.buttonL1
L2=controller_1.buttonL2
R1=controller_1.buttonR1
R2=controller_1.buttonR2
LFW=Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
LMW=Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
LBW=Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
RFW=Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
RMW=Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
RBW=Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
colorsensor=Optical(Ports.PORT14)


def SET_MOTOR(Motor,Stop):
    Motor.set_max_torque(100, PERCENT)
    Motor.set_stopping(Stop)
    Motor.set_velocity(100, PERCENT)

def originalize():
    timer.clear()
    SET_MOTOR(Deliver_left,COAST)
    SET_MOTOR(Deliver_right,HOLD)
    SET_MOTOR(Jiaolun,HOLD)
    SET_MOTOR(Store,HOLD)
    SET_MOTOR(Upsend,HOLD)
    SET_MOTOR(Enemy_Store,HOLD)
    SET_MOTOR(intake,HOLD)
    SET_MOTOR(middile,HOLD)
    SET_MOTOR(LFW,COAST)
    SET_MOTOR(LMW,BRAKE)
    SET_MOTOR(LBW,COAST)
    SET_MOTOR(RFW,COAST)
    SET_MOTOR(RMW,BRAKE)
    SET_MOTOR(RBW,COAST)
    global Leftspeed,Rightspeed,TotalSpeed
    Leftspeed=0
    Rightspeed=0
    TotalSpeed=0

def chassis_movement(Leftspeed,Rightspeed):
    LFW.set_velocity(Leftspeed,PERCENT)
    LMW.set_velocity(Leftspeed,PERCENT)
    LBW.set_velocity(Leftspeed,PERCENT)
    RFW.set_velocity(Rightspeed,PERCENT)
    RMW.set_velocity(Rightspeed,PERCENT)
    RBW.set_velocity(Rightspeed,PERCENT)
    LFW.spin(FORWARD)
    LMW.spin(FORWARD)
    LBW.spin(FORWARD)
    RFW.spin(FORWARD)
    RMW.spin(FORWARD)
    RBW.spin(FORWARD)
    CD1=[0,False]
    


def ballcontroll():
    # ball control
        if R1.pressing():#上吐
            intake.set_velocity(100,PERCENT)
            Upsend.set_velocity(100,PERCENT)
            Store.set_velocity(100,PERCENT)
            Deliver_left.set_velocity(100,PERCENT)
            Deliver_right.set_velocity(100,PERCENT)
            intake.spin(FORWARD)
            middile.spin(FORWARD)
            Enemy_Store.spin(FORWARD)
            Deliver_left.spin(FORWARD)
            Deliver_right.spin(FORWARD)
            Upsend.set_velocity(40,PERCENT)
            Upsend.spin(FORWARD)
            Jiaolun.spin(FORWARD)
            Store.spin(FORWARD)
        elif R2.pressing():#下吐
            intake.set_velocity(100,PERCENT)
            Upsend.set_velocity(50,PERCENT)
            Store.set_velocity(100,PERCENT)
            Deliver_left.set_velocity(100,PERCENT)
            Deliver_right.set_velocity(100,PERCENT)
            intake.spin(FORWARD)
            middile.spin(FORWARD)
            Enemy_Store.spin(FORWARD)
            Deliver_left.spin(REVERSE)
            Deliver_right.spin(REVERSE)
            Upsend.stop()
            Jiaolun.spin(FORWARD)
            Store.spin(FORWARD)
        elif L1.pressing():#存球
            intake.set_velocity(100,PERCENT)
            Upsend.set_velocity(100,PERCENT)
            Store.set_velocity(100,PERCENT)
            Deliver_left.set_velocity(100,PERCENT)
            Deliver_right.set_velocity(100,PERCENT)
            Upsend.set_velocity(100,PERCENT)
            intake.spin(FORWARD)
            middile.spin(FORWARD)
            Enemy_Store.spin(FORWARD)
            Deliver_left.spin(FORWARD)
            Deliver_right.spin(FORWARD)
            Upsend.spin(FORWARD)
            Jiaolun.stop()
            Store.spin(REVERSE)
        elif L2.pressing():#反转
            intake.set_velocity(100,PERCENT)
            Upsend.set_velocity(100,PERCENT)
            Store.set_velocity(100,PERCENT)
            Deliver_left.set_velocity(100,PERCENT)
            Deliver_right.set_velocity(100,PERCENT)
            Upsend.set_velocity(100,PERCENT)
            intake.spin(REVERSE)
            middile.spin(REVERSE)
            Enemy_Store.spin(REVERSE)
            Deliver_left.spin(REVERSE)
            Deliver_right.spin(REVERSE)
            Upsend.spin(REVERSE)
            Jiaolun.stop()
            Store.spin(FORWARD)
        else:  
            intake.stop()
            Enemy_Store.stop()
            Deliver_left.stop()
            Deliver_right.stop()
            Upsend.stop()
            Jiaolun.stop()
            Store.stop()
            middile.stop()
        
        
            
        '''
        elif L2.pressing():#吸球
            intake.set_velocity(100,PERCENT)
            Upsend.set_velocity(90,PERCENT)
            Store.set_velocity(50,PERCENT)
            Deliver_left.set_velocity(20,PERCENT)
            Deliver_right.set_velocity(20,PERCENT)
            Upsend.set_velocity(100,PERCENT)
            intake.spin(FORWARD)
            Enemy_Store.spin(FORWARD)
            Deliver_left.spin(FORWARD)
            Deliver_right.spin(FORWARD)
            Upsend.spin(FORWARD)
            Jiaolun.spin(REVERSE)
            Store.spin(FORWARD)
        '''


def chassiscontroll():
    # chassis control
    global Leftspeed,Rightspeed,TotalSpeed,x,y
    x=controller_1.axis4.position()
    y=controller_1.axis3.position()
    if (y>=15 or y<=-15) :
        if x<-15:
            x=(x+15)/85*80
        elif x>15:
            x=(x-15)/85*80
        else:
            x=0
        if y<0:
            y=(y+15)/85*100
        else:
            y=(y-15)/85*100
        Leftspeed=y+x
        Rightspeed=y-x
    elif x>=15 or x<=-15:
        Leftspeed=x
        Rightspeed=-x
    else:
        if x<-15:
            x=(x+15)#/85*100
        else:
            x=(x-15)#/85*100
        Leftspeed=0
        Rightspeed=0
    if Leftspeed>100:
        Leftspeed=100
    elif Leftspeed<-100:
        Leftspeed=-100
    if Rightspeed>100:
        Rightspeed=100
    elif Rightspeed<-100:
        Rightspeed=-100
    chassis_movement(Leftspeed,Rightspeed)
        



def autonomous():
    originalize()
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here


def user_control():
    originalize()
    global pushtime
    global Mode
    pushtime=0
    Mode=0
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        ballcontroll()
        if controller_1.buttonUp.pressing():
            if pushtime + 1000 < timer.time() and Mode==0:
                controller_1.rumble('.')
                pushtime=timer.time()
                Mode = 1
        if Mode ==1:
            if pushtime+100 >= timer.time():
                chassis_movement(-75,-75)
            elif pushtime+300 >= timer.time():
                chassis_movement(75,75)
            else:
                chassis_movement(0,0)
                Mode = 0
        else:
            chassiscontroll()
        wait(2,MSEC)
        '''
        if controller_1.buttonUp.pressing():
            chassis_movement(-100,-100)
            if pushtime + 1 < timer.time(SECONDS) and Mode==0:
                controller_1.rumble('.')
                pushtime=timer.time(SECONDS)
                Mode = 1
            
            if Mode ==1:
                if pushtime+1 >= timer.time(SECONDS):
                    chassis_movement(-100,-100)
                
                else:
                    chassis_movement(0,0)
                    Mode = 0
'''
        
        
        


        

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()

