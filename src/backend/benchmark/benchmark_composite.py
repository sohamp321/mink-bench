import time
import psutil
import re
import sympy
from pdfminer.high_level import extract_pages, extract_text
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from PIL import Image,ImageFilter
import random
import multiprocessing

# global ml_temp_avg, ml_max_temp, ml_freq_avg, ml_max_freq
ml_max_temp = 0
ml_max_freq = 0
ml_temp_avg = 0
ml_freq_avg = 0

# Function to obtain current CPU temperature
def curr_temp():
    temp = (psutil.sensors_temperatures()['nvme'][1][1]+psutil.sensors_temperatures()['nvme'][2][1])/2
    return temp

# MULTI CORE KERNEL BENCHMARK TESTING

# ML-Train Test
def ml_train():
    print("ml train start")
    st1 = time.time()
    cpu_f1 = (psutil.cpu_freq().current)/1000
    cpu_t1 = curr_temp()
    df = pd.read_csv(r'/home/soham/Coding_Adventures/OS/MinorProject/MinkBenchTake2/src/backend/benchmark/my_benchmark_data.csv')
    cpu_t2 = curr_temp()
    cpu_f2 = (psutil.cpu_freq().current)/1000
    y_data = np.array(df['Class'])
    x_data = np.array(df.drop(columns=['Class']))
    x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,random_state = 100,stratify = y_data)
    Ada_clf = AdaBoostClassifier(random_state=42)
    cpu_t3 = curr_temp()
    cpu_f3 = (psutil.cpu_freq().current)/1000
    Ada_clf.fit(x_test,y_test)
    cpu_t4 = curr_temp()
    cpu_f4 = (psutil.cpu_freq().current)/1000
    st2 = time.time()
    temp_avg = cpu_t1 + cpu_t2 + cpu_t3 + cpu_t4
    temp_avg = temp_avg/4
    freq_avg = cpu_f1 + cpu_f2 + cpu_f3 + cpu_f4
    freq_avg = freq_avg/4
    max_temp = max(cpu_t1,cpu_t2,cpu_t3,cpu_t4)
    max_freq = max(cpu_f1,cpu_f2,cpu_f3,cpu_f4)
    print("ml train completed")
    print("time taken : ",st2-st1, "avg_freq : ",freq_avg, "max_freq : ", max_freq , "avg_temp :  ",temp_avg, "max_temp : ",max_temp)
    return st2-st1, freq_avg, max_freq , temp_avg, max_temp

# Arithematic Operations Test
def Arith_test1():
    print("arith test start")
    start_benchmark = 700 
    start_benchmark = int(start_benchmark)
    cpu_freq_total = 0
    cpu_max_freq = 0
    cpu_temp_total = 0
    cpu_max_temp = 0
    start = time.time()
    for i in range(0,start_benchmark):
        # print(i)
        cpu_freq = (psutil.cpu_freq().current)/1000
        cpu_temp = curr_temp()
        cpu_temp_total+= cpu_temp
        cpu_freq_total+=cpu_freq
        if(cpu_freq > cpu_max_freq):
            cpu_max_freq = cpu_freq
        if(cpu_temp > cpu_max_temp):
            cpu_max_temp = cpu_temp
        for x in range(1,1000):
            3.141592 * 2**x
        for x in range(1,8000):
            float(x) / 3.141592
        for x in range(1,800):
            float(3.141592) / x
    cpu_freq_avg = cpu_freq_total/start_benchmark
    cpu_temp_avg = cpu_temp_total/start_benchmark
    end = time.time()
    duration = (end - start)
    print("time taken : ",duration,"avg_freq : ",cpu_freq_avg,"max_freq : ",cpu_max_freq, "avg_temp :  ",cpu_temp_avg, "max_temp : ",cpu_max_temp)
    print("arith test finish")
    return duration,cpu_freq_avg,cpu_max_freq,cpu_temp_avg,cpu_max_temp




# Arithematic Exponentiation Test 2

