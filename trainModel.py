import csv
import sys

def load_data(filename):
    km_list = []
    price_list = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if len(row) == 2:
                    km = float(row[0])
                    price = float(row[1])

                    km_list.append(km)
                    price_list.append(price)
        return km_list, price_list
    
    except FileNotFoundError:
        print("Error: file not found")
        sys.exit(1)
    except Exception as e:
        print(f"error: {e}")
        sys.exit(1)

def normalize_data(data: list):
    max_val = max(data)
    min_val = min(data)
    normalized_data = []

    for x in data:
        calc = (x - min_val) / (max_val - min_val)
        normalized_data.append(calc)

    return(normalized_data, max_val, min_val)


def train(km_list, price_list):
    learning_rate = 0.1
    epochs = 1900
    m = len(km_list)

    theta0 = 0.0
    theta1 = 0.0

    for i in range(epochs):
        sum_errors_theta0 = 0
        sum_errors_theta1 = 0

        for j in range(m):
            x = km_list[j]
            y = price_list[j]

            prediction = (theta1 * x) + theta0

            error = prediction - y

            sum_errors_theta0 += error
            sum_errors_theta1 += error * x

        tmp_theta0 = learning_rate * (1/m) * sum_errors_theta0
        tmp_theta1 = learning_rate * (1/m) * sum_errors_theta1

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

        if i % 100 == 0:
            print(f"Epoch {i}: theta0={theta0:.4f}, theta1={theta1:.4f}")
    
    return theta0, theta1


def save_tethas(theta0, theta1):
    try:
        with open('thetas.csv', 'w') as file:
            file.write(f"{theta0},{theta1}")
        print("Thetas saved in thetas.csv")
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":

    print("Loading data...")
    km, prices = load_data("data.csv")

    print("Normalization...")
    km_norm, km_max, km_min = normalize_data(km)
    prices_norm, price_max, price_min = normalize_data(prices)

    print("Training model...")
    th0_norm, th1_norm = train(km_norm, prices_norm)

    print(f"Thetas normalized found : Thetat0 = {th0_norm}, Theta1 = {th1_norm}")
    print("Denormalizing thetas...")

    delta_y = price_max - price_min
    delta_x = km_max - km_min

    real_theta1 = (delta_y / delta_x) * th1_norm
    real_theta0 = price_min + (delta_y * th0_norm) - (real_theta1 * km_min)

    print(f"Real thetas found : Thetat0 = {real_theta0}, Theta1 = {real_theta1}")

    save_tethas(real_theta0, real_theta1)



