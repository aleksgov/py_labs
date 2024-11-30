class Config:
    current_lab = 1

    config = {
        1 : {
            "header" : "Лабораторная работа №1",
            "variants_path": "documentation/FirstLab/Variants.html",
            "variants_count" : 19,
            "theory_path" : "documentation/FirstLab/FirstTheory.html",
            "example" : {
                "steps_count": 3,
                "steps_counters" : ["1-ый", "2-ой", "3-ий"],
                "steps_headers" : ["Определение параметров и постановка задачи",
                                   "Создание модели СМО на GPSS",
                                   "Анализ результатов моделирования"],
                "steps_paths" : ["documentation/FirstLab/FirstExample.html",
                                 "documentation/FirstLab/SecondExample.html",
                                 "documentation/FirstLab/ThirdExample.html"]
            }
        },
        2 : {
            "header" : "Лабораторная работа №2",
            "variants_path": "documentation/FirstLab/Variants.html",
            "variants_count" : 16,
            "theory_path" : "documentation/SecondLab/SecondTheory.html",
            "example" : {
                "steps_count": 1,
                "steps_counters" : ["1-ый"
                                    ],
                "steps_headers" : ["Определение параметров и постановка задачи"
                                   ],
                "steps_paths" : ["documentation/FirstLab/FirstExample.html",
                                 ]
            }
        },
        3 : {
            "header" : "Лабораторная работа №3",
            "variants_path": "documentation/FirstLab/Variants.html",
            "variants_count" : 19,
            "theory_path" : "documentation/FirstLab/FirstTheory.html",
        },
        4 : {
            "header" : "Лабораторная работа №4",
            "variants_path": "documentation/FirstLab/Variants.html",
            "variants_count" : 19,
            "theory_path" : "documentation/FirstLab/FirstTheory.html",
        },
    }