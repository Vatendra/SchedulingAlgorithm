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

    def calculate_turn_around_time(self):
        """ Calculates turn around time for each process"""
        # First calculate completion time
        self.calculate_completion_time()
        # Turn around time for first element
        for i in range(len(self.process_list)):
            self.process_list[i].turn_around_time = self.process_list[i].completion_time - self.process_list[
                i].arrival_time

    def calculate_waiting_time(self):
        """ Calculates waiting time for each process"""
        # First calculate turn around time
        self.calculate_turn_around_time()
        for i in range(len(self.process_list)):
            self.process_list[i].waiting_time = self.process_list[i].turn_around_time - self.process_list[i].burst_time

    def display(self):
        self.calculate_waiting_time()
        print("PID | ARRIVAL TIME | BURST TIME | COMPLETION TIME | TURN AROUND TIME | WAITING TIME ")
        for item in self.process_list:
            print("{:>2} {:>12} {:>12} {:>16} {:>16} {:>16}".format(item.id, item.arrival_time, item.burst_time,
                                                                    item.completion_time, item.turn_around_time,
                                                                    item.waiting_time))
