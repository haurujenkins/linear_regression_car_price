import matplotlib.pyplot as plt
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

    theta0, theta1 = get_thetas()
    print(f"Theta0: {theta0}, Theta1: {theta1}")

    x_line = np.array([min(x), max(x)])
    y_line = theta0 + (theta1 * x_line)

    plt.plot(x_line, y_line, 'r-', label=f'Prédiction (y={theta0:.0f} + {theta1:.2f}x)')

    plt.scatter(x, y, color='blue', label='Données')
    plt.xlabel('Kilométrage')
    plt.ylabel('Prix')
    plt.title('Régression Linéaire : Prix vs Kilométrage')
    plt.legend()
    plt.grid(True)
    
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n program interrupted")
        sys.exit(0)
    except Exception as e:
         print(f"error: {e}")
