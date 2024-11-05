def printJobScheduling(arr, t):
    # length of array
    n = len(arr)

    # Sort all jobs according to decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job = ['-1'] * t

    # To store total profit
    total_profit = 0

    # Iterate through all given jobs
    for i in range(len(arr)):
        # Find a free slot for this job
        # (Note that we start from the last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                total_profit += arr[i][2]
                break

    # print the sequence
    print("Job sequence:", job)
    print("Total profit:", total_profit)

if __name__ == '__main__':
    n = int(input("Enter the number of jobs: "))
    arr = []

    for i in range(n):
        job_id = input(f"Enter job ID for job {i+1}: ")
        deadline = int(input(f"Enter deadline for job {i+1}: "))
        profit = int(input(f"Enter profit for job {i+1}: "))
        arr.append([job_id, deadline, profit])

    max_deadline = max(job[1] for job in arr)
    print("Following is maximum profit sequence of jobs")

    printJobScheduling(arr, max_deadline)

# Time Complexity: (O(n^2))
# Space Complexity: (O(t + n))

# Sample I/O
# Enter the number of jobs: 4
# Enter job ID for job 1: A
# Enter deadline for job 1: 1
# Enter profit for job 1: 100
# Enter job ID for job 2: B
# Enter deadline for job 2: 2
# Enter profit for job 2: 50
# Enter job ID for job 3: C
# Enter deadline for job 3: 3
# Enter profit for job 3: 200
# Enter job ID for job 4: D
# Enter deadline for job 4: 4
# Enter profit for job 4: 70
# Following is maximum profit sequence of jobs
# Job sequence: ['B', 'A', 'D', 'C']
# Total profit: 250