import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Read data from the file
    with open(t, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file]

    # Aggregate the values into ranges
    ranges = [0, 10, 20, 30, 40, 50]
    aggregated_data = [0] * (len(ranges) - 1)
    for snowfall in snowfall_data:
        for i in range(len(ranges) - 1):
            if ranges[i] < snowfall <= ranges[i + 1]:
                aggregated_data[i] += 1
                break

    # Plotting the bar chart
    plt.bar([f"{ranges[i]}-{ranges[i+1]}" for i in range(len(ranges)-1)], aggregated_data, color='skyblue')
    plt.xlabel('Snowfall Range (in cms)')
    plt.ylabel('Frequency')
    plt.title('Snowfall Accumulation')
    # Save the plot as an image file
    plt.savefig('snowfall_plot.png')
    plt.show()

# Test the function
graphSnowfall('snowfall_data.txt')
