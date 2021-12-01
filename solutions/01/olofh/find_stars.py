from collections import deque


def read_input(filepath):
    with open(filepath) as f:
        return f.read().splitlines()


def main():
    # data_path = "small_input.txt"
    data_path = "input.txt"
    measurements = read_input(data_path)
    measurements = list(map(int, measurements))
    print(measurements)

    # Part 1
    nbr_increased = 0
    for last_measurement, measurement in zip(measurements, measurements[1:]):
        if measurement > last_measurement:
            nbr_increased += 1

    print(nbr_increased)

    # Part 2
    nbr_increased = 0
    active_measurements = deque([measurements.pop(0) for _ in range(3)], maxlen=3)
    while len(measurements) > 0:
        last_measurement = sum(active_measurements)
        active_measurements.append(measurements.pop(0))
        measurement = sum(active_measurements)

        if measurement > last_measurement:
            nbr_increased += 1

    print(nbr_increased)


if __name__ == "__main__":
    main()
