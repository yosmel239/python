ingreso_mensual = 19000
gasto_mensual = 12000

#if animados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estás en números rojos")
    elif ingreso_mensual - gasto_mensual < 5000:
        print("estás ajustado de dinero")
    else :
        print("tienes buena salud financiera")
  
elif ingreso_mensual <= 10000:
    print("ingresas lo justo")
else :
    print("debes mejorar tus ingresos")