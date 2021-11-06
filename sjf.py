import sys


class Sjf:
    """ Takes a list of process with pid, arrival time and burst time and calculate completion time as per shortest
    remaining job. """
    process_list = []

    def __init__(self, process_list):
        self.process_list = process_list

    def get_next_process(self, prev_completion_time):
        """ Return process with minimum burst time whose completion time is None"""
        min_burst_time = sys.maxsize  # min burst time
        index = None
        count = 0
        for process in self.process_list:
            if process.burst_time < min_burst_time and process.completion_time is None and process.arrival_time <= prev_completion_time:
                min_burst_time = process.burst_time
                index = count
            count += 1
        return self.process_list[index]

    def calculate_completion_time(self):
        """ Calculates completion time"""
        # First calculate the completion time for first process
        self.process_list[0].completion_time = self.process_list[0].arrival_time + self.process_list[0].burst_time
        prev_completion_time = self.process_list[0].completion_time

        # Get next shortest job process
        # calculate its completion time, repeat for n-1 time
        count = len(self.process_list)
        while count > 1:
            index = self.process_list.index(self.get_next_process(prev_completion_time))
            self.process_list[index].completion_time = prev_completion_time + self.process_list[index].burst_time
            prev_completion_time = self.process_list[index].completion_time
            count -= 1
