# Program list untuk menampung hoby

hoby = []
stop = False
i = 0

# isi hoby
while(not stop):
    new_hoby = input(f"Hobby ke-{i}: ")
    hoby.append(new_hoby)
    i += 1
    ask = input("ada lagi? (y/n): ")
    if(ask == "n"):
        stop = True
    elif(ask == "y"):
        stop = False
    else:
        break

# cetak semua hoby
print("="*50)
print(f"kamu punya {len(hoby)} hobi")
for hobby in hoby:
    print(f"- {hobby}")