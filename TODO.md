1. device
    - section 数据结构 hostname/deviceName token platform
    - 采集的数据还有 电量 信号 等
    - 实现设备的状态监控信息回传
    - 开放http 和 socketIO api 用于订阅或主动获取全部或特定设备数据
    - 实现有中心的小文本广播（待定）
    - 实现有中心的小文件广播（待定）
    - 实现有中心的小文本定向发送（待定）
    - 实现有中心的小文件定向发送（待定）
    
2. notify
    - ~~区分通道类型，全广播，仅广播到监视器~~
    
3. file
    - 有中心的文件发送
    
4. node
    - 无中心的文件等发送 这个不算是
    
    
5. InfoSpider
    - 外卖、快递等的爬虫，，通过notify发送到设备
    

4. 整体架构
    - 研究namespace和room，一定要将不同的数据分开，，择优采用
    - 将root namespace 改成 “/”
    - 使用namespace区分app，room区分用户，入口区分设备