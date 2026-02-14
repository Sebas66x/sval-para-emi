from django.shortcuts import render, redirect
from django.contrib import messages

CLAVE_SECRETA = "Sebitas"  # La clave es "Sebitas" (sensible a mayúsculas)

def acceso(request):
    # Si ya está autenticado, redirigir directo a sorpresa
    if request.session.get("ok"):
        return redirect("sorpresa")
    
    if request.method == "POST":
        clave = request.POST.get("clave", "").strip()
        
        if clave == CLAVE_SECRETA:  # Exactamente "Sebitas"
            request.session["ok"] = True
            request.session.set_expiry(86400)  # 24 horas
            return redirect("sorpresa")
        else:
            return render(request, "inicio/login.html", {
                "error": "Clave incorrecta ❌ Intenta de nuevo"
            })
    
    return render(request, "inicio/login.html")

def sorpresa(request):
    if not request.session.get("ok"):
        return redirect("acceso")
    
    # Aquí va tu página principal con todo el contenido
    return render(request, "inicio/sorpresa.html")