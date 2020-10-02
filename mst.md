## JAVA

### 并发

1. [初]在JVM中，线程可以分为daemon线程和普通线程，它们的主要区别  
> 答： daemon会随着main线程的停止而停止，普通线程则不会。

2. [初]JVM线程的状态迁移过程描述：
> 

![线程的状态迁移过程描述](https://zm.duzhaoteng.com/stadir/img/thread_state_graph.svg)

3. [初]volatile关键字的作用。一般在什么情况下使用volatile关键字。
> 答：volatile的作用有  
> - 64位写入原子性;
> - 内存可见性;
> - 禁止指令重排序;  
> 一般在多线程环境对一个变量的一写多读情况使用。  
> 如果是一写一读，使用无锁队列的内存屏障，不需要加锁，JDK8开始，Unsafe类提供了三个内存屏障函数。
> 如果是多写多读，则使用无锁队列CAS    

4. [初]描述一下interrupted函数的作用
> 答： interrupted函数相当于给线程发送了一个唤醒信号，如果此线程恰好处于WAITING或者TIME_WAITING状态，将会抛出InterruptedException异常。否则线程将什么也不做。在后断线程可以判断自己是否收到过中断信号来做中断处理。

5. [中]简述锁实现的基本原理，或者说实现一把锁的前提条件，也可以说锁的核心要素。  
> 答: 一把具有阻塞或唤醒功能的锁，需要具有几个核心要素：
> - 需要一个state变量，标记该锁的状态。至少有两个状态。对state的操作需要保证线程安全。一般使用CAS  
> - 需要记录当前哪个线程持有锁  
> - 需要底层支持将一个线程阻塞或唤醒操作  
```java
public class LockSupport {
// Unsafe类提供了阻塞和唤醒的操作原语
// LockSupport也是将Unsafe原语进行的封装。
public native void unpark(Object var1);
public native void park(boolean var1,long var2);
}
```
> - 需要一个队列维护所有阻塞的线程。这个队列也必须是线程安全的无锁队列。一般使用CAS实现  

6. [初]对于一个非常大的for查询，或者遍历对对象进行复杂操作，比较耗费时间，我们怎么提高效率。如何实现。  
> 答： 对于一个非常大的任务，我们通过做用就是将一个任务拆分成多个任务，交给多个CPU核心会完成。实现我们可以利用java8的parallelStream api方式来实现，它就是利用多核CPU优势做出来的。

7. [高]BlockingQueue是非常重要的并发容器接口，它定义了并发容器规范。从接口方法你可以获取到哪个信息,各方法有何特点。你知道其有哪个实现？描述其区别。
```java
public interface BlockingQueue<E> extends Queue<E> {
	// 添加到队列
	boolean add(E e);
	boolean offer(E e);
	void put(E e) throws InterruptedException;
	E poll(long timeout, TimeUnit unit) throws InterruptedException;
	boolean remove(Object o);
	E take() throws InterruptedException;
	E peek();
}
```
> 答： 从接口方法上分析:
>	对于入队给我们提供了add(),offer(),put()3个函数，从定义可以看到add()和offer()的返回是布尔类型，而put()无返回，还会抛出中断异常，所以可以判断add()和offer()是无阻塞的，put是阻塞式的。[由Queue接口定义:add()当队列满时，将抛出异常，offer()会返回false].  
>	对于出队给我们提供了remove(),peek(),take()函数，take()是阻塞式的,remove()和peek()是非阻塞式的。  
>	其重要子类有ArrayBlockingQueue、LinkedBlockingQeque、PriorityBlockingQueue、DelayQueue、SynchronousQueue......  
>	- ArrayBlockingQueue  
>	它是一个由数组实现的环形队列、在构造函数确定容量，它有一把锁(即lock)两个Condition(即notEmpty、notFull),因此put()和take()无法并发
>	- LinkedBlockingQeque  
>	它是一个基于单向链表形成的阻塞队列，它有两个把锁(即putLock、takeLock)两个Condition(即notEmpty、notFull),因为设计了两把锁，实现了队对队尾分开操作,所以put()和take()可以并发，但put()与put(),take()与take()不可以。因此count也必需是AtomicInteger。
>	- PriorityBlockingQueue  
>	队列通常是选进先出的，但这里实现了按元素的优先级从小到大列队。为此它的元素必需实现Comparable接口。它有一把锁(即lock)一个条件(即notEmpty)，当元素个数超出数组长度时,将执行扩容操作。
>	- DelayQueue  
>	延时队列,它是一个按延迟时间(未来将要执行时间-当前时间)从小到大的PriorityQueue。它所其中的元素必需实现Delayed接口。如果getDelay的值大小等于0.表示元素已经到期，需要出队。当队列头的元素延迟时间没到之前，队列被被阻塞。
>	- SynchronousQueue  
>	它是一个很特殊的BlockingqQueue,它本身没有容量，当一个线程调用put()时，线程会被阻塞，直到有另外一个线程调用take(),两个线程会同时解锁。对于多个线程调用put()会全部阻塞，直到多个线程调用take()所有线程会同时解锁。
>	- BlockingDueue <- LinkedBlockingDeque  
>	它定义了一个阻塞的双端队列接口，与LinkedBlockingQeque不同点是LinkedBlockingQeque是一个单向链表，LinkedBlockingDeque是一个双向链表，可以从头尾进行take()和Put()操作。
>	```java
>	public interface BlockingDeque<E> extends BlockingQueue<E>, Deque<E> {
>	void putFirst(E e) throws InterruptedException;
>	void putLast(E e) throws InterruptedException;
>	boolean offerFirst(E e, long timeout, TimeUnit unit) throws InterruptedException;
>	boolean offerLast(E e, long timeout, TimeUnit unit) throws InterruptedException;
>	}
>	```

8. [中]形成死锁的四个必要条件。  

> 答: 1. 互斥，某个资源只能被某一个线程独占。  
>     2. 占有且等待，当线程资源不能满足要求阻塞时,不主动释放持有的资源。   
>     3. 不剥夺其它线程占有资源,其它线程已经占有某个资源，不能因为自己也需要该资源就去抢夺该资源。  
>     4. 循环等待,存在一个进程链,使得每一个进程都占有下一个进程所需要的资源。  


### JAVA基础

1. JAVA servlet有哪九大空间?对于个一个未登录用户的购物车记录我们放在什么地方?   
> 答： servlet有九大内置空间，分别是config、application、exception、session、request、pagecontext、page、response、out,对于未登录的用户的购物车记录放到session空间最合适。

2. 简速你对hash函数的理解。能否完全通过hash来判断两个对象是否是严格意义上的同一对象，为什么? 在hashMap中，如果碰撞了是如何处理的。
> 答： hash函数是一个函数，它可以将任意长度的数据映射为一个固定长度的的数据，不能通过hash函数来判断严格意义上的同一对象，因为hash函数的结果是有限的，数据参数是无限的,所以当存在hash碰撞的时候无法判断。在hashmap中，相同hash的结果将被放到同一个链表（树）里。

