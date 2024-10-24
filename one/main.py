from datetime import datetime
from hospede import Hospede
from hotel import Hotel

def main() -> int:
    hospede: Hospede = Hospede("john", "abc", datetime(2000, 5, 12))
    hotel: Hotel = Hotel(hospede, 413, 4500, 12)


if(__name__ == "__main__"):
    main()