def Arith_test2():
    print("arith test 2 start")
    start_benchmark = 500 
    start_benchmark = int(start_benchmark)
    cpu_freq_total = 0
    cpu_max_freq = 0
    cpu_temp_total = 0
    cpu_max_temp = 0
    start = time.time()
    for i in range(0,start_benchmark):
        # print(i)
        cpu_freq = (psutil.cpu_freq().current)/1000
        cpu_temp = curr_temp()
        cpu_temp_total+= cpu_temp
        cpu_freq_total+=cpu_freq
        if(cpu_freq > cpu_max_freq):
            cpu_max_freq = cpu_freq
        if(cpu_temp > cpu_max_temp):
            cpu_max_temp = cpu_temp
        for x in range(1,1000):
            x = 2**x
        for y in range(1,8000):
            y = 2**(1/y)
    cpu_freq_avg = cpu_freq_total/start_benchmark
    cpu_temp_avg = cpu_temp_total/start_benchmark
    end = time.time()
    duration = (end - start)
    print("arith test 2 finished")
    print(duration,cpu_freq_avg,cpu_max_freq,cpu_temp_avg,cpu_max_temp)
    return duration,cpu_freq_avg,cpu_max_freq,cpu_temp_avg,cpu_max_temp



# PDF Renderer Testing "Kernel Benchmark"

def pdf_text_render():
    print("pdf text start")
    start_time = time.time()
    cpu_freq_total = 0
    cpu_max_freq = 0
    cpu_temp_total = 0
    cpu_max_temp = 0
    count = 0
    for page_layout in extract_pages(r'/home/soham/Coding_Adventures/OS/MinorProject/MinkBenchTake2/src/backend/benchmark/trial.pdf'):
        cpu_freq = (psutil.cpu_freq().current)/1000
        cpu_temp = curr_temp()
        cpu_temp_total+= cpu_temp
        cpu_freq_total+=cpu_freq
        count+=1
        if(cpu_freq > cpu_max_freq):
            cpu_max_freq = cpu_freq
        if(cpu_temp > cpu_max_temp):
            cpu_max_temp = cpu_temp
        for element in page_layout:
            continue
    cpu_freq_avg = cpu_freq_total/count
    cpu_temp_avg = cpu_temp_total/count
    end_time = time.time()
    duration = end_time-start_time
    print("pdf text finished")
    print((1273/duration),cpu_freq_avg,cpu_max_freq,cpu_temp_avg,cpu_max_temp)
    return (1273/duration),cpu_freq_avg,cpu_max_freq,cpu_temp_avg,cpu_max_temp



# Prime Factorization / Tree Search

def Prime_calc():
    start_time = time.time()
    n = 20000000
    cpu_f1 = (psutil.cpu_freq().current)/1000
    cpu_t1 = curr_temp()
    primes = list(sympy.primerange(1, n))
    cpu_t2 = curr_temp()
    cpu_f2 = (psutil.cpu_freq().current)/1000
    end_time = time.time()
    freq_avg = (cpu_f1 + cpu_f2)/2
    temp_avg = (cpu_t2 + cpu_t1)/2
    time_elapsed = end_time - start_time
    return time_elapsed, freq_avg, temp_avg



# Matrix Operations 

# def matrix_multiply():
#     print("matrix multiply start")
#     import numpy as np
#     cpu_freq_total = 0
#     cpu_max_freq = 0
#     cpu_temp_total = 0
#     cpu_max_temp = 0
#     st = time.time()
#     A = np.random.rand(20, 30)
#     B = np.random.rand(30, 20)
#     if len(A[0]) != len(B):
#         raise ValueError("Matrix dimensions do not match for multiplication")
#     result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
# #     for i in range(len(A)):
#         for j in range(len(B[0])):
#             for k in range(len(B)):
#                 result[i][j] += A[i][k] * B[k][j]
#                 cpu_freq = (psutil.cpu_freq().current)/1000
#                 cpu_temp = curr_temp()
#                 cpu_temp_total+= cpu_temp
#                 cpu_freq_total+=cpu_freq
#                 if(cpu_freq > cpu_max_freq):
#                     cpu_max_freq = cpu_freq
#                 if(cpu_temp > cpu_max_temp):
#                     cpu_max_temp = cpu_temp
#     avg_freq = cpu_freq_total/(len(A)*len(B[0])*len(B))
#     avg_temp = cpu_temp_total/(len(A)*len(B[0])*len(B))
#     et = time.time()
#     print("matrix multi finished")
#     print(et - st, avg_freq, cpu_max_freq, avg_temp, cpu_max_temp)
#     return et - st, avg_freq, cpu_max_freq, avg_temp, cpu_max_temp



