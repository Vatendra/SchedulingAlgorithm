class Process:
    """Class to implement each process"""

    def __init__(self, pid, arrival_time, burst_time):
        self.id = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = None
        self.turn_around_time = None
        self.waiting_time = None

    def display(self):
        print(" {} {} {}".format(self.id, self.arrival_time, self.burst_time))
