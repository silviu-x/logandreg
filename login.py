users = {}  # Dizionario per memorizzare utenti e password
admin_password = "admin123"  # Password fissa per l'admin

def register():
    username = input("Scegli un nome utente: ")
    if username in users:
        print("Questo utente esiste già!")
        return
    password = input("Scegli una password: ")
    users[username] = password
    print("Registrazione completata!")

def login():
    username = input("Inserisci il nome utente: ")
    password = input("Inserisci la password: ")
    
    if username == "admin" and password == admin_password:
        print("Accesso Admin riuscito!")
        view_users()
    elif users.get(username) == password:
        print("Login riuscito!")
    else:
        print("Credenziali errate.")

def view_users():
    print("\n=== Utenti Registrati ===")
    for user in users:
        print(f"- {user}")
    print("=========================")

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
