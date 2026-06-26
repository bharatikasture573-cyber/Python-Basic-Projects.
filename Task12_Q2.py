def manage_marks():
    marks = []
    try:
        # Take input for 5 subject marks
        print("Enter marks for 5 subjects :")
        for i in range(5):
            mark = float(input(f"Enter marks for Subject : "))
            marks.append(mark)
        average = sum(marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)
        marks.sort(reverse=True)

        # Display results
        print("\n****** Result ******")
        print("Marks List : ", marks)
        print("Average Marks : ", average)
        print("Highest Marks : ", highest)
        print("Lowest Marks : ", lowest)
        print("Marks in Descending Order : ", marks)

    except ValueError:
        print("Error: Please enter numeric values only.")
# Call the function
manage_marks()