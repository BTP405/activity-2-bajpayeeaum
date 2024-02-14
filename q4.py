def printStats(t):
    def stats_decorator(func):
        def wrapper(numbers):
            count = len(numbers)
            if count > 0:
                total = sum(numbers)
                average = total / count
                maximum = max(numbers)
                print("Numbers:", numbers)
                print("Count:", count)
                print("Average:", average)
                print("Maximum:", maximum)
            else:
                print("No numbers found in the line.")
            print()  # Empty line for readability
            func(numbers)
        return wrapper

    @stats_decorator
    def process_line(numbers):
        pass

    try:
        with open(t, 'r') as file:
            for line in file:
                numbers = [float(num) for num in line.strip().split()]
                process_line(numbers)
    except FileNotFoundError:
        print(f"File '{t}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    file_path = "data.txt"  # Update with the path to your file
    printStats(file_path)
