#微博批量删除工具

##Introduction
批量删除微博工具是一款使用Python语言开发的简陋工具其中还有很多需要完善的地方；
开发过程中使用了fiddler抓包用具用于分析网络请求，还使用了正则表达式来匹配关键内容；总体如下：

 - 获取mid：获取mid的url中关键参数为年月，对应脚本中的getmids()方法；此方法返回参数对应月所发微博列表；但是是以html形式组成，需要进行数据清洗获取最关键的mid;
 - 删除mid:数据清洗完毕后会获得一个mid列表，遍历此列表调用delmid()方法即可完成数据删除；
 -  不足点：本脚本日期参数为人为传递，更科学的方法应该是解析列表获取日期，第二点脚本速度有点慢，也许是微博接口的原因吧，但这也有好处，这样就不用人为降低访问频率了，避免了微博的屏蔽；

##Building

本脚本使用Python3开发环境

## License

Licensed under the Apache License, Version 2.0 (the "License"); you may not 
use this file except in compliance with the License. You may obtain a copy 
of the License [here](http://www.apache.org/licenses/LICENSE-2.0).

