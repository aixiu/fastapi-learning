# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2024/04/23 10:57:45

from fastapi import APIRouter

shop = APIRouter()

@shop.get("/food")
def shop_food():
    return {"shop": "food"}

@shop.get("/bed")
def shop_food():
    return {"shop": "bed"}