total_items=0
total_cost=0

# Prime the loop with the first input
item=float(input("Enter the price of item (-1 to stop):"))
while item!=-1:
    # Increment item count for every valid item entered
    total_items=total_items+1

    # Apply tax/surcharge rules based on price tiers
    if item<50:
        final_price=item*1.05
    elif item>=50 and item<=200:
        final_price=item*1.10
    else:
        final_price=(item*1.15)+10
        
    # Accumulate total cost
    total_cost=total_cost+final_price
    # Get the next input at the end of the loop
    item = float(input("Enter the price of item (-1 to stop): "))

print()
print("--- Receipt Summary ---")
print (f"You are buying {total_items} items, the final price is {total_cost:.2f}$")
