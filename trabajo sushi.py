
import time 
import os 

limpieza_pantaña =  "cls"

descuento = 0 
dinero = 0
contador = 1
total_producto = 0
poka_roll = 0
ota_roll = 0
pul_roll = 0
angui_roll = 0

#aca empieza el codigo.......

print("bienvenido")
time.sleep(3)

os.system(limpieza_pantaña)

while contador==1:
    
    print("1. Pikachu Roll $4500")
    print("2. Otaku Roll $5000")
    print("3. Pulpo Venesoso Roll $5200")
    print("4. Anguila Electrica Roll $4800")
    print("5. listo el pedido")
    respuesta = int(input("seleciones una opcion (1-5): "))
    
    if respuesta ==1:
        print("se a sumado un Pikachu Roll")
        poka_roll +=1
        total_producto +=1
        dinero +=4500
        time.sleep(1)
        os. system(limpieza_pantaña)

    elif respuesta ==2:
        print("se agrego un Otaku Roll")
        ota_roll +=1
        total_producto +=1
        dinero +=5000
        time.sleep(1)
        os.system(limpieza_pantaña)

    elif respuesta ==3:
        print("Se agrego un pulpo venenoso Roll") 
        pul_roll +=1 
        total_producto +=1
        dinero += 5200
        time.sleep(1)
        os.system(limpieza_pantaña)

    elif respuesta ==4:
        print("se agrego un Anguila Electrica Roll")
        angui_roll +=1
        total_producto +=1
        dinero += 4800
        time.sleep(1)
        os.system(limpieza_pantaña)
    elif respuesta ==5:
        print("veamos si tiene algun descuento")
        contador += 1
        time.sleep(1)
        os.system(limpieza_pantaña)
        break 
    else:
        print("error ingrese un numero bien")
        time.sleep(1)
        os.system(limpieza_pantaña)

while contador == 2:

    print("ingrese su descuento:")
    des = input("")

    if des == "soyotaku":
        descuento = 0.10
        time.sleep(1)
        os.system(limpieza_pantaña)
        break
    else:
        print("no tiene descuento")
        break

total_paga = (dinero*descuento)
final_pago = (total_paga)

print("*******************************")
print(f"total productos: {total_producto}" )
print("*******************************")
print(f"Pikachu Roll: {poka_roll}")
print(f"Otaku Roll: {ota_roll}")
print(f"Pulpo Venenoso Roll: {pul_roll}")
print(f"Anguila Electrica Roll: {angui_roll}")
print("*******************************")
print(f"subtotal por pagar:${dinero}")
print(f"descuento por codigo:{descuento}")
print(f"total:${total_paga}")







