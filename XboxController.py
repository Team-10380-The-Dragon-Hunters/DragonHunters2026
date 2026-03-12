import wpilib as wp
from wpilib import Joystick


class XboxController(Joystick):
    """
    Represents a Logitech X3D joystick.

    Provides button mapping methods specific to the Logitech X3D joystick.
    """
    def __init__(self, player: int):
        """
        Initializes the Logitech X3D joystick.

        Args:
            player: The player ID for the joystick (0-5).

        Raises:
            ValueError: If the player ID is not between 0 and 5.
        """
        super().__init__(player)
        if player < 0 and player > 5: raise ValueError("Player value must be between 0 and 5")
        self.player: int = player

    def getAButton(self) -> bool:
        """
        Gets the state of the trigger button.

        Returns:
            True if the trigger is pressed, False otherwise.
        """
        return self.getRawButton(1)

    def getBButton(self) -> bool:
        """
        Gets the state of the thumb side button.

        Returns:
            True if the thumb side button is pressed, False otherwise.
        """
        return self.getRawButton(2)
    def getXButtonPressed(self) -> bool:
        return self.getRawButtonPressed(3)
    def getXButton(self) -> bool:
        """
        Gets the state of the thumb bottom left button.

        Returns:
            True if the thumb bottom left button is pressed, False otherwise.
        """
        return self.getRawButton(3)

    def getYButton(self) -> bool:
        """
        Gets the state of the thumb bottom right button.

        Returns:
            True if the thumb bottom right button is pressed, False otherwise.
        """
        return self.getRawButton(4)

    def start(self) -> bool:
        """
        Gets the state of the thumb top left button.

        Returns:
            True if the thumb top left button is pressed, False otherwise.
        """
        return self.getRawButton(5)

    def back(self) -> bool:
        """
        Gets the state of the thumb top right button.

        Returns:
            True if the thumb top right button is pressed, False otherwise.
        """
        return self.getRawButton(6)

    def mode(self) -> bool:
        """
        Gets the state of the side top left button.

        Returns:
            True if the side top left button is pressed, False otherwise.
        """
        return self.getRawButton(7)

    def home(self) -> bool:
        """
        Gets the state of the side top right button.

        Returns:
            True if the side top right button is pressed, False otherwise.
        """
        return self.getRawButton(8)

    def dpadUp(self) -> bool:
        """
        Gets the state of the side middle left button.

        Returns:
            True if the side middle left button is pressed, False otherwise.
        """
        return self.getRawButton(9)

    def dpadDown(self) -> bool:
        """
        Gets the state of the side middle right button.

        Returns:
            True if the side middle right button is pressed, False otherwise.
        """
        return self.getRawButton(10)

    def dpadLeft(self) -> bool:
        """
        Gets the state of the side bottom left button.

        Returns:
            True if the side bottom left button is pressed, False otherwise.
        """
        return self.getRawButton(11)

    def dpadRight(self) -> bool:
        """
        Gets the state of the side bottom right button.

        Returns:
            True if the side bottom right button is pressed, False otherwise.
        """
        return self.getRawButton(12)
    
    def leftBumper(self) -> bool:
        """
        Gets the state of the throttle axis.

        Returns:
            The value of the throttle axis (-1.0 to 1.0).
        """
        return self.getRawAxis(3)
    
    def rightBumper(self) -> bool:
        """
        Gets the state of the throttle axis.

        Returns:
            The value of the throttle axis (-1.0 to 1.0).
        """
        return self.getRawAxis(3)
    
    def leftThrottle(self) -> float:
        """
        Gets the state of the throttle axis.

        Returns:
            The value of the throttle axis (-1.0 to 1.0).
        """
        return self.getRawAxis(3)

    def rightThrottle(self) -> float:
        """
        Gets the state of the throttle axis.

        Returns:
            The value of the throttle axis (-1.0 to 1.0).
        """
        return self.getRawAxis(3)
    
    def leftJoystickButton(self) -> bool:
        """
        Gets the state of the throttle axis.

        Returns:
            The value of the throttle axis (-1.0 to 1.0).
        """
        return self.getRawAxis(3)
    
    def rightJoystickButton(self) -> bool:
        """
        Gets the state of the throttle axis.

        Returns:
            The value of the throttle axis (-1.0 to 1.0).
        """
        return self.getRawAxis(3)
    
    # joysticks?
    
    def getThrottle(self) -> float:
        """
        Gets the state of the throttle axis.

        Returns:
            The value of the throttle axis (-1.0 to 1.0).
        """
        return self.getRawAxis(3)
    
    def getThrottle(self) -> float:
        """
        Gets the state of the throttle axis.

        Returns:
            The value of the throttle axis (-1.0 to 1.0).
        """
        return self.getRawAxis(3)