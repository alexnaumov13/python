#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from array import array
import unicodedata
import time
import re


def write(string):
    f = open('break.txt', 'a')
    f.write(string)
    f.close()


def stats1():
    aces = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[1]/div[1]/div[1]/div').text
    double_faults = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[1]/div[2]/div[1]/div').text
    serve1 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[1]/div[3]/div[1]/div').text
    serve1 = serve1[serve1.find('(') + 1:]
    serve1 = serve1[:serve1.find(')') - 1]
    serve2 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[1]/div[4]/div[1]/div').text
    serve2 = serve2[serve2.find('(') + 1:]
    serve2 = serve2[:serve2.find(')') - 1]
    ptswon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[1]/div[1]/div').text
    bpcount = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[2]/div[1]/div').text
    bpcount = bpcount[:bpcount.find('/')]
    bppr = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[2]/div[1]/div').text
    bppr = bppr[bppr.find('(') + 1:]
    bppr = bppr[:bppr.find(')') - 1]
    pts1serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[3]/div[1]/div').text
    pts1serve = pts1serve[pts1serve.find('(') + 1:]
    pts1serve = pts1serve[:pts1serve.find(')') - 1]
    pts2serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[4]/div[1]/div').text
    pts2serve = pts2serve[pts2serve.find('(') + 1:]
    pts2serve = pts2serve[:pts2serve.find(')') - 1]
    maxpoint = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[5]/div[1]/div').text
    pointwon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[6]/div[1]/div').text
    write(
        aces + ',' + double_faults + ',' + serve1 + ',' + serve2 + ',' + ptswon + ',' + bpcount + ',' + bppr + ',' + pts1serve + ',' + pts2serve + ',' + maxpoint + ',' + pointwon + ',')
    #####  second player#####
    aces = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[1]/div[1]/div[3]/div').text
    double_faults = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[1]/div[2]/div[3]/div').text
    serve1 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[1]/div[3]/div[3]/div').text
    serve1 = serve1[serve1.find('(') + 1:]
    serve1 = serve1[:serve1.find(')') - 1]
    serve2 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[1]/div[4]/div[3]/div').text
    serve2 = serve2[serve2.find('(') + 1:]
    serve2 = serve2[:serve2.find(')') - 1]
    ptswon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[1]/div[3]/div').text
    bpcount = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[2]/div[3]/div').text
    bpcount = bpcount[:bpcount.find('/')]
    bppr = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[2]/div[3]/div').text
    bppr = bppr[bppr.find('(') + 1:]
    bppr = bppr[:bppr.find(')') - 1]
    pts1serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[3]/div[3]/div').text
    pts1serve = pts1serve[pts1serve.find('(') + 1:]
    pts1serve = pts1serve[:pts1serve.find(')') - 1]
    pts2serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[4]/div[3]/div').text
    pts2serve = pts2serve[pts2serve.find('(') + 1:]
    pts2serve = pts2serve[:pts2serve.find(')') - 1]
    maxpoint = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[5]/div[3]/div').text
    pointwon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[2]/div[2]/div[6]/div[3]/div').text
    write(
        aces + ',' + double_faults + ',' + serve1 + ',' + serve2 + ',' + ptswon + ',' + bpcount + ',' + bppr + ',' + pts1serve + ',' + pts2serve + ',' + maxpoint + ',' + pointwon)


