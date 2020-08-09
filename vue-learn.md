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
步骤6 hook
[官网文档](https://router.vuejs.org/zh/guide/advanced/navigation-guards.html#%E5%85%A8%E5%B1%80%E5%89%8D%E7%BD%AE%E5%AE%88%E5%8D%AB)

```javascript
//路由跳转的前置钩子函数
router.beforeEach((to, from, next) => {
  document.title = to.matched[0].meta.title;
  next()
})
//路由跳转的后置钩子函数
router.afterEach()
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

## 保持活性  
[官网文档](https://cn.vuejs.org/v2/api/#keep-alive)  
keep-alive是vue的一个内置组件，可以使组件保留状态，避免重新渲染
它有两个重要属性include、exclude用来添加或排除缓存，这里配置组件的name属性
```xml
<keep-alive>
  <router-view />
</keep-alive>
``` 
与之相关有三个属性  
1. **include** - 字符串或正则表达式。只有名称匹配的组件会被缓存。
2. **exclude** - 字符串或正则表达式。任何名称匹配的组件都不会被缓存。
3. **max** - 数字。最多可以缓存多少组件实例。  

与之相关有两函数
```javascript
  //当页面被激活的时候触发
  activated() {
    console.log("activated");
  },
  //当页面失活的时候触发 
  deactivated() {
    console.log("deactivated");
  },

```
## vuex  

安装：
```bash
npm install vuex --save
```

vuex有五个非常重要的属性：

1. state 单一状态树  
对于一个未在此初始化的属性，并不能正常做到响应式刷新视图。这时候我们需要使用Vue提供的两个函数来实现  
```javascript
Vue.set(对象或列表,键值或索引,新值);
Vue.delete(对象或列表，键值或索引);
```

2. 更改 Vuex 的 store 中的状态的唯一方法是提交 mutation。  
```javascript
// 定义mutations 
mutations: {
    setTabBarActive(state, payload) {
        state.tabbarActive = payload.tabbarActive;
        console.log("change state tabbarAcitve:" + state.tabbarActive);
    },
    tabBarActive(state, o) {
        state.tabbarActive = o;
        console.log(state.tabbarActive);
    }
}
// 提交的方法通常有两种：
// 方式一：
this.$store.commit("tabBarActive", data.tabBarTitle);
// 方式二:
this.$store.commit({
  type: "setTabBarActive",
  tabbarActive: data.tabBarTitle,
});
```

3. action 
[官方文档](https://vuex.vuejs.org/zh/guide/actions.html)  
Action 可以包含任意异步操作。  

## axios

**全局axios**
```javascript
import axios from 'axios'
axios.defaults.baseURL = "https://zm.duzhaoteng.com";
//使用：
axios({
    url: "/qiqiweb/rest/open/iphoneClock"
}).then(result => {
    context.commit({
        type: mf.MF_NEXTWORKDAY,
        data: result.data,
    });
});
```

**axios实例**

```javascript
const inst1 = axios.create({
  baseURL:"http://www.baidu.com"
  timeout: 3000
})
```

## 最终项目示例配置

目录结构
```bash
├── package.json
├── build
│   ├── base.config.js
│   ├── dev.config.js
│   ├── dist
│   │   └── index.html
│   └── pro.config.js
├── node_modules
│   ├── ......
└── src
    ├── App.vue
    ├── assets
    │   ├── css
    │   └── img
    ├── components
    │   └── content
    ├── main.js
    ├── network
    │   └── main-request.js
    ├── router
    │   └── index.js
    ├── store
    │   ├── actions.js
    │   ├── index.js
    │   ├── mutations.js
    │   └── mutation-type.js
    ├── util
    │   └── routerutils.js
    └── views
        └─── home
            └── Home.vue
```

webpack.json   
```json
{
  "name": "web-demo2",
  "version": "1.0.0",
  "description": "",
  "scripts": {
    "build": "webpack --config ./build/pro.config.js",
    "dev": "webpack --config ./build/dev.config.js",
    "start": "webpack-dev-server --config ./build/dev.config.js --open"
  },
  "keywords": [],
  "author": "zeimao77",
  "devDependencies": {
    "cnpm": "^6.1.1",
    "css-loader": "^4.0.0",
    "file-loader": "^6.0.0",
    "less": "^3.12.2",
    "less-loader": "^6.2.0",
    "style-loader": "^1.2.1",
    "uglifyjs-webpack-plugin": "^2.2.0",
    "url-loader": "^4.1.0",
    "vue": "^2.6.11",
    "vue-loader": "^15.9.3",
    "vue-template-compiler": "^2.6.11",
    "webpack": "^4.44.0",
    "webpack-cli": "^3.3.12",
    "webpack-dev-server": "^3.11.0",
    "webpack-merge": "^5.0.9"
  },
  "dependencies": {
    "axios": "^0.19.2",
    "vue-router": "^3.4.2",
    "vuex": "^3.5.1"
  }
}
```

build/base.config.js  
```javascript
const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
    entry: "/home/zeimao77/桌面/web-demo2/src/main.js",
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            }, {
                test: /\.(png|jpg|gif)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            esModule: false
                        }
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
    resolve: {
        alias: {
            '@': path.resolve('src'),
        }
    }
};
```

build/dev.config.js  
```javascript
const { merge } = require('webpack-merge');
const baseConfig = require('./base.config.js');
const path = require('path');

