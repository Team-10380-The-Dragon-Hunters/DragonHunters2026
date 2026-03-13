import rev
from typing import TypeAlias
from pathplannerlib.config import RobotConfig
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
from commands2.button import CommandXboxController, Trigger


Direction: TypeAlias = bool


REVMotorType   = rev.SparkBase.MotorType
REVResetMode   = rev.ResetMode
REVPersistMode = rev.PersistMode
REVIdleMode    = rev.SparkBaseConfig.IdleMode
config = RobotConfig.fromGUISettings()

BRUSHED      : REVMotorType   = REVMotorType.kBrushed
BRUSHLESS    : REVMotorType   = REVMotorType.kBrushless

SAFE_RESET   : REVResetMode   = REVResetMode.kResetSafeParameters
NO_SAFE_RESET: REVResetMode   = REVResetMode.kNoResetSafeParameters

PERSIST      : REVPersistMode = REVPersistMode.kPersistParameters
NO_PERSIST   : REVPersistMode = REVPersistMode.kNoPersistParameters

COAST        : REVIdleMode    = REVIdleMode.kCoast
BRAKE        : REVIdleMode    = REVIdleMode.kBrake

FORWARD      : Direction      = False
REVERSE      : Direction      = True
