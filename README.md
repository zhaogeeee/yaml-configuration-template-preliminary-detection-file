# yaml-configuration-template-preliminary-detection-file
仅是新手自己练手使用
# Bucket Access Checker

Bucket Access Checker 是一个用于检测百度云存储（Baidu Cloud Storage，简称 BOS）中指定 Bucket 的访问权限的桌面应用程序。

## 功能

- 输入有效的 Access Key ID 和 Secret Access Key
- 输入要检查的 Bucket 名称
- 检测 Bucket 的访问权限设置
- 显示结果：如果 Bucket 是公开访问的，将显示相应消息；否则，将显示不是公开访问的提示。

## 运行环境

- Python 3.x

## 安装依赖

```shell
pip install tkinter baidubce
```

## 如何使用

1. 在根目录运行以下命令启动应用程序：

    ```shell
    python main.py
    ```

2. 在应用程序界面中输入有效的 Access Key ID 和 Secret Access Key。
3. 输入要检查的 Bucket 名称。
4. 点击 "检测" 按钮，等待程序执行检测。
5. 结果将在界面中显示。

注意：确保已提供正确有效的密钥信息以及要检查的 Bucket 名称。

## 注意事项

- 请确保您拥有有效的 Baidu Cloud Storage (BOS) 账户并具有足够的权限来访问和管理所选的 Bucket。
- 使用此应用程序时，建议在安全环境中处理密钥信息，并确保不泄露给未经授权的用户。

## 参考资料

- [百度云存储官方文档](https://cloud.baidu.com/doc/BOS/Developer-Resource.html)

请根据实际情况进行适当修改和补充的README文件。
