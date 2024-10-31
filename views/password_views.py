"""bibliteocas para caracteres"""
"""secrests para trabalhar com hashs"""
import string, secrets,hashlib,base64

"""manipular diretorios"""
from pathlib import Path


from cryptography.fernet import Fernet


""" 
class para o algoritmo hashing 
"""

class FernetHasher:

    RANDOM_STRING_CHARS = string.ascii_lowercase+string.ascii_uppercase


    BASE_DIR = Path(__file__).resolve().parent.parentpi
    KEY_DIR = BASE_DIR / 'keys'


    "método construtor "
    def __init__(self,key):
        print("iniciando a classe")

        if not isinstance(key,bytes):
            key = key.encode('utf-8')

        self.Fernet = Fernet(key)


    """este é o método de classe onde indentifica os métodos da mesma"""
    @classmethod
    def _get_random_string(cls,length = 25):
        string = ""
        """for para gerar 25 caracteres aleatórios"""
        for i in range(length):
            string += secrets.choice(cls.RANDOM_STRING_CHARS)

        return string
    
    @classmethod
    def create_key(cls, arquive=False):
        value = cls._get_random_string()
        
        print(value)

        """convertendo para bytes para sha256 aceitar"""
        hasher = hashlib.sha256(value.encode('utf-8')).digest()
        print(hasher)

        key = base64.b64encode(hasher)
        print(key)
        if arquive:
            return key, cls.archive_key(key)
        
        return key, None

    @classmethod
    def archive_key(cls,key):

        file = 'key.key'
        while Path(cls.KEY_DIR / file).exists():
            file = f'key_{cls._get_random_string(length=5)}.key'
        with open(cls.KEY_DIR / file,'wb') as arq:
            arq.write(key)

        return cls.KEY_DIR / file 
    

    def encrypt(self , value):
        if not isinstance(value,bytes):
            value = value.encode()
            return value
        
        return value
    
    

FernetHasher.create_key(arquive=True)