---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
menu:
  sidebar:
    name: {{ replace .Name "-" " " | title }}
    identifier: {{ .Name }}
    parent: posts
hero:
tags:
---