# Image Rendering and Processing

def Image_processing():
    print("image start")
    st = time.time()
    cpu_freq_total = 0
    cpu_max_freq = 0
    cpu_temp_total = 0
    cpu_max_temp = 0
    image = Image.open(r'/home/soham/Coding_Adventures/OS/MinorProject/MinkBenchTake2/src/backend/benchmark/Large_image.jpg')
    for _ in range(200):
        cpu_freq = (psutil.cpu_freq().current)/1000
        cpu_temp = curr_temp()
        cpu_temp_total+= cpu_temp
        cpu_freq_total+=cpu_freq
        if(cpu_freq > cpu_max_freq):
            cpu_max_freq = cpu_freq
        if(cpu_temp > cpu_max_temp):
            cpu_max_temp = cpu_temp
        image = image.filter(ImageFilter.GaussianBlur(radius=10))
        image = image.rotate(30)
        image = image.convert('L')
        image = image.resize((2000,2000), Image.ANTIALIAS)
        def custom_filter(pixel):
            return pixel
        image = image.point(custom_filter)
    avg_freq = cpu_freq_total/200
    avg_temp = cpu_temp_total/200
    et = time.time()
    print(et - st, avg_freq,cpu_max_freq, avg_temp, cpu_max_temp)
    print("image finished")
    return et - st, avg_freq,cpu_max_freq, avg_temp, cpu_max_temp

# MULTI CORE AND SINGLE CORE MICRO BENCHMARK TESTING

# Monte carlo for single and multicore

def monte_carlo_pi(num_samples):
    print("monte carlo pi start")
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    print("monte carlo pi finished")
    print((inside_circle / num_samples) * 4)
    return (inside_circle / num_samples) * 4

def single_core_pi(num_samples):
    print("single core start")
    start_time = time.time()
    pi_estimate = monte_carlo_pi(num_samples)
    end_time = time.time()
    execution_time = end_time - start_time
    print("single core finished")
    print(pi_estimate, execution_time)
    return pi_estimate, execution_time

def multi_core_pi(num_samples, num_processes):
    print("multi core start")
    start_time = time.time()
    pool = multiprocessing.Pool(num_processes)
    num_samples_per_process = num_samples // num_processes
    results = pool.map(monte_carlo_pi, [num_samples_per_process] * num_processes)
    pi_estimate = sum(results) / num_processes
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    print("multi core finished")
    print(pi_estimate, execution_time)
    return pi_estimate, execution_time

def monte_carlo():
    print("monte carlo start")
    num_samples = 2*(10**7)
    num_processes = psutil.cpu_count(logical=False)
    single_core_result, single_core_time = single_core_pi(num_samples)
    multi_core_result, multi_core_time = multi_core_pi(num_samples, num_processes)
    print("monte carlo finished")
    print(single_core_result, single_core_time, multi_core_result, multi_core_time)
    return single_core_time, multi_core_time

# Matrix operation Single core and Multicore

def matrix_op(num_samples):
    print("matrix op start")
    A = np.random.rand(num_samples, num_samples)
    B = np.random.rand(num_samples, num_samples)
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions do not match for multiplication")
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    print("matrix op finished")
    return

def single_core_op(num_samples):
    print("single core matrix start")
    start_time = time.time()
    matrix_op(num_samples)
    end_time = time.time()
    execution_time = end_time - start_time
    print("single core matrix finished")
    print(execution_time)
    return execution_time

def multi_core_op(num_samples, num_processes):
    print("multi core matrix start")
    start_time = time.time()
    pool = multiprocessing.Pool(num_processes)
    num_samples_per_process = num_samples // num_processes
    results = pool.map(matrix_op , [num_samples_per_process] * num_processes)
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    print("multi core matrix finished")
    print(execution_time)
    return execution_time

