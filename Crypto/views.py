from django.shortcuts import render



def caesar_cipher(message, key, mode):
    result = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            shifted = (ord(char) - base + key if mode == "Encrypt" else ord(char) - base - key) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

def index(request):
    message = ""
    if(request.method == "POST"):
        
        # Récupération des entrées
        message = request.POST.get("message") #un champs de texte qui as reçu le message
        key = request.POST.get("key")   # un champ entier qui reçois qui reçois qui reçois la clé 
        mode = request.POST.get("mode") # un champs boolean qui est reçois vrai s'il s'agit de crypté et qui reçois faut sinon
        if mode:
            result = caesar_cipher(message, key, "Encrypt")
        else:
            result = caesar_cipher(message, key, "Decrypt")
        
        message = result
        
    context = {
        "message":message,
    }
    
    return render(request,"index.html",context)
    
    
    
    
