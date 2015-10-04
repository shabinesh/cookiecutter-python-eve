#!/usr/bin/env python
# -*- coding: utf-8 -*-

from {{cookiecutter.app_root}} import application


if __name__ == "__main__":
    #run applcation on port 8080
    application.run(port="8080")