def stats2():
    aces = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[1]/div[1]/div[1]/div').text
    double_faults = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[1]/div[2]/div[1]/div').text
    serve1 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[1]/div[3]/div[1]/div').text
    serve1 = serve1[serve1.find('(') + 1:]
    serve1 = serve1[:serve1.find(')') - 1]
    serve2 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[1]/div[4]/div[1]/div').text
    serve2 = serve2[serve2.find('(') + 1:]
    serve2 = serve2[:serve2.find(')') - 1]
    ptswon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[1]/div[1]/div').text
    bpcount = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[2]/div[1]/div').text
    bpcount = bpcount[:bpcount.find('/')]
    bppr = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[2]/div[1]/div').text
    bppr = bppr[bppr.find('(') + 1:]
    bppr = bppr[:bppr.find(')') - 1]
    pts1serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[3]/div[1]/div').text
    pts1serve = pts1serve[pts1serve.find('(') + 1:]
    pts1serve = pts1serve[:pts1serve.find(')') - 1]
    pts2serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[4]/div[1]/div').text
    pts2serve = pts2serve[pts2serve.find('(') + 1:]
    pts2serve = pts2serve[:pts2serve.find(')') - 1]
    maxpoint = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[5]/div[1]/div').text
    pointwon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[6]/div[1]/div').text
    write(
        aces + ',' + double_faults + ',' + serve1 + ',' + serve2 + ',' + ptswon + ',' + bpcount + ',' + bppr + ',' + pts1serve + ',' + pts2serve + ',' + maxpoint + ',' + pointwon + ',')
    #####  second player#####
    aces = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[1]/div[1]/div[3]/div').text
    double_faults = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[1]/div[2]/div[3]/div').text
    serve1 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[1]/div[3]/div[3]/div').text
    serve1 = serve1[serve1.find('(') + 1:]
    serve1 = serve1[:serve1.find(')') - 1]
    serve2 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[1]/div[4]/div[3]/div').text
    serve2 = serve2[serve2.find('(') + 1:]
    serve2 = serve2[:serve2.find(')') - 1]
    ptswon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[1]/div[3]/div').text
    bpcount = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[2]/div[3]/div').text
    bpcount = bpcount[:bpcount.find('/')]
    bppr = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[2]/div[3]/div').text
    bppr = bppr[bppr.find('(') + 1:]
    bppr = bppr[:bppr.find(')') - 1]
    pts1serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[3]/div[3]/div').text
    pts1serve = pts1serve[pts1serve.find('(') + 1:]
    pts1serve = pts1serve[:pts1serve.find(')') - 1]
    pts2serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[4]/div[3]/div').text
    pts2serve = pts2serve[pts2serve.find('(') + 1:]
    pts2serve = pts2serve[:pts2serve.find(')') - 1]
    maxpoint = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[5]/div[3]/div').text
    pointwon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[3]/div[2]/div[6]/div[3]/div').text
    write(
        aces + ',' + double_faults + ',' + serve1 + ',' + serve2 + ',' + ptswon + ',' + bpcount + ',' + bppr + ',' + pts1serve + ',' + pts2serve + ',' + maxpoint + ',' + pointwon)


