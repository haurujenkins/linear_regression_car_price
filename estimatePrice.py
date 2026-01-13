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

def calculateThePrice(mileage, theta0, theta1):
    return theta0 + (mileage * theta1)

def main():
    theta0, theta1 = get_thetas()
    mileage_input = ""
    while True:
        mileage_input = input("Please enter a mileage: ")
        try:
            mileage = float(mileage_input)
            if mileage < 0:
                print("Mileage cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    price = calculateThePrice(mileage, theta0, theta1)
    print(f"Predicted price for {mileage}km : {price:.2f} €")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n program interrupted")
        sys.exit(0)
    except Exception as e:
         print(f"error: {e}")
