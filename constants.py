import rev
from typing import TypeAlias
from pathplannerlib.config import RobotConfig


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