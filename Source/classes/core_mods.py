"""
This class is responsible for all core operations that involve image manipulation

Created by: Michael Konstantinou, Constandinos Demetriou, George Hadjiantonis
"""
import cv2
from matplotlib import pyplot as plt
import numpy as np
from skimage.metrics import structural_similarity as ssim
import os

def to_grayscale(img):
    """
    Convert image to grayscale.
    """

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray


def set_plot_image(position, title, img, color_map='gray'):
    """
    Sets an image to a specified position, of a matplotlib window.
    """

    plt.subplot(position)
    plt.title(title)

    # Remove ticks
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=color_map)


def plot_all(img_gray, img_dec):
    """
    Plot all results.
    """

    plt.figure()
    set_plot_image(121, 'Initial Image', img_gray)
    set_plot_image(122, 'Picture After jpeg Algorithm', img_dec)
    plt.show()

def mse_func(img_init, img_comp):
    """
    Calculate and return MSE
    """

    return np.power(np.subtract(img_init, img_comp), 2).mean()

def psnr_func(mse_value, L=255):
    """
    Calculate and return PSNR
    """

    return 10 * np.log10(np.power(L, 2) / mse_value)

def ssim_func(img_init, img_comp):
    """
    Calculate and return SSIM
    """
    
    return ssim(img_init.astype(np.float), img_comp.astype(np.float), data_range = img_comp.max() - img_comp.min())

def compression_ratio(img_init_path, img_comp_path):
    """
    Calculate and return Compression ration
    """

    img_init_size = float(os.path.getsize(img_init_path)) / 1024
    img_comp_path = float(os.path.getsize(img_comp_path)) / 1024
    return img_init_size / img_comp_path

def appear_results(class_name, mse_value, psnr_value, ssim_value, compr_ratio):
    """
    Update textboxes to show statistics for values MSE, PSNR, SSIM and compression ratio
    """

    class_name.lineEdit_mse.setText("{:.2f}".format(mse_value))
    class_name.lineEdit_psnr.setText("{:.2f}".format(psnr_value))
    class_name.lineEdit_ssim.setText("{:.2f}".format(ssim_value))
    class_name.lineEdit_compression.setText("{:.2f}".format(compr_ratio))
