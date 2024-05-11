# -*- coding: utf-8 -*-
"""
Created on Sat May 11 21:33:54 2024

@author: Administrator
"""

def say_hello():
  print("Hello , world!")
  
  
def sayhi():
    print('嗨，这是我的模块在讲话。')

__version__ = '0.1'  


import sys, platform, os
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from scipy import interpolate


def PlotDataTE(totCL):
    # 显示次刻度标签的位置,没有标签文本
    FitResult=totCL[:,3]
    xmax=2100
    yup=250 
    ydown=-250 
    ls = np.arange(totCL.shape[0])
    fig = plt.figure(figsize = (6,6))
    plt.rcParams['xtick.direction'] = 'in'#将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'#将y轴的刻度方向设置向内
    ###############插入整个大框架图
    left, bottom, width, height = 0.0,-0.3,1.4,1.1
    ax0 = fig.add_axes([left,bottom,width,height])
    plt.xticks([])
    plt.yticks([])
    #############################################插入图ax1############################
    left, bottom, width, height = 0.0,0.0,0.4,0.8
    datafit=np.delete(FitResult,[0,1],0)
    ls2=np.delete(ls,[0,1],0)
    ax1 = fig.add_axes([left,bottom,width,height])
    ax1.plot(ls2,datafit, 'k--')
    ax1.set_xlim([1.5,30])
    ax1.set_ylim([-30,30])
    plt.xscale('log')
    x_tick1 =[2,5,10,30]
    plt.xticks(x_tick1,fontsize=10,color='#000000')
    yminorLocator = MultipleLocator(2) 
    ax1.yaxis.set_minor_locator(yminorLocator) 
    plt.yticks([])
    y_tick1 =[-20,-10,0,10,20]
    plt.yticks(y_tick1,fontsize=10,color='#000000')
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-TE-full_R3.01.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    plt.errorbar(xs, ys, yerrs, fmt=".m", capsize=2, label=False,ecolor='orange')
    
    
    
    
    
    ##############################################################插入图ax2#############################################
    left, bottom, width, height = 0.4,0.0,1.0,0.8
    ax2 = fig.add_axes([left,bottom,width,height])
    ax2.plot(ls,FitResult, 'b--')
    ax2.set_xlim([30,xmax])
    plt.xscale('linear')
    x_tick2 =[500,1000,1500,2000]
    plt.xticks(x_tick2,fontsize=10,color='#000000')
    xminorLocator = MultipleLocator(100) 
    ax2.xaxis.set_minor_locator(xminorLocator)
    plt.xticks([])
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-TE-binned_R3.02.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    plt.errorbar(xs, ys, yerrs, fmt=".m", capsize=2, label= r'Planck2018',ecolor='orange')
    plt.legend(fontsize=14)  
    plt.yticks([])
    ax2x = ax2.twinx()
    ax2x.set_ylim([-160,160])
    yminorLocator = MultipleLocator(10) 
    ax2x.yaxis.set_minor_locator(yminorLocator)
    y_tick2=[-140,-70,0,70,140]
    plt.yticks(y_tick2,fontsize=10,color='#000000')
    
    
    ################################插入图ax3#############################################
    left, bottom, width, height = 0.0,-0.3,0.4,0.3
    datafit=np.delete(FitResult,[0,1],0)
    ls2=np.delete(ls,[0,1],0)
    ax3 = fig.add_axes([left,bottom,width,height])
    ax3.plot(ls2,0*datafit, 'k--')
    ax3.set_xlim([1.5,30])
    plt.xscale('log')
    x_tick3 =[2,5,10,30]
    plt.xticks(x_tick3,fontsize=10,color='#000000')
    ax3.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter()) 
    fun=interpolate.interp1d(ls,FitResult,kind="cubic")
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-TE-full_R3.01.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    plt.errorbar(xs, ys-fun(xs), yerrs, fmt=".m", capsize=2, label=None,ecolor='orange')
    ax3.set_ylim([-18,18])
    yminorLocator = MultipleLocator(2) 
    ax3.yaxis.set_minor_locator(yminorLocator) 
    plt.yticks([])
    y_tick3 =[-16,-8,0,8,16]
    plt.yticks(y_tick3,fontsize=10,color='#000000')
    
    
    
    ################################插入图ax4#############################################
    left, bottom, width, height = 0.4,-0.3,1.0,0.3
    ax4 = fig.add_axes([left,bottom,width,height])
    zeroline=0*FitResult
    ax4.plot(ls,zeroline, 'b--')
    ax4.set_xlim([30,xmax])
    plt.xscale('linear')

    ax4.set_ylim([-15,15])
    x_tick4 =[500,1000,1500,2000]
    plt.xticks(x_tick4,fontsize=10,color='#000000')
    xminorLocator = MultipleLocator(100) 
    ax4.xaxis.set_minor_locator(xminorLocator)
    plt.yticks([])

    fun=interpolate.interp1d(ls,FitResult,kind="cubic")
    ########导入binned后的数据
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-TE-binned_R3.02.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    plt.errorbar(xs, ys-fun(xs), yerrs, fmt=".m", capsize=2, label=None,ecolor='orange')
    plt.yticks([])
    ax4x = ax4.twinx()
    ax4x.set_ylim([-15,15])
    yminorLocator = MultipleLocator(2) 
    ax4x.yaxis.set_minor_locator(yminorLocator)
    y_tick4 =[-10,0,10]
    plt.yticks(y_tick4,fontsize=10,color='#000000')
    
    ax1.spines['right'].set_color('none')
    ax2.spines['left'].set_color('none')
    ax3.spines['right'].set_color('none')
    ax4.spines['left'].set_color('none')
    ax2x.spines['left'].set_color('none')
    ax4x.spines['left'].set_color('none')
    
    
    ax1y = ax1.twiny()  #generates second axis (top) 
    ax1y.set_xlim(ax1.get_xlim());  #same limits
    plt.xscale('log')  #make it log
    plt.xticks([])

    ax2y = ax2.twiny()
    ax2y.set_xlim([30,xmax])  
    yminorLocator = MultipleLocator(100) 
    ax2y.xaxis.set_minor_locator(yminorLocator)
    plt.xticks([])
    ax1y.spines['right'].set_color('none')
    ax2y.spines['left'].set_color('none')


    ax1.vlines([30],  ydown, yup,'black',linestyles='dashed')
    ax3.vlines([30], ydown,  yup,'k',linestyles='dashed')
    #############################设置坐标轴的label
    ax0.set_xlabel(r'$\ell$',labelpad =12,fontsize=13,loc='center')
    ax1.set_ylabel(r'$\mathcal{D}_\ell^{TE}\,[\mu {\rm K}^2]$',fontsize=13);
    ax3.set_ylabel(r'$\Delta\mathcal{D}_\ell^{TE}\,[\mu {\rm K}^2]$',fontsize=13);
