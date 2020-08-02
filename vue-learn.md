# VUEJS

## v属性  
1. el 
绑定元素

2. data
数据

3. methods
方法

4. computed
计算属性，可以在这里对数据进行统计或者格式化  

```javascript
computed : {
    calc_fullName: {
        get : function() {
        return this.firstName + " " + this.lastName;
        }
    }
},
```
5. filters
过滤器

```javascript
filters : {
    showPrice(price) {
        return "$ " + price.toFixed(2);
    }
}
```

6. 局部组件注册

```javascript
const compDemo = Vue.extend({
    template:"<div><h2>标题</h2><p>h2h2h2h2h2h2h2h2</p></div>"
})
const app = new Vue({
    el : "#app",
    components : {
        Comp_demo : compDemo
    }
});
```


## 生命周期

1. beforeCreate

2. created

3. beforeMount

4. mounted

5. beforeUpdate

6. updated

7. beforeDestory

8. destroyed

## v指令  
1. v-for  
遍历,如果遍历的是列表，有些方法是不能做到响应式的,通过下标修改元素将不能响应式。
push(追加元素)、pop(删除最后元素)、shift(删除第一个元素)、unshift(在最前面添加元素)、splice(添加删除替换元素)、reverse(反转列表).


```xml
<li v-for="item in list"> {{item}} </li>
<li v-for="(item,index) in list"> {{index+1}}. {{item}} </li>
<li v-for="value in colors"> {{value}}</li>
<li v-for="(value,key) in colors"> {{ key }} - {{value}}</li>
<li v-for="(value,key,index) in colors" :key="key"> {{index}} - {{ key }} - {{value}}</li>
```
2. v-on  
绑定事件 

```xml
<button v-on:click="setCount(5)">重置到5</button>
<button v-on:click="count++">count++</button>
<button @click="setCount(25)">重置到25</button>
```
修饰符
```xml
<!-- 阻止事件冒泡 相当于event.stopPropagation() -->
<div @click.once="btnClick('div event',$event)">
    abcdefg
    <button @click.stop="btnClick('button event',$event)">btnClick</button>
</div>
<!-- 只触发一次 -->
<div @click.once="btnClick('div event',$event)">
<!-- 阻止默认事件 相当于event.preventDefault() -->
<form action="baidu">
    <input type="submit" value="提交" @click.prevent="submit_click()">
</form>
<!-- 键盘回调函数 当按下enter时触发  -->
<input type="text" id="barcode" @keyup.enter="barcodeEnter($event)">
```


3. v-if  
切换元素是否显示，如果不显示根本不渲染。

```xml
<h2 v-if="msg_display"> {{msg}} </h2>
```

4. v-once  
执行一次性地插值，当数据改变时，插值处的内容不会更新  

```xml
<span v-once>这个将不会改变: {{ msg }}</span>
```

5. v-bind
绑定html元素属性

```xml
<img v-bind:src="image" alt="" width="100px" height="100px">
<img :src="image" alt="" width="100px" height="100px">
<h2 :class="{text_red:isTextRed}" v-if="msg_display"> {{msg}} </h2>
```

6. v-show  
不管初始条件是什么，元素总是会被渲染，并且只是简单地基于 CSS 进行切换。在切换时效率更高。

```xml
<h1 v-show="ok">Hello!</h1>
```

7. v-model
表单元素与数据双向绑定

```xml
<input type="text" v-model="inputValue"><span> {{inputValue}} </span>
<div>
    <label for="male">
        <input type="radio" id="male" name="sex" value="1" v-model="sex">男
    </label>
    <label for="man">
        <input type="radio" id="man" name="sex" value="2" v-model="sex">女
    </label>
    <span>您选择的性别是： {{sex}}</span><br>
    <label for="agree">
        <input type="checkbox" name="agree" v-model="agree"> 我确认同意此协议
    </label>
    <span>用户是否同意:<span v-if="agree">同意</span><span v-else>不同意</span></span>
    <button :disabled="!agree">下一步</button><hr>
    <hr>
    <label v-for="item in hobbyArray" :for="item">
        <input type="checkbox" name="hobby" :id="item" :value="item" v-model="hobby"> {{item}}
    </label>
    您的爱好是 {{hobby}}
</div>

```

修饰符
```xml
<!-- lazy只有在回车或者失去焦点的时候绑定数据 -->
<!-- trim可以自动帮我们去掉空格符号 -->
<!-- number只允许输入数字 -->
<input type="text" v-model.lazy.trim="inputValue"><span> {{inputValue}} </span>
```

## 组件
Vue.extend()创建构造器

```javascript
const compDemo = Vue.extend({
    template:"<div><h2>{{title}}</h2><p>{{context}}</p></div>",
    data() {
        return {title:"标题",context:"正文h2h2h2h2h2"};
    }
})
```


