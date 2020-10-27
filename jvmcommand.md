# JVM命令

## jps

列出正在运行的虚拟机进程;  

|选项 | 作用 |
|:---|:---|
|-q	| 只输出LVMID,省略主类名称|
|-m	|输出虚拟机进程启动时传递给主类Main的参数| 
|-l	|输出主类的全名，如果执行的是jar包，输出jar路径|
|-v	|输出虚拟机进程启动时JVM参数|

**命令示例**    
```bash
显示进程详细信息
jps -vlm
```

## jinfo
实时查看调整虚拟机的各项参数;  

|选项 | 作用 |
|:---|:---|
|-flags|输出全部的参数|
|-sysprops|输出系统属性|
|-flag name=value|设定对应名称的参数|
|-flag  name|输出对应名称的参数|

```bash 
## 输出进程系统属性
jinfo -sysprops 7356
```

## jstat 
用于监视虚拟机各种运行状态信息的命令行工具。它可以显示本地或远程虚拟机进程中的类装载、内存、垃圾收集、JIT编译等运行数据;

|选项 | 作用 |
|:---|:---|
|-class|监视类装载、卸载数量、总空间以及类装载所耗费的时间|
|-gc|监视java堆状况，包括eden区、两个survivor区、老年代、永久代等的容量、已用空间、<br>GC时间合计等信息|
|-gccapacity|监视内容与-gc基本相同，但输出主要关注JAVA堆各个区域使用到的最大、最小空间|
|-gcutil|监视内容与-gc基本相同，但输出主要关注已使用空间占空空间的百分比|
|-gccause|与-gcutil功能一样，但是会额外输出导致上一次GC产生的原因|
|-gcnew|监视新生代GC状况|
|-gcnewcapacity|监视内容与-gcnew基本相同，输出主要关注使用到的最大、最小空间|
|-gcold|监视老年代GC状况|
|-gcoldcapacity|监视内容与-gcold基本相同，输出主要关注使用到的最大、最小空间|
|-gcpermcapacity|输出永久代使用到的最大、最小空间|
|-compiler|输出JIT编译器编译过的方法、耗时等信息|
|-printcompilation|输出已经被JIT编译的方法|

### -class

**输出说明**
- Loaded：装载的类的数量
- Bytes：装载类的占用的字节数
- Unloaded：卸载类的数量
- Bytes：制裁类的字节数
- Time：装载和卸载类所花费的时间

**命令示例**   
```bash
$ jstat -class 7356
Loaded  Bytes  Unloaded  Bytes     Time
47224 99135.4       82    86.4      99.90
```

### -gc

**输出说明**

- S0C：年轻代中第一个survivor（幸存区）的容量（字节）
- S1C：年轻代中第二个survivor（幸存区）的容量 (字节)
- S0U：年轻代中第一个survivor（幸存区）目前已使用空间 (字节)
- S1U：年轻代中第二个survivor（幸存区）目前已使用空间 (字节)
- EC：年轻代中Eden（伊甸园）的容量 (字节)
- EU：年轻代中Eden（伊甸园）目前已使用空间 (字节)
- OC：Old代的容量 (字节)
- OU：Old代目前已使用空间 (字节)
- PC：Perm(持久代)的容量 (字节)
- PU：Perm(持久代)目前已使用空间 (字节)
- YGC：从应用程序启动到采样时年轻代中gc次数
- YGCT：从应用程序启动到采样时年轻代中gc所用时间(s)
- FGC：从应用程序启动到采样时old代(全gc)gc次数
- FGCT：从应用程序启动到采样时old代(全gc)gc所用时间(s)
- GCT：从应用程序启动到采样时gc用的总时间(s)


**命令示例**   
```bash
## 以字节方式查看内存及GC信息  
jstat -gc 7356
```



### -gcutil

**输出说明**

- S0：年轻代中第一个survivor（幸存区）已使用的占当前容量百分比
- S1：年轻代中第二个survivor（幸存区）已使用的占当前容量百分比
- E：年轻代中Eden（伊甸园）已使用的占当前容量百分比
- O：old代已使用的占当前容量百分比
- M：元数据区使用比例
- CCS：压缩使用比例
- P：perm代已使用的占当前容量百分比
- YGC：从应用程序启动到采样时年轻代中gc次数
- YGCT：从应用程序启动到采样时年轻代中gc所用时间(s)
- FGC：从应用程序启动到采样时old代(全gc)gc次数
- FGCT：从应用程序启动到采样时old代(全gc)gc所用时间(s)
- GCT：从应用程序启动到采样时gc用的总时间(s)

**命令示例**   
```bash
## 以百分比方式查看内存及GC信息 
jstat -gcutil 7356
```

### -gcnew

**输出说明**

- S0C：年轻代中第一个survivor（幸存区）的容量 (字节)
- S1C：年轻代中第二个survivor（幸存区）的容量 (字节)
- S0U：年轻代中第一个survivor（幸存区）目前已使用空间 (字节)
- S1U：年轻代中第二个survivor（幸存区）目前已使用空间 (字节)
- TT：持有次数限制
- DSS:期望的幸存区大小
- MTT：最大持有次数限制
- EC：年轻代中Eden（伊甸园）的容量 (字节)
- EU：年轻代中Eden（伊甸园）目前已使用空间 (字节)
- YGC：从应用程序启动到采样时年轻代中gc次数
- YGCT：从应用程序启动到采样时年轻代中gc所用时间(s)

**命令示例**   
```bash
## 查看年青代内存及GC信息
jstat -gcnew 7356
```

### -gcold

**输出说明**

- MC：Perm(持久代|方法区)的容量 (字节)
- MU：Perm(持久代|方法区)目前已使用空间 (字节)
- CCSC：压缩类空间大小
- CCSU：压缩类空间使用大小
- OC：Old代的容量 (字节)
- OU：Old代目前已使用空间 (字节)
- YGC：从应用程序启动到采样时年轻代中gc次数
- FGC：从应用程序启动到采样时old代(全gc)gc次数
- FGCT：从应用程序启动到采样时old代(全gc)gc所用时间(s)
- GCT：从应用程序启动到采样时gc用的总时间(s)

**命令示例**   
```bash
## 查看老年代内存及GC信息
jstat -gcold 7356
```

## jstack

虚拟机自带的一种堆栈跟踪工具;

|选项 | 作用 |
|:---|:---|
|-F|当正常输出请求不被响应时，强制输出线程栈堆。|
|-l|除线程栈堆外，显示关于锁的附加信息。|
|-m|如果调用本地方法的话，可以显示c/c++的栈堆|

```bash 
## 查看进程堆栈
jstack 7356
```