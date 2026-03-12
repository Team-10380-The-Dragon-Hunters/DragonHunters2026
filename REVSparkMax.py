from rev        import SparkMax, SparkLowLevel       as REVSparkMax
from rev         import SparkMaxConfig as REVSparkMaxConfig
from constants import *
from typing      import Optional


class REVSparkMax(REVSparkMax):
    """Wrapper class for a REV Spark MAX motor controller.

    This class provides additional functionality and management for REV Spark MAX motor controllers.
    It stores motor configuration details and provides convenient methods for setting and retrieving them.
    """
    def __init__(self, can_id: int, motor_type: REVMotorType) -> None:
        """Initialize a new REVSparkMax object.

        This constructor initializes the REVSparkMax object with the given CAN ID and motor type.
        It also sets default values for other motor parameters.
        """
        super().__init__(can_id, motor_type)

        self.can_id     : int             = can_id

        self.motor_type : REVMotorType    = motor_type
        self.idle_mode  : REVIdleMode     = BRAKE
        self.leader_id  : Optional[int]   = None
        self.direction  : Direction       = FORWARD

        self.is_follower: bool            = False
        self.is_inverted: bool            = False

    # Setters and Getters
    def getID(self) -> int:
        """Get the CAN ID of the Spark MAX.

        This method returns the CAN ID that was used to initialize the Spark MAX object.
        It provides a convenient way to access the CAN ID.
        """
        return self.can_id

    def getMotorType(self) -> REVMotorType:
        """Get the motor type of the Spark MAX.

        This method returns the motor type that was used to initialize the Spark MAX object.
        It provides a convenient way to access the motor type.
        """
        return self.motor_type

    def setIdleMode(self, idle_mode: REVIdleMode) -> None:
        """Set the idle mode of the Spark MAX.

        This method sets the idle mode of the motor, which determines its behavior when no input is applied.
        It allows setting the idle mode to either BRAKE or COAST.
        """
        self.idle_mode = idle_mode

    def getIdleMode(self) -> REVIdleMode:
        """Get the idle mode of the Spark MAX.

        This method returns the current idle mode of the motor.
        It provides a way to check the configured idle mode.
        """
        return self.idle_mode

    def setLeaderID(self, leader_id: Optional[int]) -> None:
        """Set the leader ID for follower mode.

        This method sets the CAN ID of the leader motor for follower mode.
        If leader_id is None, follower mode is disabled.
        """
        if leader_id <= 1: raise ValueError("Leader ID must be greater than 1")
        self.leader_id = leader_id
        self.is_follower = leader_id is not None

    def getLeaderID(self) -> Optional[int]:
        """Get the leader ID for follower mode.

        This method returns the CAN ID of the leader motor, or None if not in follower mode.
        It provides a way to check the current leader ID.
        """
        return self.leader_id

    def setDirection(self, direction: Direction) -> None:
        """Set the rotation direction of the Spark MAX.

        This method sets the rotation direction of the motor.
        It updates the is_inverted flag based on the provided direction.
        """
        self.is_inverted = direction != FORWARD
        self.direction = direction
    
    def getDirection(self) -> Direction:
        """Get the rotation direction of the Spark MAX.

        This method returns the current rotation direction of the motor.
        It provides a way to check the configured direction.
        """
        return self.direction

    def getIsFollower(self) -> bool:
        """Get the follower status of the Spark MAX.

        This method returns True if the motor is in follower mode, False otherwise.
        It provides a way to check if the motor is following another.
        """
        return self.is_follower

    def getIsInverted(self) -> bool:
        """Get the inverted status of the Spark MAX.

        This method returns True if the motor is inverted, False otherwise.
        It provides a way to check the motor's inversion setting.
        """
        return self.is_inverted

    # REVSparkMax Config
    def setConfig(self) -> None:
        """Set the configuration of the Spark MAX.

        This method sets the configuration of the motor, including inversion, idle mode, and follower mode.
        It uses the provided reset and persist modes to determine how the configuration is applied.
        """
        self.configure(self.getConfig())

    def getConfig(self) -> REVSparkMaxConfig:
        """Get the current configuration of the Spark MAX.

        This method retrieves the current configuration of the motor, including inversion, idle mode, and follower settings.
        It returns a REVSparkMaxConfig object containing the current settings.
        """
        sparkmax_config: REVSparkMaxConfig = REVSparkMaxConfig()

        sparkmax_config = sparkmax_config.inverted(self.getIsInverted())
        sparkmax_config = sparkmax_config.setIdleMode(self.getIdleMode())
        if not self.getIsFollower(): sparkmax_config = sparkmax_config.disableFollowerMode()
        else: sparkmax_config = sparkmax_config.follow(self.getLeaderID())

        return sparkmax_config

    def resetConfig(self) -> None:
        """Reset the configuration of the Spark MAX to default values.

        This method resets the motor's configuration to its default state, including setting the idle mode to BRAKE,
        disabling follower mode, and setting the rotation direction to FORWARD.
        """
        self.setIdleMode(BRAKE)
        self.setLeaderID(None)
        self.setDirection(FORWARD)
