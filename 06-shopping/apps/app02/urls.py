# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2024/04/23 11:08:25

from fastapi import APIRouter

user = APIRouter()

@user.post("/login")
def shop_food():
    return {"shop": "login"}

@user.post("/reg")
def shop_food():
    return {"shop": "reg"}