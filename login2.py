users = {}  # Dizionario per utenti e password
blocked_users = {}  # Dizionario per utenti bloccati
admin_password = "admin123"  # Password admin

def register():
    username = input("Scegli un nome utente: ")
    if username in users:
        print("Questo utente esiste già!")
        return
    
    password = input("Scegli una password: ")
    password2 = input("Conferma la password: ")
    if password2 != password:
        print("Le password non coincidono!")
        return
    users[username] = {"password": password, "attempts": 0}
    print("Registrazione completata!")

def login():
    username = input("Inserisci il nome utente: ")

    # Controllo se l'utente è bloccato
    if username in blocked_users:
        print("Questo account è bloccato. Contatta l'admin per sbloccarlo.")
        return

    password = input("Inserisci la password: ")

    # Accesso admin
    if username == "admin" and password == admin_password:
        print("Accesso Admin riuscito!")
        admin_menu()
        return
    
    # Controllo credenziali
    if username in users:
        if users[username]["password"] == password:
            print("Login riuscito!")
            users[username]["attempts"] = 0  # Reset tentativi falliti
        else:
            users[username]["attempts"] += 1
            print(f"Password errata! Tentativi rimasti: {3 - users[username]['attempts']}")

            if users[username]["attempts"] >= 3:
                blocked_users[username] = True
                print("Troppe prove sbagliate! Questo account è ora bloccato.")
    else:
        print("Questo utente non esiste.")

def view_users():
    print("\n=== Utenti Registrati ===")
    for user in users:
        status = "Attivo" if user not in blocked_users else "Bloccato"
        print(f"- {user} ({status})")
    print("=========================")

def unblock_user():
    username = input("Inserisci il nome utente da sbloccare: ")
    if username in blocked_users:
        del blocked_users[username]
        users[username]["attempts"] = 0  # Reset tentativi
        print(f"L'utente '{username}' è stato sbloccato!")
    else:
        print("Questo utente non è bloccato.")

def admin_menu():
    while True:
        choice = input("\n1) Vedi utenti  2) Sblocca utente  3) Esci\nScelta: ")
        if choice == '1':
            view_users()
        elif choice == '2':
            unblock_user()
        elif choice == '3':
            print("Uscita dalla modalità Admin.")
            break
        else:
            print("Scelta non valida.")

def main():
    while True:
        choice = input("\nRegistrati (r), Accedi (l), Esci (e): ").lower()
        if choice == 'r':
            register()
        elif choice == 'l':
            login()
        elif choice == 'e':
            print("Uscita...")
            break
        else:
            print("Scelta non valida.")

main()
