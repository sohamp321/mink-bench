import time
import psutil
import re
import sympy
from pdfminer.high_level import extract_pages, extract_text
import numpy as np 
import pandas as pd 
from PIL import Image,ImageFilter
import random
import multiprocessing


# Monte carlo for single and multicore

def monte_carlo_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_samples) * 4

def single_core_pi(num_samples):
    start_time = time.time()
    pi_estimate = monte_carlo_pi(num_samples)
    end_time = time.time()
    execution_time = end_time - start_time
    return pi_estimate, execution_time

def multi_core_pi(num_samples, num_processes):
    start_time = time.time()
    pool = multiprocessing.Pool(num_processes)
    num_samples_per_process = num_samples // num_processes
    results = pool.map(monte_carlo_pi, [num_samples_per_process] * num_processes)
    pi_estimate = sum(results) / num_processes
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return pi_estimate, execution_time

def monte_carlo():
    num_samples = 2*(10**7)
    num_processes = psutil.cpu_count(logical=False)
    single_core_result, single_core_time = single_core_pi(num_samples)
    multi_core_result, multi_core_time = multi_core_pi(num_samples, num_processes)
    return single_core_time, multi_core_time





# Matrix operation Single core and Multicore

def matrix_op(num_samples):
    A = np.random.rand(num_samples, num_samples)
    B = np.random.rand(num_samples, num_samples)
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions do not match for multiplication")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return

def single_core_op(num_samples):
    start_time = time.time()
    pi_estimate = matrix_op(num_samples)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def multi_core_op(num_samples, num_processes):
    start_time = time.time()
    pool = multiprocessing.Pool(num_processes)
    num_samples_per_process = num_samples // num_processes
    results = pool.map(matrix_op , [num_samples_per_process] * num_processes)
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time



def Mat_operation_check():
    num_samples = 300
    num_processes = psutil.cpu_count(logical=False)
    single_core_time = single_core_pi(num_samples)
    multi_core_time = multi_core_pi(num_samples, num_processes)
    return single_core_time, multi_core_time



# Image Processing and Rendering on single and Multicore

def image_ren_pro(num_samples):
    image = Image.open('Large_image.jpg')
    for _ in range(num_samples):
        image = image.filter(ImageFilter.GaussianBlur(radius=10))
        image = image.rotate(30)
        image = image.convert('L')
        image = image.resize((2000,2000), Image.ANTIALIAS)
        def custom_filter(pixel):
            return pixel
        image = image.point(custom_filter)
    return

def single_core_ren(num_samples):
    start_time = time.time()
    image_ren_pro(num_samples)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def multi_core_ren(num_samples, num_processes):
    start_time = time.time()
    pool = multiprocessing.Pool(num_processes)
    num_samples_per_process = num_samples // num_processes
    results = pool.map(image_ren_pro, [num_samples_per_process] * num_processes)
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


def Check_single_multi_image():
    num_samples = 100
    num_processes = psutil.cpu_count(logical=False)
    single_core_time = single_core_pi(num_samples)
    multi_core_time = multi_core_pi(num_samples, num_processes)
    return single_core_time, multi_core_time


# Arithematics test for single and Multicore

def arith_call(num_samples):
    for _ in range(num_samples):
        for x in range(1,1000):
                3.141592 * 2**x
        for x in range(1,10000):
                float(x) / 3.141592
        for x in range(1,10000):
                float(3.141592) / x
    return

def single_core_pro(num_samples):
    start_time = time.time()
    arith_call(num_samples)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def multi_core_pro(num_samples, num_processes):
    start_time = time.time()
    pool = multiprocessing.Pool(num_processes)
    num_samples_per_process = num_samples // num_processes
    results = pool.map(arith_call, [num_samples_per_process] * num_processes)
    # pi_estimate = sum(results) / num_processes
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def Arith_check():
    num_samples = 5000
    num_processes = psutil.cpu_count(logical=False)
    single_core_time = single_core_pi(num_samples)
    multi_core_time = multi_core_pi(num_samples, num_processes)
    return single_core_time, multi_core_time


