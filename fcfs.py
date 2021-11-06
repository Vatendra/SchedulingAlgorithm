class Fcfs:
    """ Takes a list of process as input with pid, arrival time and burst time, and calculates rest"""
    process_list = []

    def __init__(self, process_list):
        self.process_list = process_list

    def calculate_completion_time(self):
        """ Calculates completion time for each process."""
        # Completion time for first element
        self.process_list[0].completion_time = self.process_list[0].burst_time
        for i in range(1, len(self.process_list)):
            self.process_list[i].completion_time = self.process_list[i - 1].completion_time + self.process_list[
                i].burst_time
