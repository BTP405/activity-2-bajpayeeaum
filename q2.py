def graphSnowfall(t):
import matplotlib.pyplot as plt

plt.ion()  # Enable interactive mode

def graphSnowfall(t):
    # Read data from file
    with open(t, 'r') as file:
        lines = file.readlines()

    # Initialize bins
    bins = [0] * 10

    # Aggregate values into bins
    for line in lines:
        snowfall = int(line.strip())
        bin_index = snowfall // 10
        if bin_index < 10:
            bins[bin_index] += 1
        else:
            bins[-1] += 1

    # Create bar chart
    plt.bar(range(0, 101, 10), bins)
    plt.xlabel('Snowfall (cm)')
    plt.ylabel('Occurrences')
    plt.title('Snowfall Distribution')
    plt.show()
