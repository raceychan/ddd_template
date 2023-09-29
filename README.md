# Table of Contents

- [Introduction](#Introduction)
- [Usage](#Usage)

# Introduction

Project template for ddd in python

> _Do not use this project in production use without modification!_

# Usage

## Build project from this template

### 1. Clone this repo

```bash
git clone https://github.com/raceychan/ddd_template.git
```

### 2. Remove git info

```
cd ddd_template && rm -rf .git
```

assure remove via

```
git remote -v
```

there should be nothing appear

### 3. Re-create git repo

```
git init
git remote add origin master # your repo url
```

## Tools

## Build docker images using make commands

```bash
make start
```

## Organize your entry-points in adapters

```python
python -m src.adapters.usecase
```

# How to start your project

## 1. Domain Modeling

Design your domain object

1. how do they look like?
2. what are the their relationships between them?
3. which one is the aggregate root?

## 2. Domain Services

Define operations allowed in your domain

## 3. Application Services

skip for now

## 4. Chose and develope your application dependency / Infrastructure

skip for now

## TODOs:

- [ ] add more examples
