import random

def higher_or_lower(target: int, num_guesses) -> str:
    # Initialise iterator
    i = 0
    
    # While the iterator is less than the number of guesses
    while i < num_guesses:
        
        # Get the input value from the user
        x = int(input("Type a integer: "))
        
        # Try
        try:
            # If greater than the target
            if x > target:
                
                print("Go lower")
                
                i += 1
            
            # If less than the target
            if x < target:
                
                print("Go higher")
                
                i += 1
            
            # If same as the target
            elif x == target:
                
                print("Nice!")
                
                break
            
        # Error catching for worng input
        except ValueError:
             
            print("Enter a number (integer)")
            
            i += 1
    else:
        
        print("Out of guesses!")

if __name__ == '__main__':
    # Get a random target
    target = random.randint(0,1000)
    
    # Get the number of guesses chosen by the user
    num_guesses = int(input("Enter number of guesses: "))
    
    print(target)
    
    # Run the function we need to print it out
    higher_or_lower(target, num_guesses)