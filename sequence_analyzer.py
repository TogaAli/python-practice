# Prompt the user for the starting integer
integer=int(input("Enter a positive starting point!"))

# Initialize tracking variables
steps=0
even=0
odd=0
maximum=integer

# Check the very first starting number's parity
if integer%2==0:
    even=even+1
else:
    odd=odd+1

# Generate the sequence automatically until it reaches 1   
while integer!=1:
    # If the number is even, divide by 2
    if integer%2==0:
        integer=integer//2
        print(f"Step {steps+1}: {integer} (Even)")
        even=even+1
    # If the number is odd, multiply by 3 and add 1
    else:
        integer=(integer*3)+1
        print(f"Step {steps+1}: {integer} (Odd)")
        odd=odd+1
        
    # Check if the current value is the highest peak reached so far 
    if integer>maximum:
        maximum=integer

    # Increment the step counter
    steps=steps+1

# Print the final summary of the sequence analysis    
print()
print("--- Sequence Analysis ---")
print(f"Total Steps: {steps}")
print(f"Maximum value: {maximum}")
print(f"Total Even Numbers: {even}")
print(f"Total Odd Numbers: {odd}")
