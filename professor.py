from random import randint

def get_level()-> int:
        try: 
            level: int =int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                return get_level()
        except ValueError:
            return get_level()

def get_integer(level: str)-> int:
            if level in [1, 2, 3]:
                if int(level) == 1:
                    return randint(0, 9)
                elif int(level) == 2:
                    return randint(10, 99)
                elif int(level) == 3:
                    return  randint(100, 999)
            else:
                raise ValueError
def get_answer(first_number: int, second_number: int)-> int:
        return input(f"{first_number} + {second_number} = ")
def main()->None:
            level:  str = get_level()
            score: int = 0
            
            for _ in range(10):
                try:
                    first_number: int = get_integer(level)
                    second_number: int = get_integer(level)
                except ValueError:
                    main()
                
                correct_answer = first_number + second_number
                tries = 0
                while tries < 3:
                    try:
                        answer = int(get_answer(first_number=first_number, second_number=second_number))
                    except ValueError:
                        print(f"EEE")
                        tries += 1
                    else:
                        if answer == correct_answer:
                            score += 1
                            tries = 0
                            break
                        else:
                            print(f"EEE")
                            tries += 1
                if tries == 3:
                    print(f"{first_number} + {second_number} = {correct_answer}")
                    tries = 0
            print(f"Score: {score}")


if __name__=="__main__":

    main()
