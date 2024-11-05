from fisical_person import FisicalPerson
from juridical_person import JuridicalPerson

def main() -> int:
    fperson1: FisicalPerson = FisicalPerson("John", 4000)
    fperson2: FisicalPerson = FisicalPerson("Dave", 2200)
    fperson3: FisicalPerson = FisicalPerson("Rose", 1700)
    jperson1: JuridicalPerson = JuridicalPerson("Jade", 2450)
    jperson2: JuridicalPerson = JuridicalPerson("Roxy", 1270)
    jperson3: JuridicalPerson = JuridicalPerson("Jane", 2000)

    print(fperson1.calculate_tax())
    print(fperson2.calculate_tax())
    print(fperson3.calculate_tax())
    print(jperson1.calculate_tax())
    print(jperson2.calculate_tax())
    print(jperson3.calculate_tax())

    return 0

if(__name__ == "__main__"):
    main()