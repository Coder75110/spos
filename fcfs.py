class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = f"P{pid}"  # Format PID as P1, P2, etc.
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.response_time = -1  # Initialize to -1 to track the first time it gets CPU

# First-Come, First-Serve (Non-preemptive)
def fcfs(processes):
    time = 0
    for process in sorted(processes, key=lambda p: p.arrival_time):  # Sort by arrival time
        # Wait until the process arrives
        if time < process.arrival_time:
            time = process.arrival_time
        
        # Set response time if it's the first time the process is scheduled
        if process.response_time == -1:
            process.response_time = time - process.arrival_time

        # Process the job and calculate completion, turnaround, and waiting times
        time += process.burst_time
        process.completion_time = time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

    return processes

# Helper function to calculate averages
def calculate_averages(processes):
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    total_waiting_time = sum(p.waiting_time for p in processes)
    total_response_time = sum(p.response_time for p in processes)
    n = len(processes)
    
    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n
    avg_response_time = total_response_time / n
    
    return avg_turnaround_time, avg_waiting_time, avg_response_time

# Helper function to display the results
def display_results(processes, algorithm_name):
    print(f"\n{algorithm_name}:")
    print(f"{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<10}{'Response':<10}")
    for process in processes:
        print(f"{process.pid:<10}{process.arrival_time:<10}{process.burst_time:<10}{process.completion_time:<15}{process.turnaround_time:<15}{process.waiting_time:<10}{process.response_time:<10}")

    avg_turnaround_time, avg_waiting_time, avg_response_time = calculate_averages(processes)
    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Response Time: {avg_response_time:.2f}")

if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    
    for i in range(1, num_processes + 1):
        arrival_time = int(input(f"Enter arrival time for Process P{i}: "))
        burst_time = int(input(f"Enter burst time for Process P{i}: "))
        processes.append(Process(i, arrival_time, burst_time))

    # First-Come, First-Serve Scheduling
    fcfs_result = fcfs(processes)
    display_results(fcfs_result, "First-Come, First-Serve (FCFS)")
