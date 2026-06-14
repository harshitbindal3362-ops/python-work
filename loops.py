students_age = {
    "Alice": 20,
    "Bob": 22,
    "Charlie": 19,
    "David": 21,
    "Eve": 20
}
print("students_age: " + str(students_age))







quantity_aaloo_paratha = 10
while quantity_aaloo_paratha > 0:
    print("Preparing aaloo paratha. Remaining quantity: " + str(quantity_aaloo_paratha))
    quantity_aaloo_paratha -= 1

    if quantity_aaloo_paratha == 5:
        print("Half of the aaloo parathas are prepared. Time to start preparing gobi parathas.")
        continue

    if quantity_aaloo_paratha == 1:
        print("Only one aaloo paratha left. Need to prepare more.")
        break



rows = [1,2,3,4,5]
for row in rows:
    print("row: " + str(row))
    for seat in range(1,6):
        print(" seat: " + str(seat))