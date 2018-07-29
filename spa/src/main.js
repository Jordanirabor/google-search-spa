  // The steps are numbered below
    
    // 1
    import Vue from 'vue'
    
    // 2
    import App from './App'
    
    // 3
    import VueRouter from 'vue-router'
    
    // 4
    import Searchbox from './components/Searchbox'
    
    // 5
    import Insert from './components/Insert'
    
    // 6
    Vue.use(VueRouter)
    
    // 7
    const routes = [
    
    { path: '/', component: Searchbox },
    
    { path: '/insert', component: Insert }
    
    ]
    
    // 8
    const router = new VueRouter({
      routes, 
      mode: 'history'
    })
    
    // 9
    new Vue({
    
      el: '#app',
      
      template: '<App/>',
      
      components: { App },
    
      router
      
    }).$mount('#app')