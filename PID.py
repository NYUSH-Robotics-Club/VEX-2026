import math

class PID:
    """
    PID controller class with optional settling and custom update period.
    """

    def __init__(self, error, kp, ki, kd, starti,
                 settle_error=0, settle_time=0, timeout=0, update_period=10):
        """
        PID constructor with optional settling inputs and update period.
        Starti keeps the I term at 0 until error is less than starti.
        Settling system works like this: The robot is settled when error is less
        than settle_error for a duration of settle_time, or if the function has
        gone on longer than timeout. Otherwise it is not settled.

        :param error: Difference in desired and current position.
        :param kp: Proportional constant.
        :param ki: Integral constant.
        :param kd: Derivative constant.
        :param starti: Maximum error to start integrating.
        :param settle_error: Maximum error to be considered settled.
        :param settle_time: Minimum time to be considered settled.
        :param timeout: Time after which to give up and move on.
        :param update_period: Loop delay time in ms.
        """
        self.error = error
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.starti = starti
        self.settle_error = settle_error
        self.settle_time = settle_time
        self.timeout = timeout
        self.update_period = update_period

        self.accumulated_error = 0
        self.previous_error = 0
        self.time_spent_settled = 0
        self.time_spent_running = 0
        self.output = 0

    def compute(self, error):
        """
        Computes the output power based on the error.
        Typical PID calculation with some optimizations: When the robot crosses
        error=0, the i-term gets reset to 0. And, the robot only accumulates
        i-term when error is less than starti.

        :param error: Difference in desired and current position.
        :return: Output power.
        """
        if abs(error) < self.starti:
            self.accumulated_error += error

        # Checks if the error has crossed 0, and if it has, it eliminates the integral term.
        if (error > 0 and self.previous_error < 0) or (error < 0 and self.previous_error > 0):
            self.accumulated_error = 0

        self.output = self.kp * error + self.ki * self.accumulated_error + self.kd * (error - self.previous_error)
        self.previous_error = error

        if abs(error) < self.settle_error:
            self.time_spent_settled += self.update_period
        else:
            self.time_spent_settled = 0

        self.time_spent_running += self.update_period

        return self.output

    def is_settled(self):
        """
        Computes whether or not the movement has settled.
        The robot is considered settled when error is less than settle_error
        for a duration of settle_time, or if the function has gone on longer
        than timeout. Otherwise it is not settled.

        :return: Whether the movement is settled.
        """
        if self.timeout != 0 and self.time_spent_running > self.timeout:
            return True  # If timeout equals 0, the move will never actually time out.

        if self.time_spent_settled > self.settle_time:
            return True

        return False