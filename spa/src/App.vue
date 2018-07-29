    // src/App.vue
	
    <template>
      <div id="app">
      
      <router-link v-bind:to="'/'">HOME</router-link>   |  
      <router-link v-bind:to="'/insert'">INSERT</router-link>
      <router-view></router-view>
      
      </div>
    </template>
    
    <script>
    
    export default {
      name: 'app',
    }
    
    </script>
    <style>
    
    #app {
      font-family: 'Avenir', Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
      margin-top: 60px;
      text-decoration: none;
    }
    
    </style>