def Mat_operation_check():
    print("matrix check start")
    num_samples = 300
    num_processes = psutil.cpu_count(logical=False)
    single_core_time = single_core_op(num_samples)
    multi_core_time = multi_core_op(num_samples, num_processes)
    print("matrix check finished")
    print(single_core_time, multi_core_time)
    return single_core_time, multi_core_time




# Image Processing and Rendering on single and Multicore

def image_ren_pro(num_samples):
    print("image start")
    image = Image.open(r'/home/soham/Coding_Adventures/OS/MinorProject/MinkBenchTake2/src/backend/benchmark/Large_image.jpg')
    for _ in range(num_samples):
        image = image.filter(ImageFilter.GaussianBlur(radius=10))
        image = image.rotate(30)
        image = image.convert('L')
        image = image.resize((2000,2000), Image.ANTIALIAS)
        def custom_filter(pixel):
            return pixel
        image = image.point(custom_filter)
    print("image finished")
    return

def single_core_ren(num_samples):
    print("single core image start")
    start_time = time.time()
    image_ren_pro(num_samples)
    end_time = time.time()
    execution_time = end_time - start_time
    print("single core image finished")
    print(execution_time)
    return execution_time

def multi_core_ren(num_samples, num_processes):
    print("multi core image start")
    start_time = time.time()
    pool = multiprocessing.Pool(num_processes)
    num_samples_per_process = num_samples // num_processes
    results = pool.map(image_ren_pro, [num_samples_per_process] * num_processes)
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    print("multi core image finished")
    print(execution_time)
    return execution_time


def Check_single_multi_image():
    print("image check start")
    num_samples = 100
    num_processes = psutil.cpu_count(logical=False)
    single_core_time = single_core_ren(num_samples)
    multi_core_time = multi_core_ren(num_samples, num_processes)
    print("image check finished")
    print(single_core_time, multi_core_time)    
    return single_core_time, multi_core_time

# Arithematics test for single and Multicore

def arith_call(num_samples):
    print("arith start")
    for i in range(num_samples):
        print(i)
        for x in range(1,100):
                3.141592 * 2**x
        for x in range(1,1000):
                float(x) / 3.141592
        for x in range(1,1000):
                float(3.141592) / x
    print("arith finished")
    return

def single_core_pro(num_samples):
    print("single core arith start")
    start_time = time.time()
    arith_call(num_samples)
    end_time = time.time()
    execution_time = end_time - start_time
    print("single core arith finished")
    print(execution_time)
    return execution_time

def multi_core_pro(num_samples, num_processes):
    print("multi core arith start")
    start_time = time.time()
    pool = multiprocessing.Pool(num_processes)
    num_samples_per_process = num_samples // num_processes
    results = pool.map(arith_call, [num_samples_per_process] * num_processes)
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    print("multi core arith finished")
    print(execution_time)
    return execution_time

def Arith_check():
    print("arith check start")
    num_samples = 5000
    num_processes = psutil.cpu_count(logical=False)
    single_core_time = single_core_pro(num_samples)
    multi_core_time = multi_core_pro(num_samples, num_processes)
    print("arith check finished")
    print(single_core_time, multi_core_time)
    return single_core_time, multi_core_time








# RUNNING SEPERATE TESTS AND FINAL SCORE CALCULATION FOR ALL TESTS

def scores_monte_carlo():
    mc_single_core_time, mc_multi_core_time = monte_carlo()
    mc_single_core_score = (1000/mc_single_core_time)*10
    mc_multi_core_score = (1000/mc_multi_core_time)*10
    #return int values of scores int()
    return int(mc_single_core_score), int(mc_multi_core_score)
    
    

# global scores_Mat_operation_check
def scores_Mat_operation_check():
    mt_single_core_time, mt_multi_core_time = Mat_operation_check()
    mt_single_core_score = (1000/mt_single_core_time)*10
    mt_multi_core_score = (1000/mt_multi_core_time)*10
    #
    return int(mt_single_core_score),int(mt_multi_core_score)

# global scores_Check_single_multi_image
def scores_Check_single_multi_image():
    img_single_core_time, img_multi_core_time = Check_single_multi_image()
    img_single_core_score = (1000/img_single_core_time)*10
    img_multi_core_score = (1000/img_multi_core_time)*10
    
    return int(img_single_core_score),int(img_multi_core_score)