#############################保存图片
    plt.savefig('CMB_TE_Plot.pdf',bbox_inches = 'tight')
    print("请查看保存的文件CMB_TE_Plot.pdf")
    plt.show()
    
    
    
def PlotDataTT(totCL):    
    #plot the total lensed CMB power spectra versus unlensed, and fractional difference
    FitResult=totCL[:,0]
    xmax=2510
    yup=6000 
    ydown=-6000
    ystep=100
    # 显示次刻度标签的位置,没有标签文本
##############################################################################################
    ls = np.arange(totCL.shape[0])
    fig = plt.figure(figsize = (6,6))

    plt.rcParams['xtick.direction'] = 'in'#将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'#将y轴的刻度方向设置向内
    ###############插入整个大框架图
    left, bottom, width, height = 0.0,-0.3,1.4,1.1
    ax0 = fig.add_axes([left,bottom,width,height])
    plt.xticks([])
    plt.yticks([])
    ##########################################################################插入图ax1#############################################
    left, bottom, width, height = 0.0,0.0,0.4,0.8
    datafit=np.delete(FitResult,[0,1],0)
    ls2=np.delete(ls,[0,1],0)
    ax1 = fig.add_axes([left,bottom,width,height])
    ax1.plot(ls2,datafit, 'k--')
    ax1.set_xlim([1.5,30])
    plt.xscale('log')
    
    x_tick1 =[2,5,10,30]
    plt.xticks(x_tick1,fontsize=10,color='#000000')
    #ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter()) 
    ax1.spines['right'].set_color('red')
 
    ########导入全l的数据
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-TT-full_R3.01.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    plt.errorbar(xs, ys, yerrs, fmt=".m", capsize=2, label=False,ecolor='orange')
    



##############################################################插入图ax2#############################################
    left, bottom, width, height = 0.4,0.0,1.0,0.8
    ax2 = fig.add_axes([left,bottom,width,height])
    ax2.plot(ls,FitResult, 'b--')
    ax2.set_xlim([30,xmax])
    #ax2.set_ylim([-150,150])
    plt.xscale('linear')

    x_tick2 =[500,1000,1500,2000]
    plt.xticks(x_tick2,fontsize=10,color='#000000')
    xminorLocator = MultipleLocator(100) 
    ax2.xaxis.set_minor_locator(xminorLocator)
    plt.xticks([])
    ax2.spines['left'].set_color('red')
    plt.yticks([])
    
        
