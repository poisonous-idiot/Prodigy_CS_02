from PIL import Image
import numpy as np

def encrypt(image_path, key):
    image = np.array(Image.open(image_path))
    encrypted_image = image ^ key
    return encrypted_image

def decrypt(encrypted_image, key):
    image = encrypted_image ^ key
    return image

def save_image(image, output_path):
    img = Image.fromarray(image)
    img.save(output_path)

# Example usage
image_path = r"C:\Users\Lenovo\Desktop\Prodigy infotech\Prodigy_CS_02\photo.jpg"
key = 22
encrypted_image = encrypt(image_path, key)
encrypted_image_path = r"C:\Users\Lenovo\Desktop\Prodigy infotech\Prodigy_CS_02\encrypted.jpg"
save_image(encrypted_image, encrypted_image_path)

decrypted_image = decrypt(encrypted_image, key)
decrypted_image_path = r"C:\Users\Lenovo\Desktop\Prodigy infotech\Prodigy_CS_02\decrypted.jpg"
save_image(decrypted_image, decrypted_image_path)
