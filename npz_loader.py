import numpy as np
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import io


def load_encrypted_npz(password: str, encrypted_file: str = "student_encr.npz"):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"salt",
        iterations=100000,
        backend=default_backend(),
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))

    with open(encrypted_file, "rb") as f:
        encrypted_data = f.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    npz_buffer = io.BytesIO(decrypted_data)

    with np.load(npz_buffer, allow_pickle=True) as data:
        return {key: data[key] for key in data}
