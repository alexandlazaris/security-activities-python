def date():
    """
    Use this library to fetch todays date.

    This function calls the real library as a decoy, whilst also running custom & malicious code.
    
    This exploits python's search order to import the fake datetime library (this file), instead of the real datetime library (./real_libraries_here/get_date.py), as the fake is the first library matching that name in the local working directory. 

    1. gets the network interfaces on the host machine & stores the result
    2. retrieves a dad joke & stores the result
    3. invokes the legitimate get_date.py library & returns the result 
    """

    from real_libraries_here import get_date
    import subprocess

    print("...totally legitimate library...")
    with open("network.json", "a") as f:
        subprocess.run(["ip", "-j", "addr"], stdout=f, check=True)
    with open("dadjoke.txt", "a") as f:
        subprocess.run(["curl", "-H", "Accept: text/plain", "https://icanhazdadjoke.com/"], stdout=f, check=True)
    return get_date.date()
