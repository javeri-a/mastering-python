
# print(" [+] Addition")

# Screen pe ek option show karta hai.

# Yeh sirf user ko batata hai ke plus se addition hota hai.

# print(" [-] Subtraction")

# Screen pe subtraction ka option show karta hai.

# print(" [*] Multiplication")

# Multiplication option show karta hai.

# print(" [/] Division")

# Division option show karta hai.

# operation: str = input("\n➤ Your choice: ")

# User se operation ka input leta hai.

# operation variable me woh string store hoti hai.

# : str type hint hai, matlab isi variable me string hone ki umeed hai. Yeh runtime pe enforce nahi hota, sirf hint hai.

# \n new line insert karta hai taa ke prompt thoda gap ke sath dikhe.

# print("\n---------- Result ----------")

# Ek header print karta hai, jo result ko visually separate karta hai.

# if operation == '+':

# Yeh check karta hai ke user ne plus chuna hai ya nahi.

# Agar true hua to next indented block execute hoga.

# result: int = num1 + num2

# Dono numbers ko add karta hai.

# Result ko result me store karta hai.

# : int hint hai, result integer expected hai agar inputs integers thay.

# print(f"{num1} + {num2} = {result}")

# f-string se formatted output deta hai.

# Example: "10 + 5 = 15" aayega.

# elif operation == '-':

# Agar user minus choose kare to yeh block chalega.

# result: int = num1 - num2

# Subtraction karta hai aur result store karta hai.

# print(f"{num1} - {num2} = {result}")

# Subtraction ka formatted output show karta hai.

# elif operation == '*':

# Agar multiplication choose kiya to yeh block chalega.

# result: int = num1 * num2

# Multiplication karta hai aur result store karta hai.

# print(f"{num1} * {num2} = {result}")

# Multiplication ka formatted output show karta hai.

# elif operation == '/':

# Agar division choose kiya to yeh block chalega.

# if num2 != 0:

# Division se pehle check karta hai ke divisor zero to nahi.

# Zero hone pe program crash ho sakta hai, isliye check important hai.

# result: float = num1 / num2

# Division karta hai aur result float me store karta hai.

# Division hamesha float return karti hai agar numbers integer bhi hon.

# print(f"{num1} / {num2} = {result:.2f}")

# Formatted output print karta hai.

# {result:.2f} ka matlab result ko 2 decimal places tak round karke dikhana. Example: 3.3333 => 3.33

# else:

# Yeh else us if num2 != 0 ka part hai.

# Yani agar num2 zero hua to yeh run hoga.

# print("⚠ Error! Division by zero.")

# User ko error message dikhata hai.

# Program yahan crash nahi karega, safe message show karega.

# else:

# Yeh outer if-elif chain ka final else hai.

# Agar user ne koi unknown symbol dala ho to yeh run hoga.

# print("⚠ Invalid operation!")

# User ko batata hai ke operation valid nahi tha.

# print("-----------------------------")

# Footer print karta hai.

# Yeh result block ko visually close karta hai.

# Extra notes, short and practical:

# Make sure num1 aur num2 pehle se defined hon. Agar user ne non-numeric input diya to pehle layer me int() conversion ValueError de sakta hai.

# Normalize input with operation = operation.strip() taake accidental spaces hata do.

# Agar tum chaho to operations ke liye operation = operation.strip() aur if operation == '+' ke ilawa if operation in ['+', 'plus'] bhi rakh sakti ho.





print("------------------WELCOME TO JAV CALCULATOR------------------")

num1 = int(input("Enter your 1st number:"))
num2 = int(input("Enter your 2nd number:"))

print("\n choose your operation")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operation: str = input("\n➤ Your choice:  " )


print("\n---------- Result ----------")

if operation == "+" :
    result :int= num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-" :
    result :int= num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*" :
    result :int= num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/" :
    if num2 != 0:
        result :float= num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error! Division by zero.")
  










