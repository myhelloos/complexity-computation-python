
# 环境设置
```bash
pip3 install virtualenvwrapper
```

## edit `.zshrc`
```bash
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export WORKON_HOME=~/venvs
source /usr/local/bin/virtualenvwrapper.sh
```

## then install new virtualenv
```bash
mkvirtualenv ccp
```

# 安装依赖
```bash
pip install -r requirement.txt
```

# freeze
```bash
pip freeze > requirement.txt 
```

## 额外
### 修改pip源镜像地址

```bash
[global]
index-url = https://mirrors.ustc.edu.cn/pypi/web/simple
format = columns
```