注意：
组件不可以访问vue实例的数据

杂项：
```javascript
//调用子组件的方法
this.$children[0].event1(">|");
this.$refs.refcomp1.event1(",,");
//子组件调用父组件
this.$parent.parentEvent();
//子组件调用根组件
this.$root.parentEvent();
```
插槽
```xml
<slot_comp><span slot="left">左SP</span><span slot="right">右SP</span></slot_comp>
```

```javascript
components : {
    slot_comp : {
        template : "<div><slot name='left'><button>左边</button></slot><slot name='right'><button>右边</button></slot></div>",
    }
}
```

webpack

```javascript
resolve: {
alias: {
    'vue$': 'vue/dist/vue.esm.js'
}
},
```

```javascript

//pro.config.js
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')
const { merge } = require('webpack-merge');
const baseConfig = require('./base.config.js');

module.exports = merge(baseConfig, {
    plugins: [
        new UglifyJsPlugin()
    ]
});

//dev.config.js
const { merge } = require('webpack-merge');
const baseConfig = require('./base.config.js');

module.exports = merge([baseConfig, {
    devServer: {
        contentBase: './dist',
        port: 9000,

    }
}]);

//base.config.js
const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
    entry: './src/main.js',
    mode: 'development',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [{
            test: /\.css$/,
            use: ["style-loader", "css-loader"]
        }, {
            test: /\.(png|jpg|gif|jpeg)$/,
            use: [
                {
                    loader: 'url-loader',
                    options: {
                        limit: 8192
                    }
                }
            ]
        }, {
            test: /\.(png|jpg|gif)$/,
            use: [
                {
                    loader: 'file-loader',
                    options: {}
                }
            ]
        }, {
            test: /\.vue$/,
            loader: 'vue-loader'
        }, {
            test: /\.less$/,
            use: [{
                loader: "style-loader"
            }, {
                loader: "css-loader"
            }, {
                loader: "less-loader"
            }]
        }]
    },
    plugins: [
        new VueLoaderPlugin(),
    ],
    // runtime-compiler
    // resolve: {
    //     alias: {
    //         'vue$': 'vue/dist/vue.esm.js'
    //     }
    // }
};

```

## vue-router 
步骤1 安装vue-router  
```bash
npm install vue-router --save
```
步骤2 在模块中使用，首先导入路由对象，并申明使用插件，创建路由实例,并在其中配置路由和path的对应关系
/src/router/index.js
```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'
import About from '../components/About.vue'
import Home from '../components/Home.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    component: About
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

```

步骤3 在vue中挂载路由实例  
/src/main.js
```javascript
import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router/index'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```
步骤4 通过router-view和router-link渲染出来
```xml
<template>
  <div id="app">
    <div id="nav">
     <!-- router-link还有三个常用属性
		1. tag 可以指定标签最终渲染成什么组件
		2. replace: 可以不保留history记录
		3. active-class: 可以指定当标签被激活的时候，添加的class属性值
      -->
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>  
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

```

步骤4 程序实现路由跳转
```javascript
    this.$router.puth("/home");
```

步骤5 子路由
```javascript
	path:'/home',
	component: Home,
	children: [
		{
			path:'',
			redirect:'news'
		},{
			path:'news',
			component: HomeNew
		}
	]
```

路由中的传参
/src/router/index.js
```javascript
const routes = [
  {
    path: '/userInfo/:userCode',
    component: UserInfo,
    meta: {
      title: "用户信息"
    }
  },
  {
    path: '/firstPage',
    component: FirstPage,
    meta: {
      title: "首页"
    }
  }
  ];
```
/src/App.vue
```xml
<router-link to="/userInfo/abc">userInfo</router-link>|
<router-link :to="{path:'/firstPage',query:{userCode:'abc',userName:'zeimao77'}}">firstPage</router-link>
```
取参  
/src/util/routerutils.js
```javascript
const pathParam = function (vueComp, paramName) {
    var paramsMap = vueComp.$route.params;
    return paramsMap[paramName];
};

const queryParam = function (vueComp, queryName) {
    var paramMap = vueComp.$route.query;
    return paramMap[queryName];
}

export {
    pathParam, queryParam
}
```
/src/views/UserInfo.vue  
```javascript
import * as r from "../util/routerutils.js";

export default {
  //...
  computed: {
    userCode: {
      get() {
        return r.pathParam(this, "userCode");
      },
    },
  },
}
```
/src/views/FirstPage.vue
```javascript
import * as r from "../util/routerutils.js";

export default {
  //...
  computed: {
    userCode: {
      get() {
        return r.queryParam(this, "userCode");
      },
    },
    userName: {
      get() {
        return r.queryParam(this, "userName");
      },
    },
  },
};
```