# global scores_Arith_check
def scores_Arith_check():
    ar_single_core_time, ar_multi_core_time = Arith_check()
    ar_single_core_score = (1000/ar_single_core_time)*10
    ar_multi_core_score = (1000/ar_multi_core_time)*10
    return int(ar_single_core_score),int(ar_multi_core_score)




def scores_ml():
    global ml_temp_avg, ml_max_temp, ml_freq_avg, ml_max_freq
    # print("pehle",ml_max_temp)
    ml_exe, ml_freq_avg, ml_max_freq , ml_temp_avg, ml_max_temp = ml_train()
    # print("baad_me",ml_max_temp)
    ml_score = (1000/ml_exe)*(ml_freq_avg/ml_temp_avg)*500
    print("inside score_ml")
    print("ml_score : ",ml_score)
    print("ml_max_temp : ",ml_max_temp)
    print("ml_max_freq : ",ml_max_freq)
    print("ml_freq_avg : ",ml_freq_avg)
    print("ml_temp_avg : ",ml_temp_avg)
    return int(ml_score)

# global ar1_cpu_freq_avg, ar1_cpu_max_freq, ar1_cpu_temp_avg, ar1_cpu_max_temp
ar1_cpu_freq_avg = 0
ar1_cpu_max_freq = 0
ar1_cpu_temp_avg = 0
ar1_cpu_max_temp = 0
def scores_ar1():
    global ar1_cpu_freq_avg, ar1_cpu_max_freq, ar1_cpu_temp_avg, ar1_cpu_max_temp
    ar1_duration, ar1_cpu_freq_avg, ar1_cpu_max_freq, ar1_cpu_temp_avg, ar1_cpu_max_temp = Arith_test1()
    ar1_score = (1000/ar1_duration)*(ar1_cpu_freq_avg/ar1_cpu_temp_avg)*2000
    print("inside score_ar1")
    print("ar1_score : ",ar1_score)
    print("ar1_cpu_max_temp : ",ar1_cpu_max_temp)
    print("ar1_cpu_max_freq : ",ar1_cpu_max_freq)
    print("ar1_cpu_freq_avg : ",ar1_cpu_freq_avg)
    print("ar1_cpu_temp_avg : ",ar1_cpu_temp_avg)
    return int(ar1_score)

# global ar2_cpu_freq_avg, ar2_cpu_max_freq, ar2_cpu_temp_avg, ar2_cpu_max_temp 
ar2_cpu_freq_avg = 0
ar2_cpu_max_freq = 0
ar2_cpu_temp_avg = 0
ar2_cpu_max_temp = 0

def scores_ar2():
    global ar2_cpu_freq_avg, ar2_cpu_max_freq, ar2_cpu_temp_avg, ar2_cpu_max_temp 
    ar2_duration, ar2_cpu_freq_avg, ar2_cpu_max_freq, ar2_cpu_temp_avg, ar2_cpu_max_temp = Arith_test2()
    ar2_score = (1000/ar2_duration)*(ar2_cpu_freq_avg/ar2_cpu_temp_avg)*2000
    print("inside score_ar2")
    print("ar2_score : ",ar2_score)
    print("ar2_cpu_max_temp : ",ar2_cpu_max_temp)
    print("ar2_cpu_max_freq : ",ar2_cpu_max_freq)
    print("ar2_cpu_freq_avg : ",ar2_cpu_freq_avg)
    print("ar2_cpu_temp_avg : ",ar2_cpu_temp_avg)
    return int(ar2_score)

# global pdf_cpu_freq_avg, pdf_cpu_max_freq, pdf_cpu_temp_avg, pdf_cpu_max_temp

