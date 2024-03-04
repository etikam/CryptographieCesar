from django.shortcuts import render



def caesar_cipher(message, key, mode):
    result = ""
    for char in message:
        if ord(char) not in range(65,90) and ord(char) not in range(97,122):
            result += char
        elif char.isalpha():
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
    message_result=""
    message_error_key =""
    message_error_mode=""
    key=""
    if(request.method == "POST"):
        
        # Récupération des entrées
        message = request.POST.get("message") #un champs de texte qui as reçu le message
        key = request.POST.get("key")   # un champ entier qui reçois qui reçois qui reçois la clé 
        try:
            key = int(key)
        except:
            message_error_key ="vous essayé de joué avec la clé"
        mode = request.POST.get("mode") # un champs boolean qui est reçois vrai s'il s'agit de crypté et qui reçois faut sinon
        print(mode)
        
        if mode:
            result = caesar_cipher(message, key, "Encrypt")
        else:
            result = caesar_cipher(message, key, "Decrypt")
        
        message_result = result
    
    context = {
        "message_result":message_result,
        "message":message,
        "key":key,
        "message_error_mode":message_error_mode,
        "message_error_key":message_error_key,
    }
    
    return render(request,"base.html",context)
    
    
    
    
