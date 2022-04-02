from gevent import killall
import undetected_chromedriver.v2 as uc
from time import sleep
from selenium import webdriver
from colorama import init, Fore
init(convert=True, autoreset=True)
if __name__ == '__main__':
    def join(token, url):
        token = token
        url = url
        print(Fore.YELLOW+"Loading browser...")
        driver = uc.Chrome(use_subprocess=True)
        print(Fore.YELLOW+"Browser Loaded!")
        script = """
                    function login(token) {
                    setInterval(() => {
                    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                    }, 50);
                    setTimeout(() => {
                    location.reload();
                    }, 2500);
                    }
                    """
        driver.get(url)
        driver.execute_script(script + f'\nlogin("{token}")')
        print(Fore.YELLOW + 'Logged in with token!')
        sleep(5)
        driver.get(url)
        sleep(3)
        print(Fore.GREEN + "Please do captcha, Then click enter.", end='')
        input()
        forp = url.replace('https://discord.gg/', '')
        print(Fore.YELLOW+"Joined server: "+ forp )
        print(Fore.GREEN + "Join with another token?[yes/no]: ", end='')
        another = input()
        if another=="yes":
            print("\n\n")
            menu()
        if another=="no":
            print("Ok.")
            killall()

    def menu():
        print(Fore.GREEN + "Token: ", end='')
        token = input()
        print(Fore.GREEN + "Invite link: ", end='')
        url = input()
        join(token=token, url=url)
menu()
