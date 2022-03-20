import os

for i in range(1, 127+1):
    try:
        os.rename(f"arc_{i:0>3}", f"arc{i:0>3}")
    except:
        pass