pdf_cpu_freq_avg = 0
pdf_cpu_max_freq = 0
pdf_cpu_temp_avg = 0
pdf_cpu_max_temp = 0
def score_pdf():
    global pdf_cpu_freq_avg, pdf_cpu_max_freq, pdf_cpu_temp_avg, pdf_cpu_max_temp
    pdf_render_pages_per_sec, pdf_cpu_freq_avg, pdf_cpu_max_freq, pdf_cpu_temp_avg, pdf_cpu_max_temp = pdf_text_render()
    pdf_score = pdf_render_pages_per_sec * (pdf_cpu_freq_avg/pdf_cpu_temp_avg)*2000
    print("inside score_pdf")
    print("pdf_score : ",pdf_score)
    print("pdf_cpu_max_temp : ",pdf_cpu_max_temp)
    print("pdf_cpu_max_freq : ",pdf_cpu_max_freq)
    print("pdf_cpu_freq_avg : ",pdf_cpu_freq_avg)
    print("pdf_cpu_temp_avg : ",pdf_cpu_temp_avg)
    return int(pdf_score)

# global pf_freq_avg, pf_temp_avg 
pf_freq_avg = 0
pf_temp_avg = 0
def score_prime():
    global pf_freq_avg, pf_temp_avg 
    pf_time_elapsed, pf_freq_avg, pf_temp_avg = Prime_calc()
    pf_score = (1000/pf_time_elapsed)*(pf_freq_avg/pf_temp_avg)*1500

    print("inside score_prime")
    print("pf_score : ",pf_score)
    print("pf_freq_avg : ",pf_freq_avg)
    print("pf_temp_avg : ",pf_temp_avg)
    return int(pf_score)



# global img_avg_freq, img_cpu_max_freq, img_avg_temp, img_cpu_max_temp
img_avg_freq = 0
img_cpu_max_freq = 0
img_avg_temp = 0
img_cpu_max_temp = 0

def score_img():
    global img_avg_freq, img_cpu_max_freq, img_avg_temp, img_cpu_max_temp
    img_duration, img_avg_freq, img_cpu_max_freq, img_avg_temp, img_cpu_max_temp = Image_processing()
    img_score = (1000/img_duration)*(img_avg_freq/img_avg_temp)*1500
    print("inside score_img")
    print("img_score : ",img_score)
    print("img_cpu_max_temp : ",img_cpu_max_temp)
    print("img_cpu_max_freq : ", img_cpu_max_freq)
    print("img_avg_freq : ",img_avg_freq)
    print("img_avg_temp : ",img_avg_temp)
    return int(img_score)

def extra_info():
    print("Calling extra info")
    print("ml_max_temp : ",ml_max_temp)
    print("ar1_cpu_max_temp : ",ar1_cpu_max_temp)
    print("ar2_cpu_max_temp : ",ar2_cpu_max_temp)
    print("pdf_cpu_max_temp : ",pdf_cpu_max_temp)
    print("img_cpu_max_temp : ",img_cpu_max_temp)
    print("------------------------------------------")
    print("ml_max_freq : ",ml_max_freq)
    print("ar1_cpu_max_freq : ",ar1_cpu_max_freq)
    print("ar2_cpu_max_freq : ",ar2_cpu_max_freq)
    print("pdf_cpu_max_freq : ",pdf_cpu_max_freq)
    print("img_cpu_max_freq : ",img_cpu_max_freq)
    print("------------------------------------------")
    benchmark_max_temp = max(ml_max_temp, ar1_cpu_max_temp, ar2_cpu_max_temp, pdf_cpu_max_temp, img_cpu_max_temp)
    benchmark_max_freq = max(ml_max_freq, ar1_cpu_max_freq, ar2_cpu_max_freq, pdf_cpu_max_freq,  img_cpu_max_freq)
    benchmark_avg_freq = (ml_freq_avg + ar1_cpu_freq_avg + ar2_cpu_freq_avg + pdf_cpu_freq_avg + pf_freq_avg  + img_avg_freq)/6
    benchmark_avg_temp = (ml_temp_avg + ar1_cpu_temp_avg + ar2_cpu_temp_avg + pdf_cpu_temp_avg + pf_temp_avg  + img_avg_temp)/6
    print("benchmark_max_temp : ",benchmark_max_temp)
    print("benchmark_avg_temp : ",benchmark_avg_temp)
    print("benchmark_max_freq : ",benchmark_max_freq)
    print("benchmark_avg_freq : ",benchmark_avg_freq)
    return round(benchmark_max_temp,1), round(benchmark_max_freq,2), round(benchmark_avg_freq,1), round(benchmark_avg_temp,1)



