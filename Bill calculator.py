def bill_calculator():
    print("მოგესალმებით! ეს არის მარტივი კალკულატორი პროდუქტების საერთო თანხის გამოსათვლელად.")
    
    # საცავები პროდუქტებისთვის და ფასებისთვის
    products = []
    prices = []
    
    while True:
        # მომხმარებელს სთხოვს შეიყვანოს პროდუქტის სახელი
        product = input("შეიყვანეთ პროდუქტის სახელი (ან 'stop' შეწყვეტისთვის): ")
        if product.lower() == 'stop':
            break
        
        # პროდუქტის ფასის მოთხოვნა
        try:
            price = float(input(f"{product} - შეიყვანეთ ფასი: "))
            products.append(product)
            prices.append(price)
        except ValueError:
            print("გთხოვთ, სწორად შეიყვანეთ ფასი.")
    
    # საერთო თანხის გამოთვლა
    total = sum(prices)
    
    # ანგარიშის ჩვენება
    print("\nანგარიში:")
    for i in range(len(products)):
        print(f"{products[i]} - {prices[i]:.2f} ლარი")
    print(f"\nსაერთო თანხა: {total:.2f} ლარი")

# კალკულატორის დაწყება
bill_calculator()
