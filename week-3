# Define the function to calculate the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply discount if the discount percentage is 20% or higher
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # Return the original price if the discount is below 20%
        return price

# Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and print the final price
final_price = calculate_discount(price, discount_percent)

# Output the final price
if final_price != price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${price:.2f}")