# def Main_benchmark():
#     print("main benchmark start")
#     b_start = time.time()
    
#     # Multi core Kernel benchmark tests
    
#     # ML Scoring
#     ml_exe, ml_freq_avg, ml_max_freq , ml_temp_avg, ml_max_temp = ml_train()
#     ml_score = (1000/ml_exe)*(ml_freq_avg/ml_temp_avg)*500
    
#     # Arithematic Operations Scoring
#     ar1_duration, ar1_cpu_freq_avg, ar1_cpu_max_freq, ar1_cpu_temp_avg, ar1_cpu_max_temp = Arith_test1()
#     ar1_score = (1000/ar1_duration)*(ar1_cpu_freq_avg/ar1_cpu_temp_avg)*2000
#     # Arithematic exponentiation Scoring
#     ar2_duration, ar2_cpu_freq_avg, ar2_cpu_max_freq, ar2_cpu_temp_avg, ar2_cpu_max_temp = Arith_test2()
#     ar2_score = (1000/ar2_duration)*(ar2_cpu_freq_avg/ar2_cpu_temp_avg)*2000
#     # PDF Rendering Scoring
#     pdf_render_pages_per_sec, pdf_cpu_freq_avg, pdf_cpu_max_freq, pdf_cpu_temp_avg, pdf_cpu_max_temp = pdf_text_render()
#     pdf_score = pdf_render_pages_per_sec * (pdf_cpu_freq_avg/pdf_cpu_temp_avg)*20
#     # Prime Factorization Scoring
#     pf_time_elapsed, pf_freq_avg, pf_temp_avg = Prime_calc()
#     pf_score = (1000/pf_time_elapsed)*(pf_freq_avg/pf_temp_avg)*1500
#     # Matrix Operations Scoring
#     # mo_duration, mo_avg_freq, mo_cpu_max_freq, mo_avg_temp, mo_cpu_max_temp = matrix_multiply()
#     # mo_score = (1000/mo_duration)*(mo_avg_freq/mo_avg_temp)*2000
#     mo_score = 0
#     # Image Processing and Rendering score
#     img_duration, img_avg_freq, img_cpu_max_freq, img_avg_temp, img_cpu_max_temp = Image_processing()
#     img_score = (1000/img_duration)*(img_avg_freq/img_avg_temp)*1500
    
    
    
#     total_k_benchmark_score = ml_score + ar1_score + ar2_score + pdf_score + pf_score + mo_score + img_score
    
    
#     # Multi core and Single core microbenchmark tests
    
#     # Monte Carlo Simulation
    
#     mc_single_core_time, mc_multi_core_time = monte_carlo()
#     mc_single_core_score = (1000/mc_single_core_time)*10
#     mc_multi_core_score = (1000/mc_multi_core_time)*10
    
#     # Matrix Score single core and Multi core
    
    
#     mt_single_core_time, mt_multi_core_time = Mat_operation_check()
#     mt_single_core_score = (1000/mt_single_core_time)*10
#     mt_multi_core_score = (1000/mt_multi_core_time)*10
    
#     # Image Rendering and Processing Multi core and Single core

        
#     img_single_core_time, img_multi_core_time = Check_single_multi_image()
#     img_single_core_score = (1000/img_single_core_time)*10
#     img_multi_core_score = (1000/img_multi_core_time)*10
    
#     # Arithmetic Operations Single core and multi core
    
        
#     ar_single_core_time, ar_multi_core_time = Arith_check()
#     ar_single_core_score = (1000/ar_single_core_time)*10
#     ar_multi_core_score = (1000/ar_multi_core_time)*10
    
#     total_single_core_score_micro = mc_single_core_score + mt_single_core_score + img_single_core_score + ar_single_core_score
#     total_multi_core_score_micro = mc_multi_core_score + mt_multi_core_score + img_multi_core_score + ar_multi_core_score
    
#     b_end = time.time()
    