########导入binned后的数据
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-TT-binned_R3.01.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    plt.errorbar(xs, ys, yerrs, fmt=".m", capsize=2, label= r'Planck2018',ecolor='orange')
    plt.legend(fontsize=14)  
    
################################插入图ax3#############################################
    left, bottom, width, height = 0.0,-0.3,0.4,0.3
    datafit=np.delete(FitResult,[0,1],0)
    ls2=np.delete(ls,[0,1],0)
    ax3 = fig.add_axes([left,bottom,width,height])
    ax3.plot(ls2,0*datafit, 'k--')
    ax3.set_xlim([1.5,30])
    plt.xscale('log')
    x_tick3 =[2,5,10,30]
    plt.xticks(x_tick3,fontsize=10,color='#000000')
    ax3.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter()) 

    ax3.set_ylim([-900,900])
    yminorLocator = MultipleLocator(100) 
    ax3.yaxis.set_minor_locator(yminorLocator) 
    #plt.yticks([])
    y_tick3 =[-600,-300,0,300,600]
    plt.yticks(y_tick3,fontsize=10,color='#000000')

    fun=interpolate.interp1d(ls,FitResult,kind="cubic")
    ########导入binned后的数据
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-TT-full_R3.01.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    plt.errorbar(xs, ys-fun(xs), yerrs, fmt=".m", capsize=2, label=None,ecolor='orange')


    ################################插入图ax4#############################################
    left, bottom, width, height = 0.4,-0.3,1.0,0.3
    ax4 = fig.add_axes([left,bottom,width,height])
    zeroline=0*FitResult
    ax4.plot(ls,zeroline, 'b--')
    ax4.set_xlim([30,xmax])
    plt.xscale('linear')
    x_tick4 =[500,1000,1500,2000]
    plt.xticks(x_tick4,fontsize=10,color='#000000')

    ax4.set_ylim([-75,75])
    xminorLocator = MultipleLocator(100) 
    ax4.xaxis.set_minor_locator(xminorLocator)
    plt.yticks([])

    fun=interpolate.interp1d(ls,FitResult,kind="cubic")
    ########导入binned后的数据
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-TT-binned_R3.01.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    plt.errorbar(xs, ys-fun(xs), yerrs, fmt=".m", capsize=2, label=None,ecolor='orange')
    plt.yticks([])


###########################################################
    ax1.set_ylim([-100,6000])
    ax2.set_ylim([-100,6000])  
    yminorLocator = MultipleLocator(200) 
    #ax1.yaxis.set_minor_locator(yminorLocator) 
    #ax2.yaxis.set_minor_locator(yminorLocator)
    plt.yticks([])
    xmajorLocator = MultipleLocator(1000)  # 将x主刻度标签设置为1000的倍数
    xmajorFormatter = FormatStrFormatter('%1.0f')  # 设置x轴标签文本的格式
    ax1.yaxis.set_major_locator(xmajorLocator)
    ax1.yaxis.set_major_formatter(xmajorFormatter)
    
    ax2x = ax2.twinx()
    ax2x.set_ylim([-100,6000])  
    yminorLocator = MultipleLocator(200) 
    ax2x.yaxis.set_minor_locator(yminorLocator)
    plt.yticks([])

    ax4x = ax4.twinx()
    ax4x.set_ylim([-75,75])
    yminorLocator = MultipleLocator(5) 
    ax4x.yaxis.set_minor_locator(yminorLocator)
    y_tick4x =[-60,-30,0,30,60]
    plt.yticks(y_tick4x,fontsize=10,color='#000000')

    ax1y = ax1.twiny()  #generates second axis (top) 
    ax1y.set_xlim(ax1.get_xlim());  #same limits
    plt.xscale('log')  #make it log
    plt.xticks([])

    ax2y = ax2.twiny()
    ax2y.set_xlim([30,xmax])  
    yminorLocator = MultipleLocator(100) 
    ax2y.xaxis.set_minor_locator(yminorLocator)
    plt.xticks([])


    #######################################################################################################################################
    ax1.spines['right'].set_color('none')
    ax2.spines['left'].set_color('none')
    ax3.spines['right'].set_color('none')
    ax4.spines['left'].set_color('none')
    ax2x.spines['left'].set_color('none')
    ax4x.spines['left'].set_color('none')

    ax1y.spines['right'].set_color('none')
    ax2y.spines['left'].set_color('none')

    ax1.vlines([30],  ydown, yup,'black',linestyles='dashed')
    ax3.vlines([30], ydown,  yup,'k',linestyles='dashed')
