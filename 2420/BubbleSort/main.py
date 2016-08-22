def main():
    numbers = [3,4,14,235,65,36,87,0,7,3,24,64,35,65,23,112,43,564,4564556]
    bubbleSort(numbers)
    print numbers
def bubbleSort(objects):
    for obj in objects:
        for i in range(len(objects) - 1):
            if objects[i] < objects[i+1]:
                objects[i], objects[i+1] = objects[i+1], objects[i]
main()