def stats3():
    aces = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[1]/div[1]/div[1]/div').text
    double_faults = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[1]/div[2]/div[1]/div').text
    serve1 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[1]/div[3]/div[1]/div').text
    serve1 = serve1[serve1.find('(') + 1:]
    serve1 = serve1[:serve1.find(')') - 1]
    serve2 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[1]/div[4]/div[1]/div').text
    serve2 = serve2[serve2.find('(') + 1:]
    serve2 = serve2[:serve2.find(')') - 1]
    ptswon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[1]/div[1]/div').text
    bpcount = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[2]/div[1]/div').text
    bpcount = bpcount[:bpcount.find('/')]
    bppr = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[2]/div[1]/div').text
    bppr = bppr[bppr.find('(') + 1:]
    bppr = bppr[:bppr.find(')') - 1]
    pts1serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[3]/div[1]/div').text
    pts1serve = pts1serve[pts1serve.find('(') + 1:]
    pts1serve = pts1serve[:pts1serve.find(')') - 1]
    pts2serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[4]/div[1]/div').text
    pts2serve = pts2serve[pts2serve.find('(') + 1:]
    pts2serve = pts2serve[:pts2serve.find(')') - 1]
    maxpoint = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[5]/div[1]/div').text
    pointwon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[6]/div[1]/div').text
    write(
        aces + ',' + double_faults + ',' + serve1 + ',' + serve2 + ',' + ptswon + ',' + bpcount + ',' + bppr + ',' + pts1serve + ',' + pts2serve + ',' + maxpoint + ',' + pointwon + ',')
    #####  second player#####
    aces = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[1]/div[1]/div[3]/div').text
    double_faults = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[1]/div[2]/div[3]/div').text
    serve1 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[1]/div[3]/div[3]/div').text
    serve1 = serve1[serve1.find('(') + 1:]
    serve1 = serve1[:serve1.find(')') - 1]
    serve2 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[1]/div[4]/div[3]/div').text
    serve2 = serve2[serve2.find('(') + 1:]
    serve2 = serve2[:serve2.find(')') - 1]
    ptswon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[1]/div[3]/div').text
    bpcount = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[2]/div[3]/div').text
    bpcount = bpcount[:bpcount.find('/')]
    bppr = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[2]/div[3]/div').text
    bppr = bppr[bppr.find('(') + 1:]
    bppr = bppr[:bppr.find(')') - 1]
    pts1serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[3]/div[3]/div').text
    pts1serve = pts1serve[pts1serve.find('(') + 1:]
    pts1serve = pts1serve[:pts1serve.find(')') - 1]
    pts2serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[4]/div[3]/div').text
    pts2serve = pts2serve[pts2serve.find('(') + 1:]
    pts2serve = pts2serve[:pts2serve.find(')') - 1]
    maxpoint = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[5]/div[3]/div').text
    pointwon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[4]/div[2]/div[6]/div[3]/div').text
    write(
        aces + ',' + double_faults + ',' + serve1 + ',' + serve2 + ',' + ptswon + ',' + bpcount + ',' + bppr + ',' + pts1serve + ',' + pts2serve + ',' + maxpoint + ',' + pointwon)


def stats4():
    aces = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[1]/div[1]/div[1]/div').text
    double_faults = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[1]/div[2]/div[1]/div').text
    serve1 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[1]/div[3]/div[1]/div').text
    serve1 = serve1[serve1.find('(') + 1:]
    serve1 = serve1[:serve1.find(')') - 1]
    serve2 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[1]/div[4]/div[1]/div').text
    serve2 = serve2[serve2.find('(') + 1:]
    serve2 = serve2[:serve2.find(')') - 1]
    ptswon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[1]/div[1]/div').text
    bpcount = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[2]/div[1]/div').text
    bpcount = bpcount[:bpcount.find('/')]
    bppr = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[2]/div[1]/div').text
    bppr = bppr[bppr.find('(') + 1:]
    bppr = bppr[:bppr.find(')') - 1]
    pts1serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[3]/div[1]/div').text
    pts1serve = pts1serve[pts1serve.find('(') + 1:]
    pts1serve = pts1serve[:pts1serve.find(')') - 1]
    pts2serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[4]/div[1]/div').text
    pts2serve = pts2serve[pts2serve.find('(') + 1:]
    pts2serve = pts2serve[:pts2serve.find(')') - 1]
    maxpoint = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[5]/div[1]/div').text
    pointwon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[6]/div[1]/div').text
    write(
        aces + ',' + double_faults + ',' + serve1 + ',' + serve2 + ',' + ptswon + ',' + bpcount + ',' + bppr + ',' + pts1serve + ',' + pts2serve + ',' + maxpoint + ',' + pointwon + ',')
    #####  second player#####
    aces = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[1]/div[1]/div[3]/div').text
    double_faults = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[1]/div[2]/div[3]/div').text
    serve1 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[1]/div[3]/div[3]/div').text
    serve1 = serve1[serve1.find('(') + 1:]
    serve1 = serve1[:serve1.find(')') - 1]
    serve2 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[1]/div[4]/div[3]/div').text
    serve2 = serve2[serve2.find('(') + 1:]
    serve2 = serve2[:serve2.find(')') - 1]
    ptswon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[1]/div[3]/div').text
    bpcount = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[2]/div[3]/div').text
    bpcount = bpcount[:bpcount.find('/')]
    bppr = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[2]/div[3]/div').text
    bppr = bppr[bppr.find('(') + 1:]
    bppr = bppr[:bppr.find(')') - 1]
    pts1serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[3]/div[3]/div').text
    pts1serve = pts1serve[pts1serve.find('(') + 1:]
    pts1serve = pts1serve[:pts1serve.find(')') - 1]
    pts2serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[4]/div[3]/div').text
    pts2serve = pts2serve[pts2serve.find('(') + 1:]
    pts2serve = pts2serve[:pts2serve.find(')') - 1]
    maxpoint = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[5]/div[3]/div').text
    pointwon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[5]/div[2]/div[6]/div[3]/div').text
    write(
        aces + ',' + double_faults + ',' + serve1 + ',' + serve2 + ',' + ptswon + ',' + bpcount + ',' + bppr + ',' + pts1serve + ',' + pts2serve + ',' + maxpoint + ',' + pointwon)


