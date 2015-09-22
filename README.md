# iPhoneSMSMailer
iPhone收到短信时发送邮件到指定邮箱

#环境配置
以下环境测试下没有问题

- iPhone5S 
- Python2.7
- sqlite3 3.7.13

```
Rming:~ root# cat  /System/Library/CoreServices/SystemVersion.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
        <key>ProductBuildVersion</key>
        <string>12B440</string>
        <key>ProductCopyright</key>
        <string>1983-2014 Apple Inc.</string>
        <key>ProductName</key>
        <string>iPhone OS</string>
        <key>ProductVersion</key>
        <string>8.1.2</string>
</dict>
</plist>
````


```
Python 2.7.3 (default, Aug 11 2012, 10:54:38)
[GCC 4.2.1 Compatible Apple Clang 3.0 (tags/Apple/clang-211.11)] on darwin
```

```
Rming:~ root# sqlite3 --version
3.7.13
```

需要修改脚本中smtp设置`smtpConfig` 和 接受者`reviever` 

