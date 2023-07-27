# Email slicer Project


# Jeito 1 - função
def email_slicer(email):
    for x in email:
        pass
    if '@' not in email:
        print("Endereço de email inválido")
    else:
        nome_usuário, dominio = email.split("@")
        print(f"Nome do Usuário: {nome_usuário}\nNome do domínio: @{dominio}")


email = str(input("Digite o seu email: "))
email_slicer(email)

print()

# jeito 2 - Básico

email = str(input("Digite o seu email: "))

nome_usuário, dominio = email.split("@")

print(nome_usuário)
print(dominio)


# Jeito 3 - função (
def email_slicer2(email):
    dominios_populares = ["gmail.com", "outlook.com", " hotmail.com", "icloud.com", "aol.com", "protonmail.com"]

    for x in email:
        pass
    if '@' not in email:
        print("Endereço de email inválido")
    else:
        nome_usuário, dominio = email.split("@")
        if dominio not in dominios_populares:
            print(f"Nome do Usuário: {nome_usuário}\nNome do domínio: @{dominio}")
            print("Atenção o endereço de email apresentado não faz parte de domínios populares. Verifique a procedencia do email em questão")
            print("gmail.com (Google)  outlook.com (Microsoft)  yahoo.com (Yahoo)  hotmail.com (anteriormente da Microsoft, mas agora integrado ao Outlook)  icloud.com (Apple)  aol.com (AOL) protonmail.com (ProtonMail, serviço de email criptografado) mail.com (Mail.com)")
        else:
            print(f"Nome do Usuário: {nome_usuário}\nNome do domínio: @{dominio}")


email = str(input("Digite o seu email: "))
email_slicer2(email)

