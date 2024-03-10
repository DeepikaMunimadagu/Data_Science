import matplotlib.pyplot as plt
from skimage import io, img_as_float
import bm3d
import cv2
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

def load_image(file_path):
    """Load and return an image as a float."""
    return img_as_float(io.imread(file_path, as_gray=True))

def display_images(original, denoised, title_original="Original", title_denoised="Denoised"):
    """Display original and denoised images side by side."""
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title(title_original)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(denoised, cmap='gray')
    plt.title(title_denoised)
    plt.axis('off')

    plt.show()

def calculate_metrics(original, denoised):
    """Calculate PSNR and SSIM between original and denoised images."""
    psnr_value = peak_signal_noise_ratio(original, denoised)
    ssim_value, _ = structural_similarity(original, denoised, full=True)
    return psnr_value, ssim_value

def main():
    # File path to the noisy MRI image
    file_path = r'C:\Users\HP\OneDrive\Desktop\noisy mri.tif'

    # Load the noisy MRI image
    noisy_img = load_image(file_path)

    # Denoise using BM3D
    sigma_psd = 0.2  # Adjust as needed
    denoised_img = bm3d.bm3d(noisy_img, sigma_psd=sigma_psd, stage_arg=bm3d.BM3DStages.HARD_THRESHOLDING)

    # Display the original and denoised images
    display_images(noisy_img, denoised_img)

    # Calculate and print denoising metrics
    psnr_value, ssim_value = calculate_metrics(noisy_img, denoised_img)
    print(f"PSNR: {psnr_value:.2f} dB")
    print(f"SSIM: {ssim_value:.4f}")

    # Optionally, you can save the denoised image
    # cv2.imwrite("denoised_image.png", denoised_img * 255)

if _name_ == "_main_":
    main()
