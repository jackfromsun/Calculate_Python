initial_value = float(input("Enter the initial value of the asset: "))
salvage_value = float(input("Enter the salvage value of the asset: "))
useful_life = float(input("Enter the useful life of the asset (in years): "))

depreciation_per_year = (initial_value - salvage_value) / useful_life

print("The annual depreciation of the asset is: $", depreciation_per_year)
