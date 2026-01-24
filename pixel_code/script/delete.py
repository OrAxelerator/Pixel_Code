import shutil

def delete_dir(dir):
    txt = {
        "en": f"1 : Delete {dir} and clone it\n2 : Do nothing",
        "fr": f"1 : Supprime {dir} et le clone\n2 : Ne rien faire"
    }

    print(txt["en"])

    while True:
        try:
            res = int(input("[1/2] ").strip())
        except ValueError:
            continue

        if res == 1:
            print(f"deleting {dir}")
            shutil.rmtree(dir, ignore_errors=True)
            print(f"{dir} delete")

            return True

        if res == 2:
            print("nothing happened")
            return False
        # toute autre valeur → boucle → re-input

#dir = "trophee-nsi-ant"
#delete_dir(dir)