#     benchmark_duration = b_end - b_start
#     benchmark_max_temp = max(ml_max_temp, ar1_cpu_max_temp, ar2_cpu_max_temp, pdf_cpu_max_temp, img_cpu_max_temp)
#     benchmark_max_freq = max(ml_max_freq, ar1_cpu_max_freq, ar2_cpu_max_freq, pdf_cpu_max_freq,  img_cpu_max_freq)
#     benchmark_avg_freq = (ml_freq_avg + ar1_cpu_freq_avg + ar2_cpu_freq_avg + pdf_cpu_freq_avg + pf_freq_avg  + img_avg_freq)/7
#     benchmark_avg_temp = (ml_temp_avg + ar1_cpu_temp_avg + ar2_cpu_temp_avg + pdf_cpu_temp_avg + pf_temp_avg  + img_avg_temp)/7
    
#     # Result1 = Single core scores [mc,mt,img,ar]
#     Result1 = [mc_single_core_score,mt_single_core_score,img_single_core_score,ar_single_core_score]
#     # Result2 = Multi core scores [mc,mt,img,ar]
#     Result2 = [mc_multi_core_score,mt_multi_core_score,img_multi_core_score,ar_multi_core_score]
#     # Result3 = Total Micro Benchmark score for single core
#     Result3 = total_single_core_score_micro
#     # Result4 = Total Micro Benchmark score for multi core
#     Result4 = total_multi_core_score_micro
    
#     # Result5 = Kernel Benchmark scores [ml,ar1,ar2,pdf,pf,mo,img]
#     Result5 = [ml_score,ar1_score,ar2_score,pdf_score,pf_score,mo_score,img_score]
#     # Result6 = Total Kernel benchmark score
#     Result6 = total_k_benchmark_score
    
#     print("main benchmark finished")
#     return Result1, Result2, Result3, Result4, Result5, Result6, benchmark_max_temp, benchmark_avg_temp, benchmark_max_freq, benchmark_avg_freq, benchmark_duration
    
    





# if __name__ == "__main__":
#     Result1, Result2, Result3, Result4, Result5, Result6, benchmark_max_temp, benchmark_avg_temp, benchmark_max_freq, benchmark_avg_freq, benchmark_duration = Main_benchmark()
#     print("Running Micro Benchmark Testing on single core ")
#     print("-----------------------------------------------")
#     print("Monte Carlo Score : ", Result1[0])
#     print("Matrix Score      : ", Result1[1])
#     print("Image Score       : ", Result1[2])
#     print("Arithematic Score : ", Result1[3])
#     print("")
#     print("")
#     print("Running Micro Benchmark Testing on multi core ")
#     print("-----------------------------------------------")
#     print("Monte Carlo Score : ", Result2[0])
#     print("Matrix Score      : ", Result2[1])
#     print("Image Score       : ", Result2[2])
#     print("Arithematic Score : ", Result2[3])
#     print("")
#     print("")
#     print("Micro Benchmark Score for Single core : ", Result3)
#     print("Micro Benchmark Score for multi core  : ", Result4)
#     print("-----------------------------------------------")
#     print("-----------------------------------------------")
#     print("-----------------------------------------------")
#     print("")
#     print("")
#     print("Running Kernel Benchmark Testing")
#     print("-----------------------------------------------")
#     print("ML Train Score          : ", Result5[0])
#     print("Arithematic1 Score      : ", Result5[1])
#     print("Arithematic2 Score      : ", Result5[2])
#     print("PDF Rendering Score     : ", Result5[3])
#     print("Prime Factor Score      : ", Result5[4])
#     # print("Matrix Op Score         : ", Result5[5])
#     print("IMG Processing Score    : ", Result5[6])
#     print("")
#     print("")
#     print("Kernel Benchmark Score final : ", Result6)
#     print("")
#     print("")
#     print("Extra Details..........")
#     print("Benchmark Max Temp.     : ",benchmark_max_temp)
#     print("Benchmark Avg Temp.     : ",benchmark_avg_temp)
#     print("Benchmark Max Freq.     : ",benchmark_max_freq)
#     print("Benchmark Avg Temp.     : ",benchmark_avg_freq)
#     print("Benchmark duration      : ",benchmark_duration)
    
# THANK YOU