def stats5():
    aces = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[1]/div[1]/div[1]/div').text
    double_faults = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[1]/div[2]/div[1]/div').text
    serve1 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[1]/div[3]/div[1]/div').text
    serve1 = serve1[serve1.find('(') + 1:]
    serve1 = serve1[:serve1.find(')') - 1]
    serve2 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[1]/div[4]/div[1]/div').text
    serve2 = serve2[serve2.find('(') + 1:]
    serve2 = serve2[:serve2.find(')') - 1]
    ptswon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[1]/div[1]/div').text
    bpcount = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[2]/div[1]/div').text
    bpcount = bpcount[:bpcount.find('/')]
    bppr = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[2]/div[1]/div').text
    bppr = bppr[bppr.find('(') + 1:]
    bppr = bppr[:bppr.find(')') - 1]
    pts1serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[3]/div[1]/div').text
    pts1serve = pts1serve[pts1serve.find('(') + 1:]
    pts1serve = pts1serve[:pts1serve.find(')') - 1]
    pts2serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[4]/div[1]/div').text
    pts2serve = pts2serve[pts2serve.find('(') + 1:]
    pts2serve = pts2serve[:pts2serve.find(')') - 1]
    maxpoint = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[5]/div[1]/div').text
    pointwon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[6]/div[1]/div').text
    write(
        aces + ',' + double_faults + ',' + serve1 + ',' + serve2 + ',' + ptswon + ',' + bpcount + ',' + bppr + ',' + pts1serve + ',' + pts2serve + ',' + maxpoint + ',' + pointwon + ',')
    #####  second player#####
    aces = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[1]/div[1]/div[3]/div').text
    double_faults = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[1]/div[2]/div[3]/div').text
    serve1 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[1]/div[3]/div[3]/div').text
    serve1 = serve1[serve1.find('(') + 1:]
    serve1 = serve1[:serve1.find(')') - 1]
    serve2 = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[1]/div[4]/div[3]/div').text
    serve2 = serve2[serve2.find('(') + 1:]
    serve2 = serve2[:serve2.find(')') - 1]
    ptswon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[1]/div[3]/div').text
    bpcount = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[2]/div[3]/div').text
    bpcount = bpcount[:bpcount.find('/')]
    bppr = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[2]/div[3]/div').text
    bppr = bppr[bppr.find('(') + 1:]
    bppr = bppr[:bppr.find(')') - 1]
    pts1serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[3]/div[3]/div').text
    pts1serve = pts1serve[pts1serve.find('(') + 1:]
    pts1serve = pts1serve[:pts1serve.find(')') - 1]
    pts2serve = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[4]/div[3]/div').text
    pts2serve = pts2serve[pts2serve.find('(') + 1:]
    pts2serve = pts2serve[:pts2serve.find(')') - 1]
    maxpoint = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[5]/div[3]/div').text
    pointwon = driver.find_element_by_xpath(
        '/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/div/div[6]/div[2]/div[6]/div[3]/div').text
    write(
        aces + ',' + double_faults + ',' + serve1 + ',' + serve2 + ',' + ptswon + ',' + bpcount + ',' + bppr + ',' + pts1serve + ',' + pts2serve + ',' + maxpoint + ',' + pointwon)


