Main Points of __pycache__ and .pyc files

Jab Python code run hota hai to uska compiled form (bytecode) .pyc file me store hota hai.

Ye .pyc files hamesha pycache folder ke andar banti hain.

Purpose: Next time run karte waqt Python dobara compile na kare, direct .pyc use karke program fast execute kare.

Naming format: filename.cpython-313.pyc

yahan 313 = Python version (3.13).

.pyc file ko tum manually run nahi karte, ye Python internally use karta hai.

Badi applications (jaise Django, Flask, NumPy) automatically .pyc generate karti hain performance ke liye.

Agar PYTHONDONTWRITEBYTECODE=1 set ho to .pyc file nahi banti.