#############################设置坐标轴的label
    ax0.set_xlabel(r'$\ell$',labelpad =12,fontsize=13,loc='center')
    ax1.set_ylabel(r'$\mathcal{D}_\ell^{TT}\,[\mu {\rm K}^2]$',fontsize=13);
    ax3.set_ylabel(r'$\Delta\mathcal{D}_\ell^{TT}\,[\mu {\rm K}^2]$',fontsize=13);
    #############################保存图片
    plt.savefig('CMB_TT_Plot.pdf',bbox_inches = 'tight')
    print("请查看保存的文件CMB_TT_Plot.pdf")
    plt.show()


    
    
    
def PlotDataEE(totCL):  
#plot the total lensed CMB power spectra versus unlensed, and fractional difference
    FitResult=totCL[:,1]
    xmax=2100
    yup=250000 
    ydown=-250000 
# 显示次刻度标签的位置,没有标签文本
##############################################################################################
    ls = np.arange(totCL.shape[0])
    fig = plt.figure(figsize = (6,6))

    plt.rcParams['xtick.direction'] = 'in'#将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'#将y轴的刻度方向设置向内
    ###############插入整个大框架图
    left, bottom, width, height = 0.0,-0.3,1.4,1.1
    ax0 = fig.add_axes([left,bottom,width,height])
    plt.xticks([])
    plt.yticks([])

##########################################################################插入图ax1#############################################
    left, bottom, width, height = 0.0,0.0,0.4,0.8
    datafit=np.delete(FitResult,[0,1],0)
    ls2=np.delete(ls,[0,1],0)
    scale=ls2*(ls2+1)/2/np.pi*1e-5

    ax1 = fig.add_axes([left,bottom,width,height])
    ax1.plot(ls2,datafit/scale, 'k--')
    ax1.set_xlim([1.5,30])
    ax1.set_ylim([-7000,20000])
    plt.xscale('log')
    #x_tick = np.linspace(2,30,8)
    x_tick1 =[2,5,10,30]
    plt.xticks(x_tick1,fontsize=10,color='#000000')
    #ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter()) 
    ax1.spines['right'].set_color('red')
    

    yminorLocator = MultipleLocator(1000) 
    ax1.yaxis.set_minor_locator(yminorLocator) 
    plt.yticks([])
    y_tick1 =[0,5000,10000,15000]
    plt.yticks(y_tick1,fontsize=10,color='#000000')
        
        
########导入全l的数据
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-EE-full_R3.01.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    scale=xs*(xs+1)/2/np.pi*1e-5
    plt.errorbar(xs, ys/scale, yerrs/scale, fmt=".m", capsize=2, label=False,ecolor='orange')
    
##############################################################插入图ax2#############################################
    left, bottom, width, height = 0.4,0.0,1.0,0.8
    ax2 = fig.add_axes([left,bottom,width,height])
    ls2=np.delete(ls,[0,1],0)
    scale=ls2*(ls2+1)/2/np.pi*1e-5
    datafit=np.delete(FitResult,[0,1],0)
    ax2.plot(ls2,datafit/scale, 'b--')
    
    ax2.set_xlim([30,xmax])
    #ax2.set_ylim([-150,150])
    plt.xscale('linear')
    ax2.set_ylim([-20,120])
    

    x_tick2 =[500,1000,1500,2000]
    plt.xticks(x_tick2,fontsize=10,color='#000000')
    xminorLocator = MultipleLocator(100) 
    ax2.xaxis.set_minor_locator(xminorLocator)
    plt.xticks([])
    ax2.spines['left'].set_color('red')
    


    ########导入binned后的数据
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-EE-binned_R3.02.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    scale=xs*(xs+1)/2/np.pi*1e-5
    plt.errorbar(xs, ys/scale, yerrs/scale, fmt=".m", capsize=2, label= r'Planck2018',ecolor='orange')
    plt.legend(fontsize=14)  
    plt.yticks([])


    ax2x = ax2.twinx()
    ax2x.set_ylim([-20,120])
    yminorLocator = MultipleLocator(10) 
    ax2x.yaxis.set_minor_locator(yminorLocator)
    y_tick2=[0,20,40,60,80,100]
    plt.yticks(y_tick2,fontsize=10,color='#000000')

