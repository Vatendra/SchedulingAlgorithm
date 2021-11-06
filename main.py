import process
import fcfs
import sjf


class Main:
    process_list = []

    def __init__(self):
        pass

    def input_data(self):
        """ Takes pid, arrival time and burst time as input"""
        number_of_process = int(input("Enter number of process: "))
        for pid in range(number_of_process):
            print("For PID {} ".format(pid))
            arrival_time = float(input("Enter arrival time : "))
            burst_time = float(input("Enter burst time : "))
            self.process_list.append(process.Process(pid, arrival_time, burst_time))
        self.schedule_sjf()

    def calculate_turn_around_time(self):
        """ Calculates turn around time for each process"""
        # Turn around time for first element
        for i in range(len(self.process_list)):
            self.process_list[i].turn_around_time = self.process_list[i].completion_time - self.process_list[
                i].arrival_time

    def calculate_waiting_time(self):
        """ Calculates waiting time for each process"""
        for i in range(len(self.process_list)):
            self.process_list[i].waiting_time = self.process_list[i].turn_around_time - self.process_list[i].burst_time

    def display(self):
        print("PID | ARRIVAL TIME | BURST TIME | COMPLETION TIME | TURN AROUND TIME | WAITING TIME ")
        for item in self.process_list:
            print("{:>2} {:>12} {:>12} {:>16} {:>16} {:>16}".format(item.id, item.arrival_time, item.burst_time,
                                                                    item.completion_time, item.turn_around_time,
                                                                    item.waiting_time))

    def schedule_sjf(self):
        schedule = sjf.Sjf(self.process_list)
        schedule.calculate_completion_time()
        self.process_list = schedule.process_list
        self.calculate_turn_around_time()
        self.calculate_waiting_time()
        self.display()

    def schedule_fcfs(self):
        schedule = fcfs.Fcfs(self.process_list)
        schedule.calculate_completion_time()
        self.process_list = schedule.process_list
        self.calculate_turn_around_time()
        self.calculate_waiting_time()
        self.display()


main = Main()
main.input_data()
