for i in range(5):
    name = input("Enter the name:")
    total = 0
    for j in range(5):
      mark = float(input("Enter the mark"))
      total += mark
    print(" The total of", name, "is", total)