################################插入图ax3#############################################
    left, bottom, width, height = 0.0,-0.3,0.4,0.3
    datafit=np.delete(FitResult,[0,1],0)
    ls2=np.delete(ls,[0,1],0)
    ax3 = fig.add_axes([left,bottom,width,height])
    ax3.plot(ls2,0*datafit, 'k--')
    ax3.set_xlim([1.5,30])
    plt.xscale('log')

    #x_tick = np.linspace(2,30,8)
    x_tick3 =[2,5,10,30]
    plt.xticks(x_tick3,fontsize=10,color='#000000')
    ax3.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter()) 
    
    #############################################
    fun=interpolate.interp1d(ls,FitResult,kind="cubic")
    ########导入binned后的数据
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-EE-full_R3.01.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    scale=xs*(xs+1)/2/np.pi*1e-5
    plt.errorbar(xs,  (ys-fun(xs))/scale, yerrs/scale, fmt=".m", capsize=2, label=None,ecolor='orange')
    ax3.set_ylim([-200,200])
    yminorLocator = MultipleLocator(20) 
    ax3.yaxis.set_minor_locator(yminorLocator) 
    plt.yticks([])
    y_tick3 =[-100,0,100]
    plt.yticks(y_tick3,fontsize=10,color='#000000')


    ################################插入图ax4#############################################
    left, bottom, width, height = 0.4,-0.3,1.0,0.3
    ax4 = fig.add_axes([left,bottom,width,height])
    zeroline=0*FitResult
    ax4.plot(ls,zeroline, 'b--')
    ax4.set_xlim([30,xmax])
    plt.xscale('linear')

    ax4.set_ylim([-6,6])
    x_tick4 =[500,1000,1500,2000]
    plt.xticks(x_tick4,fontsize=10,color='#000000')
    xminorLocator = MultipleLocator(100) 
    ax4.xaxis.set_minor_locator(xminorLocator)
    plt.yticks([])
    

    fun=interpolate.interp1d(ls,FitResult,kind="cubic")
    ########导入binned后的数据
    file_name = 'planck2018TTTEEE/COM_PowerSpect_CMB-EE-binned_R3.02.txt'
    data=np.loadtxt(file_name, skiprows=0, usecols = (0,1,2,3), dtype=np.float32)
    xs=data[:,0]
    ys=data[:,1]
    yerrs=data[:,(2,3)].T
    scale=xs*(xs+1)/2/np.pi*1e-5
    plt.errorbar(xs, (ys-fun(xs))/scale, yerrs/scale, fmt=".m", capsize=2, label=None,ecolor='orange')
    plt.yticks([])
        
    ax4x = ax4.twinx()
    ax4x.set_ylim([-6,6])
    yminorLocator = MultipleLocator(2) 
    ax4x.yaxis.set_minor_locator(yminorLocator)
    y_tick4 =[-4,0,4]
    plt.yticks(y_tick4,fontsize=10,color='#000000')

#######################################################################################################################################
    ax1y = ax1.twiny()  #generates second axis (top) 
    ax1y.set_xlim(ax1.get_xlim());  #same limits
    plt.xscale('log')  #make it log
    plt.xticks([])
    
    ax2y = ax2.twiny()
    ax2y.set_xlim([30,xmax])  
    yminorLocator = MultipleLocator(100) 
    ax2y.xaxis.set_minor_locator(yminorLocator)
    plt.xticks([])

    #######################################################################################################################################
    ax1.spines['right'].set_color('none')
    ax2.spines['left'].set_color('none')
    ax3.spines['right'].set_color('none')
    ax4.spines['left'].set_color('none')

    #ax1x.spines['right'].set_color('none')
    ax2x.spines['left'].set_color('none')
    #ax3x.spines['right'].set_color('none')
    ax4x.spines['left'].set_color('none')
    ax1y.spines['right'].set_color('none')
    ax2y.spines['left'].set_color('none')

    ax1.vlines([30],  ydown, yup,'black',linestyles='dashed')
    ax3.vlines([30], ydown,  yup,'k',linestyles='dashed')
    #############################设置坐标轴的label
    ax0.set_xlabel(r'$\ell$',labelpad =12,fontsize=13,loc='center')
    ax1.set_ylabel(r'$\mathcal{C}_\ell^{EE}\,[10^{-5}\mu {\rm K}^2]$',fontsize=13);
    ax3.set_ylabel(r'$\Delta\mathcal{C}_\ell^{EE}\,[10^{-5} \mu {\rm K}^2]$',fontsize=13);
#############################保存图片
    plt.savefig('CMB_EE_Plot.pdf',bbox_inches = 'tight')
    print("请查看保存的文件CMB_EE_Plot.pdf")
    plt.show()
    




