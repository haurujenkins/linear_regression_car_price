import numpy as np
import sys

def get_thetas():
    """
    Tente de lire le fichier thetas.csv.
    S'il n'existe pas ou s'il est vide, retourne 0, 0.
    """
    try:
        with open('thetas.csv', 'r') as file:
            content = file.read().strip()
            if not content:
                return 0.0, 0.0
            
            theta0, theta1 = content.split(',')
            return float(theta0), float(theta1)
            
    except FileNotFoundError:
        print("Warning: Model not trained yet (thetas.csv not found). Using default values.")
        return 0.0, 0.0
    except ValueError:
        print("Error: Corrupted thetas file.")
        return 0.0, 0.0

def main():
    x, y = np.loadtxt("data.csv", delimiter=",", skiprows=1, unpack=True)

    real_prices_mean = np.mean(y)
    theta0, theta1 = get_thetas()
    i = 0

    sum_errors_square = 0
    sum_variance_total = 0

    for mileage in x:
        estimated_price = theta0 + (mileage * theta1)
        tmp_error = y[i] - estimated_price
        tmp_error_variance = real_prices_mean - estimated_price
        i += 1
        print(f"car {i} : {tmp_error}")
        sum_errors_square += tmp_error * tmp_error
        sum_variance_total += tmp_error_variance * tmp_error_variance

    round_r = 1 - (sum_errors_square / sum_variance_total)

    print(round_r)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n program interrupted")
        sys.exit(0)
    except Exception as e:
         print(f"error: {e}")