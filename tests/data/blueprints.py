#!/usr/bin/env python3
"""Factorio blueprint examples"""

bps = {
    "constant_combinator": {
        "b64_str": (
            "0eNp9UNFOwzAM/Bc/pxOFdSyR9sJvoGlKSwBLjVMSt1pV5d9xMgGCB5QX5+zz3XmDfpzdFJEYzAY4BEpgnjdI+EZ2LBhZ78BA6bAlbo"
            "bgeyTLIUJWgPTirmDafFbgiJHR3RbUz3qh2fcuyoD6b5GCKSThBiqKsq9p2+OuU7CCeTzsOhESGscwXnr3bhcUjgwmNxRO+l2L+JcrB"
            "a84sot/UV6nYmXByLOk/PZ2S908CfIhDQkgIIXo65AYnmyshg2cKjCXu0l4ebmcANl5af4cVcEi8jVYd7jXe627Y/ug9d0+50/AVIAU"
        ),
        "bp": {
            "blueprint": {
                "icons": [{"signal": {"name": "constant-combinator"}, "index": 1}],
                "entities": [
                    {
                        "entity_number": 1,
                        "name": "constant-combinator",
                        "position": {"x": -118.5, "y": 76.5},
                        "control_behavior": {
                            "sections": {
                                "sections": [
                                    {
                                        "index": 1,
                                        "filters": [
                                            {
                                                "index": 1,
                                                "type": "virtual",
                                                "name": "signal-B",
                                                "quality": "normal",
                                                "comparator": "=",
                                                "count": 1,
                                            }
                                        ],
                                    }
                                ]
                            }
                        },
                    }
                ],
                "item": "blueprint",
                "version": 562949958139904,
            }
        },
    },
    "assembler": {
        "b64_str": (
            "0eNqtlm1vmzAQx7+LX22T6XiwWYO2F3u5zzBViIdLahVsaptsUcV33xkIoYVGTTIpiuDs+93Z//PhF5JXLTRaSEuSFyIKJQ1Jfr8QI3"
            "Yyq5xNZjWQhGTGQJ1XQu68OisehQQvIh0lQpbwlyRB90AJSCusgIHQvxxS2dY5aJxAz5IoaZRBZyVdTAe853eckgNJvt1xjIOZWa2qN"
            "IfHbC+UdtMKoYtW2BRklldQksTqFuhkRpdyQm6FNjZdLKvJND5Y0J5PhijGZm4zAt+91W7cumjk+zguobCpVWmldsJYUaQS7B+ln47R"
            "J/t/D48TNBSieet4NKfPbVbhnuOwVLrGQCiPhXrQQ5SzuLDdikKALA5ercq2gl7KYS5OlamQexRQ6cPge3pjlGCKBS7X7+g7I8G7I2H"
            "30OGPLsojnMojb6snT0gDGld3ri42WBcrpOjjJDYjUVIK3MZh/H6Fy+hJNGPEHrxGq70oUYLiEYw9l2rgr+fKJ6aG5xYh52BsDqNHj3"
            "QrKnTrdTND/qPe48GkZJrxyrqowACDrlTQqyr80RtaV6HeqHLPC1d44YW8cMaLVnjRhbxoxmMrPHYhj814fIXHL+TxGS9e4cUX8mI8W"
            "O500RNj0Nwe+paBDWCK8guPuusO5aIHTdPHGqXHh4QErtVsMY+2ypyfnxo0lNAALsKl4BrgjNAHfBPCFRl2fg0ldh/rqe37Cay5h7e5"
            "R7e5s9vc+W3u8cfdl9r1G3/SrhbyUxOkhqKIIviK//ZL5H8+K+cKNFxCwxEaXg2NltBohEZXQ9kSykYouxrKl1A+QvnV0HgJjUdofA7"
            "6MHzA3XdvutLhbSTLAS8c5Odw6epj7bEx9B8WHocbttnw+yDabHzWdf8AaJFP9Q=="
        ),
        "bp": {
            "blueprint": {
                "entities": [
                    {
                        "control_behavior": {
                            "circuit_condition": {
                                "comparator": "<",
                                "constant": 10,
                                "first_signal": {
                                    "name": "parameter-0",
                                },
                            },
                            "circuit_enabled": True,
                            "connect_to_logistic_network": True,
                            "logistic_condition": {
                                "comparator": "<",
                                "constant": 10,
                                "first_signal": {
                                    "name": "parameter-0",
                                },
                            },
                        },
                        "entity_number": 1,
                        "items": [
                            {
                                "id": {
                                    "name": "efficiency-module",
                                },
                                "items": {
                                    "in_inventory": [
                                        {
                                            "inventory": 4,
                                            "stack": 0,
                                        },
                                        {
                                            "inventory": 4,
                                            "stack": 1,
                                        },
                                        {
                                            "inventory": 4,
                                            "stack": 2,
                                        },
                                    ],
                                },
                            },
                        ],
                        "name": "assembling-machine-3",
                        "position": {
                            "x": 185.5,
                            "y": 7.5,
                        },
                        "recipe": "parameter-0",
                        "recipe_quality": "normal",
                    },
                    {
                        "entity_number": 2,
                        "name": "bulk-inserter",
                        "position": {
                            "x": 185.5,
                            "y": 9.5,
                        },
                    },
                    {
                        "direction": 8,
                        "entity_number": 3,
                        "name": "bulk-inserter",
                        "position": {
                            "x": 184.5,
                            "y": 9.5,
                        },
                    },
                    {
                        "entity_number": 4,
                        "name": "passive-provider-chest",
                        "position": {
                            "x": 185.5,
                            "y": 10.5,
                        },
                    },
                    {
                        "entity_number": 5,
                        "name": "requester-chest",
                        "position": {
                            "x": 184.5,
                            "y": 10.5,
                        },
                        "request_filters": {
                            "sections": [
                                {
                                    "filters": [
                                        {
                                            "comparator": "=",
                                            "count": -1,
                                            "index": 1,
                                            "name": "parameter-1",
                                            "quality": "normal",
                                        },
                                        {
                                            "comparator": "=",
                                            "count": -2,
                                            "index": 2,
                                            "name": "parameter-2",
                                            "quality": "normal",
                                        },
                                        {
                                            "comparator": "=",
                                            "count": -3,
                                            "index": 3,
                                            "name": "parameter-3",
                                            "quality": "normal",
                                        },
                                        {
                                            "comparator": "=",
                                            "count": -4,
                                            "index": 4,
                                            "name": "parameter-4",
                                            "quality": "normal",
                                        },
                                        {
                                            "comparator": "=",
                                            "count": -5,
                                            "index": 5,
                                            "name": "parameter-5",
                                            "quality": "normal",
                                        },
                                        {
                                            "comparator": "=",
                                            "count": -6,
                                            "index": 6,
                                            "name": "parameter-6",
                                            "quality": "normal",
                                        },
                                    ],
                                    "index": 1,
                                },
                            ],
                        },
                    },
                ],
                "icons": [
                    {
                        "index": 1,
                        "signal": {
                            "name": "assembling-machine-3",
                        },
                    },
                ],
                "item": "blueprint",
                "label": "Assembler",
                "parameters": [
                    {
                        "id": "parameter-0",
                        "name": "Item",
                        "type": "id",
                    },
                    {
                        "dependent": True,
                        "formula": "p0_s",
                        "number": "10",
                        "type": "number",
                    },
                    {
                        "id": "parameter-1",
                        "ingredient-of": "parameter-0",
                        "type": "id",
                    },
                    {
                        "id": "parameter-2",
                        "ingredient-of": "parameter-0",
                        "type": "id",
                    },
                    {
                        "id": "parameter-3",
                        "ingredient-of": "parameter-0",
                        "type": "id",
                    },
                    {
                        "id": "parameter-4",
                        "ingredient-of": "parameter-0",
                        "type": "id",
                    },
                    {
                        "id": "parameter-5",
                        "ingredient-of": "parameter-0",
                        "type": "id",
                    },
                    {
                        "id": "parameter-6",
                        "ingredient-of": "parameter-0",
                        "type": "id",
                    },
                    {
                        "dependent": True,
                        "formula": "min(p1_s,p0_i1/p0_t*30)",
                        "number": "-1",
                        "type": "number",
                    },
                    {
                        "dependent": True,
                        "formula": "min(p2_s,p0_i2/p0_t*30)",
                        "number": "-2",
                        "type": "number",
                    },
                    {
                        "dependent": True,
                        "formula": "min(p3_s,p0_i3/p0_t*30)",
                        "number": "-3",
                        "type": "number",
                    },
                    {
                        "dependent": True,
                        "formula": "min(p4_s,p0_i4/p0_t*30)",
                        "number": "-4",
                        "type": "number",
                    },
                    {
                        "dependent": True,
                        "formula": "min(p5_s,p0_i5/p0_t*30)",
                        "number": "-5",
                        "type": "number",
                    },
                    {
                        "dependent": True,
                        "formula": "min(p6_s,p0_i6/p0_t*30)",
                        "number": "-6",
                        "type": "number",
                    },
                ],
                "version": 562949958139904,
            },
        },
    },
}
