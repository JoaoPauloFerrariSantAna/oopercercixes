from normal_medicine import NormalMedicine
from brand_medicine import BrandMedicine
from farmacy import Farmacy

def main() -> int:
    normal_medicine1: NormalMedicine = NormalMedicine(45.20)
    normal_medicine2: NormalMedicine = NormalMedicine(25.20)
    normal_medicine3: NormalMedicine = NormalMedicine(25.20)
    brand_medicine1: BrandMedicine = BrandMedicine(62.90, "banana")
    brand_medicine2: BrandMedicine = BrandMedicine(62.90, "maça")
    
    farmancy: Farmacy = Farmacy([normal_medicine1, normal_medicine2, normal_medicine3], [brand_medicine1, brand_medicine2])

    print(farmancy.calculate_normal_medicine_price())

    return 0

if(__name__ ==  "__main__"):
    main()