def set_stats(current_set):
    if current_set == 0:
        try:
            a = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/ul/li[2]/a')
            a.click()
            stats1()
        except NoSuchElementException:
            write('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
            print('Нет статы')
    elif current_set == 1:
        try:
            a = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/ul/li[3]/a')
            a.click()
            stats2()
        except NoSuchElementException:
            write('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
            print('Нет статы')
    elif current_set == 2:
        try:
            a = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/ul/li[4]/a')
            a.click()
            stats3()
        except NoSuchElementException:
            write('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
            print('Нет статы')
    elif current_set == 3:
        try:
            a = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/ul/li[5]/a')
            a.click()
            stats4()
        except NoSuchElementException:
            write('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
            print('Нет статы')
    elif current_set == 4:
        try:
            a = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[9]/div/ul/li[6]/a')
            a.click()
            stats5()
        except NoSuchElementException:
            write('0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
            print('Нет статы')


def players_tournament():
    ##### Tournament####
    tournament = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[2]/a')
    a = tournament.text
    if a == 'Кубок Дэвиса':
        write('1,12,')
    if a == 'Кубок Федераций':
        write('2,12,')
    if a == 'Кубок Хопмана':
        write('3,12,')
    if a == 'Challenger':
        write('4,1,')
    if a == 'Challenger Women':
        write('5,2,')
    if a == 'ATP':
        write('6,1,')
    if a == 'ITF Women':
        write('7,2,')
    if a == 'ITF Men':
        write('8,1,')
    if a == 'WTA':
        write('9,2,')
    ######## Doubles    1-yes 2-no
    doubles_singles_mixed = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/ul/li[3]/a').text
    singles = doubles_singles_mixed.find('Singles')
    doubles = doubles_singles_mixed.find('Doubles')
    mixed = doubles_singles_mixed.find('Mixed')
    if doubles != -1:
        write('1,')
    if mixed != -1:
        write('2,')
    else:
        write('0,')


######   1 - мужчины, 2 - женщины, 12-непонятные
########players
'''        players = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/h2/span[2]')
        b = players.text
        c = b.split(' - ')
        k = unicodedata.normalize('NFKD', c[0]).encode('ascii', 'ignore')
        k1 = unicodedata.normalize('NFKD', c[1]).encode('ascii', 'ignore')
        l = str(k)
        l1 = str(k1)
        c[0] = l[2:len(l)-1]
        c[1] = l1[2:len(l)-1]
        write(c[0]+','+c[1]+',')

'''


def coefficients():
    ########  Coefficients + Favorite
    try:
        cf1 = driver.find_element_by_xpath(
            'html/body/div[5]/div/div[2]/div/div[1]/div[11]/div/div/div[1]/table/tbody/tr/td[1]/a/div/span[1]/span[1]').text
        write(cf1 + ',')
        try:
            cf2 = driver.find_element_by_xpath(
                'html/body/div[5]/div/div[2]/div/div[1]/div[11]/div/div/div[1]/table/tbody/tr/td[2]/a/div/span[1]/span[1]').text
            write(cf2 + ',')
            if float(cf1) < float(cf2):
                write('1,')
            else:
                write('2,')
        except NoSuchElementException:
            print('1')
    except NoSuchElementException:
        try:
            rt1 = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div/div[1]/div[10]/div/div/div/div[1]/div[2]/span').text
            rt1 = rt1[:len(rt1) - 1]
            write('0,')
            try:
                rt2 = driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div[2]/div/div[1]/div[10]/div/div/div/div[2]/div[2]/span').text
                rt2 = rt2[:len(rt1) - 1]
                write('0,')
                if float(rt1) < float(rt2):
                    write('1,')
                else:
                    write('2,')
            except NoSuchElementException:
                print('1')
        except NoSuchElementException:
            print('2')


def all_together(i):
    l = 0
    p1 = [0, 0, 0, 0, 0]
    p2 = [0, 0, 0, 0, 0]
    for i in range(1, 6):
        try:
            p1[i - 1] = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div/div[1]/div[7]/div/div/table/tbody/tr/td[%s]/span[1]' % i).text
            p2[i - 1] = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div/div[1]/div[7]/div/div/table/tbody/tr/td[%s]/span[2]' % i).text
        except NoSuchElementException:
            break
    for i in range(len(p1)):
        if len(str(p1[i])) > 1:
            p1[i] = p1[i][:1]
    for i in range(len(p2)):
        if len(str(p2[i])) > 1:
            p2[i] = p2[i][:1]
    for i in range(0, len(p1)):
        if p1[i] != '':
            l = l + 1
    del p1[l:]
    del p2[l:]
    for i in range(0, len(p1)):
        if int(p1[i]) + int(p2[i]) == 12:
            if int(p1[i]) > int(p2[i]):
                write('1,0,')
            # print(str(i)+'1')
            else:
                write('2,0,')
            # print(str(i)+'2')
            write(str(i + 1) + ',')
            players_tournament()
            set_stats(i)
            write('\n')
        # print(str(i)+'3')
        elif int(p1[i]) + int(p2[i]) == 13:
            if int(p1[i]) > int(p2[i]):
                write('1,1,')
            # print(str(i)+'4')
            else:
                write('2,1,')
            # print(str(i)+'5')
            write(str(i + 1) + ',')
            players_tournament()
            set_stats(i)
            write('\n')
        # print(str(i)+'6')


def serve():
    l = 0
    p1 = [0, 0, 0, 0, 0]
    p2 = [0, 0, 0, 0, 0]
    for i in range(1, 6):
        try:
            p1[i - 1] = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div/div[1]/div[7]/div/div/table/tbody/tr/td[%s]/span[1]' % i).text
            p2[i - 1] = driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/div/div[1]/div[7]/div/div/table/tbody/tr/td[%s]/span[2]' % i).text
        except NoSuchElementException:
            break
    for i in range(len(p1)):
        if len(str(p1[i])) > 1:
            p1[i] = p1[i][:1]
    for i in range(len(p2)):
        if len(str(p2[i])) > 1:
            p2[i] = p2[i][:1]
    for i in range(0, len(p1)):
        if p1[i] != '':
            l = l + 1
    del p1[l:]
    del p2[l:]
    bp = []
    bp_count = 0
    i = 1
    cmbp = 0
    el = driver.find_elements_by_class_name('pbp__setcell')

    for i in range(2, len(el) + len(p1) + 1):
        for j in range(1, 3):
            try:
                temp = driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div[2]/div/div[1]/div[8]/div/div/div[%s]/div[1]/div[%s]' % (
                    i, j)).get_attribute("class")
                if temp.find('orange') != -1:
                    bp.append('1')
                    bp_count = bp_count + 1
                else:
                    bp.append('0')
            except NoSuchElementException:
                continue
    i = 1
    for i in range(len(p1)):
        for j in range(0, int(p1[i]) + int(p2[i])):
            if bp[i] == bp[i - 1]:
                cmbp = cmbp + 1


driver = webdriver.Chrome('/Users/Максим/Desktop/chromedriver')
# driver.get('http://myscore.ru/tennis')
driver.get('https://www.sofascore.com/ru/tennis')
driver.implicitly_wait(10)
a = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div/div[1]/a")
time.sleep(5)
a.click()
driver.implicitly_wait(10)
# a = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div[1]/div/table/tbody/tr[4]/td[2]/a')
# time.sleep(5)
# a.click()
# driver.implicitly_wait(10)
proverka = input()
if proverka == 'y':
    print('go')
elements = driver.find_elements_by_xpath(
    '//div[@class="event-list-table-wrapper js-event-list-table-wrapper"]/div[@class = "js-event-list-tournament tournament"]/div[@class = "js-event-list-tournament-events"]/a')
ids = []
for i in range(len(elements)):
    ids.append(elements[i].get_attribute('href'))
print(ids)

for i in range(0, len(ids)):
    driver.get(ids[i])
    try:
        driver.find_element_by_class_name("statistics-container")
        all_together(i)
        print(i)
    except NoSuchElementException:
        print(i)