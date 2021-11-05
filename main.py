import process
import fcfs


def main():
    number_of_process = int(input("Enter number of process: "))
    process_list = []
    for pid in range(number_of_process):
        print("For PID {} ".format(pid))
        arrival_time = float(input("Enter arrival time : "))
        burst_time = float(input("Enter burst time : "))
        process_list.append(process.Process(pid, arrival_time, burst_time))
    schedule = fcfs.Fcfs(process_list)
    schedule.display()


main()
