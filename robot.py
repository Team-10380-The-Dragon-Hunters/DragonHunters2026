#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import typing
from constants import *
from phoenix6 import CANBus, controls, hardware
from robotcontainer import RobotContainer
from XboxController import XboxController
from pathplannerlib.auto import AutoBuilder
from pathplannerlib.controller import PPHolonomicDriveController
from pathplannerlib.config import RobotConfig, PIDConstants
from wpilib import DriverStation
import limelight
import limelightresults
import json
import time

from phoenix6 import HootAutoReplay


class MyRobot(commands2.TimedCommandRobot):
    """
    Command v2 robots are encouraged to inherit from TimedCommandRobot, which
    has an implementation of robotPeriodic which runs the scheduler for you
    """

    autonomousCommand: typing.Optional[commands2.Command] = None

    def robotInit(self) -> None:
        """
        This function is run when the robot is first started up and should be used for any
        initialization code.
        """
        
        self.flywheelOne = hardware.TalonFX(16, CANBus("rio"))
        self.flywheelTwo = hardware.TalonFX(17, CANBus("rio"))
        self.IMU = hardware.Pigeon2(23, CANBus("rio"))
        #rev.SparkMax(deviceID: SupportsInt | SupportsIndex, type: rev._rev.SparkLowLevel.MotorType)
        # CAN ID
        self.intakeArm = rev.SparkMax(18, BRUSHLESS)
        self.intakeArmFollower = rev.SparkMax(19, BRUSHLESS)
        self.intakePower = rev.SparkMax(20,BRUSHLESS)
        self.transferMotor = rev.SparkMax(21,BRUSHLESS)
        self.conveyorMotor = rev.SparkMax(22, BRUSHLESS)
        self.limelight = limelight.limelight("limelight")
        
        # Drive Motors
        #self.intakeArm           : REVSparkMax = self.addDriveMotor(REVSparkMax(intakeArm, BRUSHLESS))
        #self.intakeArmFollower   : REVSparkMax = self.addDriveMotor(REVSparkMax(intakeArmFollower, BRUSHLESS))
        #self.intakePower         : REVSparkMax = self.addDriveMotor(REVSparkMax(intakePower, BRUSHLESS))
        #self.transferMotor       : REVSparkMax = self.addDriveMotor(REVSparkMax(transferMotor, BRUSHLESS))
        #self.conveyorMotor       : REVSparkMax = self.addDriveMotor(REVSparkMax(conveyorMotor, BRUSHLESS))
        
        # Follower Motors
        #self.addFollowerMotor(self.intakeArm, self.intakeArmFollower)
        
        # Reversed Motors
        #self.addReversedMotor(self.left_motor)

        #Controller
        self.driverController: XboxController = XboxController(0)
        self.toolController: XboxController = XboxController(1)
        
        #2 servos
        self.hoodServoOne = wpilib.Servo(8)
        self.hoodServoTwo = wpilib.Servo(9)
        self.angle = 0
        # Instantiate our RobotContainer.  This will perform all our button bindings, and put our
        # autonomous chooser on the dashboard.
        self.container = RobotContainer()
        self.IMU.reset()
        self.targetRPM = 4500
        self.targetRPS = self.targetRPM / 60


        # log and replay timestamp and joystick data
        self._time_and_joystick_replay = (
            HootAutoReplay()
            .with_timestamp_replay()
            .with_joystick_replay()
        )

    def robotPeriodic(self) -> None:
        """This function is called every 20 ms, no matter the mode. Use this for items like diagnostics
        that you want ran during disabled, autonomous, teleoperated and test.

        This runs after the mode specific periodic functions, but before LiveWindow and
        SmartDashboard integrated updating."""

        self._time_and_joystick_replay.update()
        # Runs the Scheduler.  This is responsible for polling buttons, adding newly-scheduled
        # commands, running already-scheduled commands, removing finished or interrupted commands,
        # and running subsystem periodic() methods.  This must be called from the robot's periodic
        # block in order for anything in the Command-based framework to work.
        commands2.CommandScheduler.getInstance().run()

    def disabledInit(self) -> None:
        """This function is called once each time the robot enters Disabled mode."""
        pass

    def disabledPeriodic(self) -> None:
        """This function is called periodically when disabled"""
        pass

    def autonomousInit(self) -> None:
        """This autonomous runs the autonomous command selected by your RobotContainer class."""
        # Another option that allows you to specify the default auto by its name
      #  self.autoChooser = AutoBuilder.buildAutoChooser("topAuto")
      #  self.autonomousCommand = self.container.getAutonomousCommand()
    #    SmartDashboard.putData("Auto Chooser", self.autoChooser)

        if self.autonomousCommand:
            commands2.CommandScheduler.getInstance().schedule(self.autonomousCommand)

    def autonomousPeriodic(self) -> None:
        """This function is called periodically during autonomous"""
        pass

    def teleopInit(self) -> None:
        # This makes sure that the autonomous stops running when
        # teleop starts running. If you want the autonomous to
        # continue until interrupted by another command, remove
        # this line or comment it out.
        if self.autonomousCommand:
            commands2.CommandScheduler.getInstance().cancel(self.autonomousCommand)

    def teleopPeriodic(self) -> None:
        """This function is called periodically during operator control"""
        #intake code
        if self.toolController.rightThrottle > 0: #self.driverController.getYButton(): bmmmmmmm TRIGGERS!!!!!!!!!!!!
            self.intakeArm.set(.25 * self.toolController.rightThrottle()) #ADD SOFTWARE LIMITS OR DEATH BE UPON YE
            self.intakeArmFollower.set(.25 * self.toolController.rightThrottle()) 
            #makes intake go in at half speed
        elif self.toolController.leftThrottle() > 0:#self.driverController.getAButton():
            self.intakeArm.set(-.25 * self.toolController.leftThrottle()) #ADD SOFTWARE LIMITS OR DEATH BE UPON YE
            self.intakeArmFollower.set(-.25 * self.toolController.leftThrottle())
            #makes intake go out at half speed
        else:
            self.intakeArm.set(0)
            self.intakeArmFollower.set(0)
            #sets intake power to 0 when nothing is pressed

        if self.toolController.rightBumper():#self.driverController.rightBumper():
            self.intakePower.set(-.5)
            #makes the intake go forward
        elif self.toolController.leftBumper():#self.driverController.leftBumper():
            self.intakePower.set(.5)
            #makes intake go backward
        else:
            self.intakePower.set(0)
            #stops the intake 
        #flywheel code
        #probably some weird limelight stuff
        self.flywheelOne.set(1 * self.toolController.rightThrottle())
        self.flywheelTwo.set(1 * self.toolController.rightThrottle())
        if self.toolController.getYButton():
            self.flywheelOne.set_control(controls.VelocityVoltage(self.targetRPS))
            self.flywheelTwo.set_control(controls.VelocityVoltage(self.targetRPS))
        else:
            self.flywheelOne.set(0)
            self.flywheelTwo.set(0)
        #conveyor code
        if self.toolController.getAButton():
            self.conveyorMotor.set(-.5)
            self.transferMotor.set(.5)
        if self.toolController.getBButton():
            self.conveyorMotor.set(0)
            self.transferMotor.set(0)

        # Servos thats crazy
        self.hoodServoOne.setAngle(self.angle)
        self.hoodServoOne.setAngle(self.angle)
        if self.toolController.dpadUp():
            self.angle += 2
        elif self.toolController.dpadDown():
            self.angle -= 2

    def testInit(self) -> None:
        # Cancels all running commands at the start of test mode
        #commands2.CommandScheduler.getInstance().cancelAll()
        pass
    