module.exports = merge([baseConfig, {
    devServer: {
        contentBase: path.resolve(__dirname, 'dist'),
        port: 9000,
        hot: true,
        historyApiFallback: true
    }
}]);
```
build/pro.config.js  
```javascript
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')
const { merge } = require('webpack-merge');
const baseConfig = require('./base.config.js');

module.exports = merge(baseConfig, {
    mode: 'production',
    plugins: [
        new UglifyJsPlugin()
    ]
});
```

src/main.js
```javascript
import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router/index'
import store from '@/store/index'

Vue.config.productionTip = false

axios.defaults.baseURL = "https://zm.duzhaoteng.com";

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
```
路由 
src/router/index.js
```javascript
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const Home = () => import("@/views/home/Home.vue")

const routes = [
    {
        path: "",
        redirect: "/home"
    }, {
        path: "/home",
        component: Home
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
```

AJAX    
src/network/main-request.js  
```javascript
import axios from 'axios'

function mainRequest(conf) {
    const mainwork = axios.create({
        baseURL: "https://zm.duzhaoteng.com",
        timeout: 3000
    })

    mainwork.interceptors.request.use(config => {
        console.log(config);
        return config;
    }, err => {
        console.log(err);
    });
    return mainwork(conf);
}

export {
    mainRequest
}
```

vuex 
src/store/index.js  
```javascript
import Vue from 'vue'
import Vuex from 'vuex'
import mutations from '@/store/mutations'
import actions from '@/store/actions'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        tabbarActive: "首页",
        nextWorkDay: "1970-01-01",
        userInfo: {
            loginState: 1,
            userName: "zeimao",
            token: "sadfDFlasdownbcx",
            role: "admin"
        }
    },
    mutations,
    actions,
    getters: {

    },
    modules: {

    }

})

export default store
```
src/store/actions.js  
```javascript  
import * as mf from '@/store/mutation-type'
import { mainRequest } from '@/network/main-request'

export default {
    [mf.AF_SETUSERINFO](context, payload) {
        console.log(payload);
        return new Promise((resolve, reject) => {
            mainRequest({
                url: "/qiqiweb/rest/open/iphoneClock"
            }).then(result => {
                context.commit({
                    type: mf.MF_NEXTWORKDAY,
                    data: result.data,
                });
            });
            setTimeout(() => {
                context.commit({
                    type: mf.MF_SETUSERINFO,
                    loginState: 1,
                    userName: "zeimao77",
                    token: "AFBDEFG"
                });
                resolve("AF用户登录完成！！！");
            }, 2000);
        })
    }
}
```

src/store/mutation-type.js  
```javascript
export const MF_SETTABBARACTIVE = "SETTABBARACTIVE";
export const AF_SETUSERINFO = "SETUSERINFO";
export const MF_SETUSERINFO = "SETUSERINFOA";
export const MF_NEXTWORKDAY = "NEXTWORKDAY";
```

src/store/mutations.js  
```javascript 
import * as mf from '@/store/mutation-type'

export default {
    [mf.MF_SETTABBARACTIVE](state, payload) {
        state.tabbarActive = payload.tabbarActive;
        console.log("change state tabbarAcitve:" + state.tabbarActive);
    },
    [mf.MF_SETUSERINFO](state, payload) {
        state.userInfo.loginState = payload.loginState;
        state.userInfo.userName = payload.userName;
        state.userInfo.token = payload.token;
    },
    [mf.MF_NEXTWORKDAY](state, payload) {
        console.log("payload")
        console.log(payload)
        state.nextWorkDay = payload.data.data.nextWorkDay;
    },
    tabBarActive(state, o) {
        state.tabbarActive = o;
        console.log(state.tabbarActive);
    }
}
```

src/util/routerutils.js  
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



