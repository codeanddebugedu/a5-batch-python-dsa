def calculate_marks(physics, chemistry, science, english, computer):
    total = physics + chemistry + science + english + computer
    print(f"Total = {total}")


# Named Arguments
calculate_marks(science=99, english=44, chemistry=11, physics=88, computer=55)
calculate_marks(52, 85, computer=11, english=99, science=66)
